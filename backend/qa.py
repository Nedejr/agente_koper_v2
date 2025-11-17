"""
Módulo responsável pelo sistema de Q&A usando RAG
"""

import re
from typing import List, Optional, Tuple

from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from .config import Config
from .improved_prompts import (
    IMPROVED_SYSTEM_PROMPT,
    detect_prompt_type,
    get_prompt_by_type,
)

# Prompt padrão (mantido para compatibilidade)
DEFAULT_SYSTEM_PROMPT = IMPROVED_SYSTEM_PROMPT


def build_prompt_with_history(
    system_prompt: str, chat_history: Optional[List[dict]] = None
) -> ChatPromptTemplate:
    """
    Constrói um prompt do ChatGPT incluindo histórico de conversa

    Args:
        system_prompt: Prompt do sistema
        chat_history: Lista de mensagens anteriores [{'role': 'user'/'ai', 'content': '...'}]

    Returns:
        ChatPromptTemplate configurado
    """
    messages = [("system", system_prompt)]

    if chat_history:
        for message in chat_history:
            role = message.get("role")
            content = message.get("content")

            # Converte role 'user' ou 'ai' para formato do langchain
            if role == "user":
                messages.append(("human", content))
            elif role == "ai":
                messages.append(("assistant", content))

    # Adiciona a pergunta atual
    messages.append(("human", "{input}"))

    return ChatPromptTemplate.from_messages(messages)


def _extract_image_tags(text: str) -> List[str]:
    """
    Extrai todas as tags de imagem do texto.

    Args:
        text: Texto contendo tags [image: filename.png]

    Returns:
        Lista de nomes de arquivos de imagem
    """
    if not text:
        return []
    pattern = r"\[image:\s*([^\]]+)\]"
    matches = re.findall(pattern, text)
    # Filtra valores None ou vazios
    return [m.strip() for m in matches if m and m.strip()]


def _extract_video_tags(text: str) -> List[str]:
    """
    Extrai todas as tags de vídeo do texto.

    Args:
        text: Texto contendo tags [video: filename.mp4]

    Returns:
        Lista de nomes de arquivos de vídeo
    """
    if not text:
        return []
    pattern = r"\[video:\s*([^\]]+)\]"
    matches = re.findall(pattern, text)
    # Filtra valores None ou vazios
    return [m.strip() for m in matches if m and m.strip()]


def _extract_media_tags(text: str) -> List[tuple]:
    """
    Extrai todas as tags de mídia (imagens e vídeos) do texto.

    Args:
        text: Texto contendo tags [image: ...] e [video: ...]

    Returns:
        Lista de tuplas (tipo, nome_arquivo) onde tipo é 'image' ou 'video'
    """
    media = []

    # Extrai imagens
    for img in _extract_image_tags(text):
        media.append(("image", img))

    # Extrai vídeos
    for video in _extract_video_tags(text):
        media.append(("video", video))

    return media


def _add_timestamps_to_videos(response: str, video_timestamps_map: dict) -> str:
    """
    Adiciona timestamps às tags de vídeo na resposta.
    Converte [video: nome.mp4] para [video: nome.mp4#t=00:18,00:43]

    Args:
        response: Resposta com tags de vídeo
        video_timestamps_map: Dicionário {video_name: [{"start": "00:18", "end": "00:43", "line": "..."}, ...]}

    Returns:
        Resposta com timestamps adicionados às tags de vídeo (formato: #t=start,end)
    """
    if not response:
        return response

    for video_name, timestamps_list in video_timestamps_map.items():
        # timestamps_list é uma LISTA de dicionários
        if timestamps_list and len(timestamps_list) > 0:
            # Usa o primeiro timestamp (pode ser melhorado com seleção inteligente)
            first_timestamp = timestamps_list[0]
            start = first_timestamp.get("start") if first_timestamp else None
            end = first_timestamp.get("end") if first_timestamp else None

            if start and end:
                # Procura pela tag do vídeo e adiciona timestamp
                # Formato: #t=start,end (com vírgula, não hífen)
                old_tag = f"[video: {video_name}]"
                new_tag = f"[video: {video_name}#t={start},{end}]"
                response = response.replace(old_tag, new_tag)

    return response


def _find_relevant_timestamp_for_query(query: str, video_timestamps_map: dict) -> dict:
    """
    Busca o timestamp mais relevante do vídeo baseado na query do usuário.
    Procura por palavras-chave da pergunta no conteúdo dos timestamps.

    Args:
        query: Pergunta do usuário
        video_timestamps_map: Mapa de timestamps dos vídeos

    Returns:
        Dicionário com o timestamp mais relevante ou None
    """
    if not video_timestamps_map or not query:
        return None

    query_lower = query.lower()

    # Remove palavras comuns (stopwords)
    stopwords = [
        "como",
        "o",
        "a",
        "de",
        "em",
        "para",
        "do",
        "da",
        "no",
        "na",
        "os",
        "as",
        "dos",
        "das",
        "nos",
        "nas",
        "um",
        "uma",
        "uns",
        "umas",
        "ao",
        "aos",
        "à",
        "às",
        "pelo",
        "pela",
        "pelos",
        "pelas",
        "é",
        "são",
        "foi",
        "foram",
        "fazer",
        "eu",
        "tu",
        "ele",
        "ela",
        "nós",
        "vós",
        "eles",
        "elas",
        "que",
        "qual",
        "onde",
        "quando",
    ]

    # Extrai palavras-chave da query
    query_words = [
        w.strip().rstrip("?!.,;:")
        for w in query_lower.split()
        if w.strip().rstrip("?!.,;:") not in stopwords and len(w.strip()) > 2
    ]

    # Palavras compostas importantes (bigramas)
    bigramas_importantes = []
    words_list = query_lower.split()
    for i in range(len(words_list) - 1):
        bigrama = f"{words_list[i]} {words_list[i+1]}"
        # Remove pontuação
        bigrama = bigrama.rstrip("?!.,;:")
        if words_list[i] not in stopwords or words_list[i + 1] not in stopwords:
            bigramas_importantes.append(bigrama)

    best_timestamp = None
    best_score = 0

    # Para cada vídeo no mapa
    for video_name, ts_list in video_timestamps_map.items():
        if not ts_list:
            continue

        # Para cada timestamp deste vídeo
        for ts_info in ts_list:
            line = ts_info.get("line", "").lower()
            if not line:
                continue

            score = 0

            # 1. Bonus por bigramas (frases compostas) - PESO 5
            for bigrama in bigramas_importantes:
                if bigrama in line:
                    score += 5

            # 2. Bonus por palavras-chave individuais - PESO 1
            for word in query_words:
                if word in line:
                    score += 1

            # 3. BONUS EXTRA: Se a linha contém TODAS as palavras principais - PESO 10
            palavras_principais = [
                w for w in query_words if len(w) > 4
            ]  # Palavras com mais de 4 letras
            if palavras_principais and all(
                palavra in line for palavra in palavras_principais
            ):
                score += 10

            # 4. BONUS: Match exato de termos técnicos - PESO 8
            termos_tecnicos = [
                "histórico",
                "movimentação",
                "estoque",
                "transferência",
                "balanço",
                "entrada",
                "saída",
                "solicitação",
                "equipamento",
            ]
            for termo in termos_tecnicos:
                if termo in query_lower and termo in line:
                    score += 8

            # Atualiza melhor timestamp se score for maior
            if score > best_score:
                best_score = score
                best_timestamp = ts_info

    # Se nenhum timestamp relevante foi encontrado, retorna o primeiro disponível
    if not best_timestamp:
        for ts_list in video_timestamps_map.values():
            if ts_list and len(ts_list) > 0:
                best_timestamp = ts_list[0]
                break

    return best_timestamp


def _add_youtube_links_to_response(
    response: str, youtube_urls: dict, video_timestamps_map: dict, query: str = ""
) -> str:
    """
    Adiciona embeds do YouTube com timestamps nas menções de vídeo na resposta.
    Cria um player embedado que inicia no timestamp correto.

    Args:
        response: Resposta gerada
        youtube_urls: Dicionário {source_name: youtube_url}
        video_timestamps_map: Timestamps dos vídeos
        query: Pergunta original do usuário (para buscar timestamp relevante)

    Returns:
        Resposta com embeds do YouTube adicionados
    """
    if not response or not youtube_urls:
        return response

    # Procura por menções de vídeos na resposta
    # Padrão atualizado para aceitar URLs completas com parâmetros (?, &, =)
    video_pattern = r"\[video:\s*([^\]]+?)\]"

    def replace_with_youtube_embed(match):
        video_content = match.group(1).strip()

        # Verifica se tem timestamp no formato #t=START,END
        timestamp_match = re.search(r"#t=([^,]+),([^\s]+)", video_content)
        start_time = timestamp_match.group(1) if timestamp_match else None
        end_time = timestamp_match.group(2) if timestamp_match else None

        # Remove timestamp da URL se presente
        video_url = re.sub(r"#t=[^,]+,[^\s]+", "", video_content).strip()

        # Se já é uma URL do YouTube, usa diretamente
        if "youtube.com" in video_url or "youtu.be" in video_url:
            youtube_url = video_url
        else:
            # Caso contrário, procura URL nos metadados
            youtube_url = None
            for source, url in youtube_urls.items():
                if video_content in source or source in video_content:
                    youtube_url = url
                    break

            if not youtube_url:
                # Tenta encontrar qualquer URL do YouTube disponível
                youtube_url = list(youtube_urls.values())[0] if youtube_urls else None

        if youtube_url:
            # Se não tem timestamp especificado, busca o mais relevante para a query
            if not start_time and video_timestamps_map:
                relevant_ts = _find_relevant_timestamp_for_query(
                    query, video_timestamps_map
                )
                if relevant_ts:
                    start_time = relevant_ts.get("start", None)
                    end_time = relevant_ts.get("end", None)

            # Converte timestamp para segundos se disponível
            seconds = 0
            if start_time:
                # Converte MM:SS ou HH:MM:SS para segundos
                time_parts = start_time.split(":")
                if len(time_parts) == 2:
                    seconds = int(time_parts[0]) * 60 + int(time_parts[1])
                elif len(time_parts) == 3:
                    seconds = (
                        int(time_parts[0]) * 3600
                        + int(time_parts[1]) * 60
                        + int(time_parts[2])
                    )

            # Extrai o ID do vídeo do YouTube
            video_id = None
            if "youtube.com/watch?v=" in youtube_url:
                video_id = youtube_url.split("watch?v=")[1].split("&")[0]
            elif "youtu.be/" in youtube_url:
                video_id = youtube_url.split("youtu.be/")[1].split("?")[0]

            if video_id:
                # Cria embed do YouTube com timestamp
                # Usa marcador especial YOUTUBE_EMBED que o frontend processará
                embed_url = f"https://www.youtube.com/embed/{video_id}"
                if seconds > 0:
                    embed_url += f"?start={seconds}"

                # Retorna formato especial para o frontend processar
                if start_time and end_time:
                    return f"\n\n🎬 **Vídeo Tutorial ({start_time} → {end_time}):**\n\n[YOUTUBE_EMBED:{embed_url}]\n"
                else:
                    return (
                        f"\n\n🎬 **Vídeo Tutorial:**\n\n[YOUTUBE_EMBED:{embed_url}]\n"
                    )

        # Se não encontrou URL, retorna tag original
        return match.group(0)

    response = re.sub(video_pattern, replace_with_youtube_embed, response)

    return response


def _ensure_media_in_response(response: str, context_media: List[tuple]) -> str:
    """
    Garante que UMA mídia relevante do contexto esteja na resposta.
    PRIORIDADE: 1 vídeo > 1 imagem
    - Se houver vídeo no contexto, inclui APENAS o primeiro vídeo
    - Se NÃO houver vídeo, inclui APENAS a primeira imagem
    - Remove duplicatas e garante apenas uma mídia por resposta

    Args:
        response: Resposta gerada pelo modelo
        context_media: Lista de tuplas (tipo, nome_arquivo) encontradas no contexto

    Returns:
        Resposta com APENAS UMA mídia (1 vídeo ou 1 imagem), sem duplicatas
    """
    # Separa vídeos e imagens do contexto
    context_videos = [m for m in context_media if m[0] == "video"]
    context_images = [m for m in context_media if m[0] == "image"]

    # Determina qual mídia devemos garantir na resposta (prioridade: vídeo > imagem)
    priority_media = None
    if context_videos:
        # Se há vídeos no contexto, escolhe o primeiro
        priority_media = context_videos[0]
    elif context_images:
        # Se não há vídeos mas há imagens, escolhe a primeira
        priority_media = context_images[0]

    # Remove TODAS as tags de mídia da resposta para garantir apenas uma
    lines = response.split("\n")
    cleaned_lines = []
    found_priority_media = False

    for line in lines:
        # Verifica se a linha contém uma tag de imagem
        img_match = re.search(r"\[image:\s*([^\]]+)\]", line)
        if img_match:
            img_name = img_match.group(1)
            if img_name:
                img_name = img_name.strip()
            else:
                # Se não há nome de imagem, ignora esta linha
                cleaned_lines.append(line)
                continue

            # Só mantém se for a mídia prioritária E ainda não encontramos ela
            if (
                priority_media
                and priority_media == ("image", img_name)
                and not found_priority_media
            ):
                found_priority_media = True
                cleaned_lines.append(line)
            # Caso contrário, remove esta linha
            continue

        # Verifica se a linha contém uma tag de vídeo
        video_match = re.search(r"\[video:\s*([^\]]+)\]", line)
        if video_match:
            video_name = video_match.group(1)
            if video_name:
                video_name = video_name.strip()
            else:
                # Se não há nome de vídeo, ignora esta linha
                cleaned_lines.append(line)
                continue

            # Só mantém se for a mídia prioritária E ainda não encontramos ela
            if (
                priority_media
                and priority_media == ("video", video_name)
                and not found_priority_media
            ):
                found_priority_media = True
                cleaned_lines.append(line)
            # Caso contrário, remove esta linha
            continue

        # Linha normal, adiciona
        cleaned_lines.append(line)

    response = "\n".join(cleaned_lines)

    # Se a mídia prioritária não foi encontrada na resposta, adiciona ao final
    if priority_media and not found_priority_media:
        media_type, media_name = priority_media
        response += f"\n\n[{media_type}: {media_name}]\n"

    return response


def ask_question(
    query: str,
    vector_store: Chroma,
    model_name: str = None,
    chat_history: Optional[List[dict]] = None,
    system_prompt: str = None,
    temperature: float = None,
) -> dict:
    """
    Faz uma pergunta ao sistema RAG e anexa referências de imagem se encontradas.

    Args:
        query: Pergunta do usuário
        vector_store: Vector store com os documentos
        model_name: Nome do modelo OpenAI (opcional, usa default)
        chat_history: Histórico de conversa (opcional)
        system_prompt: Prompt customizado (opcional, usa default melhorado)
        temperature: Temperatura do modelo (opcional, usa default)

    Returns:
        Dicionário com a resposta e os documentos fonte.
    """
    # Usa valores padrão se não fornecidos
    if model_name is None:
        model_name = Config.DEFAULT_MODEL

    if system_prompt is None:
        # Detecta automaticamente o melhor prompt baseado na query
        prompt_type = detect_prompt_type(query)
        system_prompt = get_prompt_by_type(prompt_type)

    if temperature is None:
        temperature = Config.TEMPERATURE

    # Cria o modelo LLM
    llm = ChatOpenAI(model=model_name, temperature=temperature)

    # Cria o retriever otimizado
    # Usa MMR (Maximal Marginal Relevance) para diversidade nos resultados
    # MELHORADO: Busca mais documentos e prioriza relevância
    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": Config.K_RETRIEVER + 2,  # Aumentado de 6 para 8 documentos
            "fetch_k": (Config.K_RETRIEVER + 2) * 3,  # Busca 3x mais para filtrar
            "lambda_mult": 0.85,  # 0.85 = mais peso para relevância (antes era 0.7)
        },
    )

    # Busca documentos relevantes
    docs = retriever.invoke(query)

    # SEMPRE busca chunks que têm timestamps de vídeos para adicionar ao contexto
    # Isso garante que vídeos tutoriais sejam incluídos mesmo que os docs recuperados
    # não mencionem diretamente os vídeos
    collection = vector_store._collection
    all_docs_with_ts = collection.get(where={"has_timestamps": "true"}, limit=10)

    # Adiciona esses documentos aos docs recuperados
    if all_docs_with_ts and all_docs_with_ts["ids"]:
        from langchain_core.documents import Document

        for idx, (doc_id, content, metadata) in enumerate(
            zip(
                all_docs_with_ts["ids"],
                all_docs_with_ts["documents"],
                all_docs_with_ts["metadatas"],
            )
        ):
            # Cria um Document do LangChain
            ts_doc = Document(page_content=content, metadata=metadata)
            # Adiciona aos docs se ainda não estiver lá
            if ts_doc not in docs:
                docs.append(ts_doc)

    # Formata o contexto, incluindo as tags de imagem/vídeo que já estão no conteúdo
    # O processamento em `processing.py` já substitui a sintaxe Markdown de imagem
    # por uma tag como `[image: nome-da-imagem.png]`.
    # Também inclui timestamps de vídeos quando disponíveis nos metadados.
    context_parts = []
    video_timestamps_map = {}  # Mapa para armazenar timestamps de vídeos
    youtube_urls = {}  # Mapa para armazenar URLs do YouTube

    for i, doc in enumerate(docs):
        source_name = doc.metadata.get("source", "desconhecida")

        # Extrai URL do YouTube se disponível
        if "youtube_url" in doc.metadata:
            youtube_urls[source_name] = doc.metadata["youtube_url"]

        # Remove a seção de timestamps do conteúdo para não aparecer no contexto do LLM
        content = doc.page_content
        timestamps_json = None

        # Extrai timestamps se presentes no conteúdo
        if "[VIDEO_TIMESTAMPS_DATA]" in content:
            import json
            import re

            # Extrai o JSON de timestamps
            match = re.search(
                r"\[VIDEO_TIMESTAMPS_DATA\]\s*\n(.*?)\n\[/VIDEO_TIMESTAMPS_DATA\]",
                content,
                re.DOTALL,
            )
            if match:
                timestamps_json = match.group(1)
                # Remove a seção de timestamps do conteúdo
                content = re.sub(
                    r"\n\n\[VIDEO_TIMESTAMPS_DATA\].*?\[/VIDEO_TIMESTAMPS_DATA\]\n",
                    "",
                    content,
                    flags=re.DOTALL,
                )

        context_part = f"---\nFonte {i+1} (de {source_name}):\n{content}"

        # Extrai timestamps de vídeos se disponíveis
        if timestamps_json:
            timestamps = json.loads(timestamps_json)

            # Atualiza o mapa de timestamps
            for video_name, ts_list in timestamps.items():
                if video_name not in video_timestamps_map:
                    video_timestamps_map[video_name] = []
                video_timestamps_map[video_name].extend(ts_list)

            # Adiciona informação de timestamps ao contexto para o LLM
            if timestamps:
                context_part += "\n\n[TIMESTAMPS DISPONÍVEIS]:\n"
                for video_name, ts_list in timestamps.items():
                    for ts_info in ts_list[:3]:  # Mostra apenas os 3 primeiros
                        line_desc = ts_info.get("line", "")
                        context_part += (
                            f"- {ts_info['start']} → {ts_info['end']}: {line_desc}\n"
                        )

        context_parts.append(context_part)

    context = "\n\n".join(context_parts)

    # Escapa chaves em contexto/histórico/pergunta para evitar erros de str.format
    def _escape_braces(s: str) -> str:
        if not isinstance(s, str):
            return s
        return s.replace("{", "{{").replace("}", "}}")

    # Constrói as mensagens (insere contexto protegido)
    safe_context = _escape_braces(context)
    messages = [("system", system_prompt.replace("{context}", safe_context))]

    # Adiciona o histórico de conversa (se fornecido)
    # O histórico é mantido para preservar o contexto da conversa,
    # mas a cada nova pergunta o RAG busca novos documentos relevantes,
    # garantindo que as informações (incluindo imagens) sejam sempre atualizadas
    if chat_history:
        for message in chat_history:
            role = message.get("role")
            content = message.get("content")
            # Converte role 'user' ou 'ai' para formato do langchain
            if role == "user":
                messages.append(("human", _escape_braces(content)))
            elif role == "ai":
                messages.append(("assistant", _escape_braces(content)))

    # Adiciona a pergunta atual (escapando chaves)
    messages.append(("human", _escape_braces(query)))

    # Cria o prompt e executa
    prompt = ChatPromptTemplate.from_messages(messages)
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({})

    try:
        # Extrai as mídias do contexto (imagens e vídeos)
        context_media = _extract_media_tags(context)

        # Garante que as mídias relevantes estejam na resposta
        response = _ensure_media_in_response(response, context_media)

        # Adiciona timestamps aos vídeos na resposta se disponíveis
        if video_timestamps_map:
            response = _add_timestamps_to_videos(response, video_timestamps_map)

        # Adiciona links do YouTube com timestamps
        if youtube_urls:
            response = _add_youtube_links_to_response(
                response, youtube_urls, video_timestamps_map, query
            )

        # CORREÇÃO INTELIGENTE: Adiciona vídeo SOMENTE se não houver nenhum embed na resposta
        # Isso evita duplicação mas garante que sempre tenha pelo menos um vídeo
        if youtube_urls and "[YOUTUBE_EMBED:" not in response:
            # Pega a primeira URL do YouTube disponível
            first_url = list(youtube_urls.values())[0]

            # Busca o timestamp mais relevante baseado na query do usuário
            best_timestamp = None
            if video_timestamps_map:
                best_timestamp = _find_relevant_timestamp_for_query(
                    query, video_timestamps_map
                )

            # Adiciona o vídeo ao final da resposta
            response += "\n\n---\n\n"

            if best_timestamp:
                start_time = best_timestamp.get("start", "00:00")
                end_time = best_timestamp.get("end", "")

                # Converte para segundos
                time_parts = start_time.split(":")
                if len(time_parts) == 2:
                    seconds = int(time_parts[0]) * 60 + int(time_parts[1])
                elif len(time_parts) == 3:
                    seconds = (
                        int(time_parts[0]) * 3600
                        + int(time_parts[1]) * 60
                        + int(time_parts[2])
                    )
                else:
                    seconds = 0

                # Extrai o ID do vídeo
                video_id = None
                if "youtube.com/watch?v=" in first_url:
                    video_id = first_url.split("watch?v=")[1].split("&")[0]
                elif "youtu.be/" in first_url:
                    video_id = first_url.split("youtu.be/")[1].split("?")[0]

                if video_id:
                    embed_url = (
                        f"https://www.youtube.com/embed/{video_id}?start={seconds}"
                    )

                    if end_time:
                        response += (
                            f"### 🎬 Vídeo Tutorial ({start_time} → {end_time})\n\n"
                        )
                    else:
                        response += (
                            f"### 🎬 Vídeo Tutorial (a partir de {start_time})\n\n"
                        )

                    response += f"[YOUTUBE_EMBED:{embed_url}]\n"
            else:
                # Sem timestamp específico, adiciona vídeo completo
                video_id = None
                if "youtube.com/watch?v=" in first_url:
                    video_id = first_url.split("watch?v=")[1].split("&")[0]
                elif "youtu.be/" in first_url:
                    video_id = first_url.split("youtu.be/")[1].split("?")[0]

                if video_id:
                    embed_url = f"https://www.youtube.com/embed/{video_id}"
                    response += "### 🎬 Vídeo Tutorial Relacionado\n\n"
                    response += f"[YOUTUBE_EMBED:{embed_url}]\n"

    except Exception as e:
        import traceback

        print(f"❌ Erro ao processar mídias: {e}")
        traceback.print_exc()
        # Continua com a resposta sem mídias processadas

    return {"answer": response, "source_documents": docs}


def ask_question_with_sources(
    query: str,
    vector_store: Chroma,
    model_name: str = None,
    chat_history: Optional[List[dict]] = None,
    k: int = 4,
) -> Tuple[str, List[str]]:
    """
    Faz uma pergunta e retorna a resposta junto com as fontes (documentos recuperados)

    Args:
        query: Pergunta do usuário
        vector_store: Vector store com os documentos
        model_name: Nome do modelo OpenAI
        chat_history: Histórico de conversa
        k: Número de documentos a recuperar

    Returns:
        Tupla (resposta, lista_de_fontes)
    """
    # Busca documentos relevantes
    retriever = vector_store.as_retriever(search_kwargs={"k": k})
    docs = retriever.get_relevant_documents(query)

    # Gera a resposta
    result = ask_question(query, vector_store, model_name, chat_history)
    answer = result["answer"]

    # Extrai o conteúdo dos documentos como fontes
    sources = [doc.page_content[:200] + "..." for doc in docs]

    return answer, sources
