"""
Módulo responsável pelo processamento de arquivos (PDF, TXT, Markdown)
"""

import os
import re
import tempfile
from typing import List

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from .config import Config
from .metadata_enhancer import enhance_document_metadata

# Importar tiktoken para contar tokens com precisão
try:
    import tiktoken
    TIKTOKEN_AVAILABLE = True
except ImportError:
    TIKTOKEN_AVAILABLE = False
    print("⚠️ tiktoken não disponível. Usando estimativa aproximada de tokens.")


def count_tokens(text: str, model: str = "gpt-4o-mini") -> int:
    """
    Conta o número de tokens em um texto usando tiktoken.
    Se tiktoken não estiver disponível, usa estimativa (1 token ≈ 4 caracteres).
    
    Args:
        text: Texto para contar tokens
        model: Nome do modelo (para usar o encoding correto)
    
    Returns:
        Número estimado de tokens
    """
    if TIKTOKEN_AVAILABLE:
        try:
            encoding = tiktoken.encoding_for_model(model)
            return len(encoding.encode(text))
        except Exception:
            # Fallback para estimativa se houver erro
            pass
    
    # Estimativa: ~4 caracteres por token (regra geral)
    return len(text) // 4


def split_large_content(content: str, max_tokens: int = 250000) -> List[str]:
    """
    Divide um conteúdo grande em partes menores baseado no limite de tokens.
    Tenta dividir em pontos naturais (seções markdown).
    
    Args:
        content: Conteúdo a ser dividido
        max_tokens: Máximo de tokens por parte (deixa margem de segurança)
    
    Returns:
        Lista de strings, cada uma com menos de max_tokens
    """
    token_count = count_tokens(content)
    
    # Se o conteúdo está dentro do limite, retorna como está
    if token_count <= max_tokens:
        return [content]
    
    print(f"⚠️ Documento muito grande ({token_count:,} tokens). Dividindo em partes menores...")
    
    # Tenta dividir por seções principais (## )
    sections = re.split(r'\n(?=## )', content)
    
    parts = []
    current_part = ""
    current_tokens = 0
    
    for section in sections:
        section_tokens = count_tokens(section)
        
        # Se uma única seção é maior que o limite, divide ela também
        if section_tokens > max_tokens:
            # Se já temos algo no current_part, salva primeiro
            if current_part:
                parts.append(current_part)
                current_part = ""
                current_tokens = 0
            
            # Divide a seção em subseções menores
            subsections = re.split(r'\n(?=### )', section)
            for subsection in subsections:
                subsection_tokens = count_tokens(subsection)
                
                if current_tokens + subsection_tokens > max_tokens:
                    if current_part:
                        parts.append(current_part)
                    current_part = subsection
                    current_tokens = subsection_tokens
                else:
                    current_part += "\n" + subsection
                    current_tokens += subsection_tokens
        else:
            # Se adicionar esta seção ultrapassar o limite, salva a parte atual
            if current_tokens + section_tokens > max_tokens:
                if current_part:
                    parts.append(current_part)
                current_part = section
                current_tokens = section_tokens
            else:
                current_part += "\n" + section
                current_tokens += section_tokens
    
    # Adiciona a última parte
    if current_part:
        parts.append(current_part)
    
    print(f"✅ Documento dividido em {len(parts)} partes")
    for i, part in enumerate(parts, 1):
        part_tokens = count_tokens(part)
        print(f"   Parte {i}: {part_tokens:,} tokens")
    
    return parts


def process_pdf_file(file_like) -> List[Document]:
    """
    Processa um arquivo PDF e retorna chunks de documentos

    Args:
        file_like: Objeto file-like (ex: st.uploaded_file) que possui método .read()

    Returns:
        Lista de documentos (chunks) processados
    """
    # Cria arquivo temporário para salvar o PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file_like.read())
        tmp_path = tmp.name

    try:
        # Carrega o PDF
        loader = PyPDFLoader(tmp_path)
        docs = loader.load()

        # Divide em chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE, chunk_overlap=Config.CHUNK_OVERLAP
        )
        chunks = text_splitter.split_documents(documents=docs)

        return chunks

    finally:
        # Remove o arquivo temporário
        if os.path.exists(tmp_path):
            os.remove(tmp_path)


def process_txt_file(file_like) -> List[Document]:
    """
    Processa um arquivo TXT e retorna chunks de documentos

    Args:
        file_like: Objeto file-like (ex: st.uploaded_file) que possui método .read()

    Returns:
        Lista de documentos (chunks) processados
    """
    # Lê o conteúdo do arquivo
    content = file_like.read()
    if isinstance(content, bytes):
        content = content.decode("utf-8")

    # Cria um documento único
    doc = Document(
        page_content=content, metadata={"source": file_like.name, "type": "txt"}
    )

    # Divide em chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=Config.CHUNK_SIZE,
        chunk_overlap=Config.CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    chunks = text_splitter.split_documents([doc])
    return chunks


def process_markdown_file(file_like) -> List[Document]:
    """
    Processa um arquivo Markdown mantendo estrutura, extrai imagens/vídeos e retorna chunks.
    Também extrai timestamps de vídeos quando disponíveis.
    Implementa divisão automática de documentos grandes para evitar erro de limite de tokens.

    Args:
        file_like: Objeto file-like (ex: st.uploaded_file) que possui método .read()

    Returns:
        Lista de documentos (chunks) processados com metadados enriquecidos
    """
    # Lê o conteúdo do arquivo
    content = file_like.read()
    if isinstance(content, bytes):
        content = content.decode("utf-8")
    
    # Verifica o tamanho do documento
    token_count = count_tokens(content)
    print(f"📊 Documento: {file_like.name} - {token_count:,} tokens")
    
    # Se o documento for muito grande (>250k tokens), divide em partes
    if token_count > 250000:
        print("⚠️ Documento muito grande! Processando em partes separadas...")
        content_parts = split_large_content(content, max_tokens=250000)
        
        # Processa cada parte separadamente e combina os chunks
        all_chunks = []
        for i, part_content in enumerate(content_parts, 1):
            print(f"   Processando parte {i}/{len(content_parts)}...")
            part_chunks = _process_markdown_content(part_content, file_like.name, part_index=i)
            all_chunks.extend(part_chunks)
        
        print(f"✅ Total de {len(all_chunks)} chunks gerados")
        return all_chunks
    else:
        # Documento de tamanho normal, processa diretamente
        return _process_markdown_content(content, file_like.name)


def _process_markdown_content(content: str, filename: str, part_index: int = None) -> List[Document]:
    """
    Função auxiliar que processa o conteúdo markdown.
    Extraída para permitir processamento em partes.
    
    Args:
        content: Conteúdo markdown
        filename: Nome do arquivo original
        part_index: Índice da parte (se documento foi dividido)
    
    Returns:
        Lista de documentos (chunks) processados
    """

    # Extrai o link do vídeo do YouTube se presente
    youtube_url = None
    youtube_match = re.search(
        r"\*\*🎥 Vídeo Original:\*\*\s+(https://youtu\.be/[^\s]+)", content
    )
    if youtube_match:
        youtube_url = youtube_match.group(1)

    # Regex para encontrar imagens no formato ![alt-text](./images/filename.png "title")
    img_regex = r"!\[([^\]]*)\]\(./images/([^\"]+\.(?:png|jpg|jpeg|gif|webp))(?:\s+\"([^\"]*)\")?\)"

    # Regex para encontrar vídeos no formato ![alt-text](./videos/filename.mp4 "title")
    # Captura o nome completo do arquivo até .mp4, mesmo com parênteses no nome
    video_regex = r"!\[([^\]]*)\]\(./videos/([^\"]+\.mp4)(?:\s+\"([^\"]*)\")?\)"

    # Regex para encontrar timestamps no formato: ### Tópico X — `00:00 → 00:11`
    # ou — `00:00 → 00:11` ou - **Início:** `00:00` e - **Fim:** `00:11`
    # Aceita: → (unicode), -> (ascii), - (hífen), — (em dash)
    timestamp_range_regex = r"[—-]\s*`?(\d{1,2}:\d{2}(?::\d{2})?)\s*(?:→|->|—)\s*(\d{1,2}:\d{2}(?::\d{2})?)`?"
    timestamp_start_regex = r"[Ii]nício:\*?\*?\s*`?(\d{1,2}:\d{2}(?::\d{2})?)`?"
    timestamp_end_regex = r"[Ff]im:\*?\*?\s*`?(\d{1,2}:\d{2}(?::\d{2})?)`?"

    # Encontra todas as imagens e vídeos
    images_found = re.findall(img_regex, content)
    videos_found = re.findall(video_regex, content)

    # NOVA ESTRATÉGIA: Extrai timestamps de TODO o arquivo ANTES do chunking
    # Cria um mapa de vídeo → lista de timestamps encontrados no documento
    video_timestamps_map = {}

    # PRIMEIRO: Tenta extrair do formato JSON estruturado [VIDEO_TIMESTAMPS_DATA]
    import json

    json_match = re.search(
        r"\[VIDEO_TIMESTAMPS_DATA\]\s*\n(.*?)\n\[/VIDEO_TIMESTAMPS_DATA\]",
        content,
        re.DOTALL,
    )
    if json_match:
        try:
            timestamps_json = json_match.group(1)
            video_timestamps_map = json.loads(timestamps_json)
        except json.JSONDecodeError as e:
            print(f"⚠️ Erro ao parsear JSON de timestamps: {e}")
            video_timestamps_map = {}

    # FALLBACK: Se não encontrou JSON, usa o método antigo de regex
    if not video_timestamps_map:
        for video_name in (video[1] for video in videos_found):
            video_timestamps_map[video_name] = []

            # Procura por seções de timestamps relacionadas a este vídeo
            # Padrão: procura por títulos seguidos de timestamps
            # Ex: "#### Tópico 1: Introdução — `00:00 → 00:11`"

            # Busca todas as linhas com timestamps
            lines = content.split("\n")
            for i, line in enumerate(lines):
                # Verifica se a linha tem timestamp no formato range
                range_match = re.search(timestamp_range_regex, line)
                if range_match:
                    timestamp_start = range_match.group(1)
                    timestamp_end = range_match.group(2)
                    video_timestamps_map[video_name].append(
                        {
                            "start": timestamp_start,
                            "end": timestamp_end,
                            "line": line.strip(),
                        }
                    )
                else:
                    # Verifica formato separado (Início/Fim) nas próximas linhas
                    if "início" in line.lower():
                        start_match = re.search(timestamp_start_regex, line)
                        if start_match and i + 1 < len(lines):
                            # Procura pelo Fim na linha seguinte ou próximas
                            for j in range(i + 1, min(i + 5, len(lines))):
                                end_match = re.search(timestamp_end_regex, lines[j])
                                if end_match:
                                    timestamp_start = start_match.group(1)
                                    timestamp_end = end_match.group(1)
                                    video_timestamps_map[video_name].append(
                                        {
                                            "start": timestamp_start,
                                            "end": timestamp_end,
                                            "line": line.strip(),
                                        }
                                    )
                                    break
                        # Procura pelo Fim na linha seguinte ou próximas
                        for j in range(i + 1, min(i + 5, len(lines))):
                            end_match = re.search(timestamp_end_regex, lines[j])
                            if end_match:
                                timestamp_start = start_match.group(1)
                                timestamp_end = end_match.group(1)
                                video_timestamps_map[video_name].append(
                                    {
                                        "start": timestamp_start,
                                        "end": timestamp_end,
                                        "line": line.strip(),
                                    }
                                )
                                break

    # Substitui as sintaxes por tags que o frontend entende
    content_processed = re.sub(img_regex, r"[image: \2]", content)
    content_processed = re.sub(video_regex, r"[video: \2]", content_processed)

    # Divide o conteúdo em chunks primeiro
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=Config.CHUNK_SIZE,
        chunk_overlap=Config.CHUNK_OVERLAP,
        separators=["\n## ", "\n### ", "\n#### ", "\n\n", "\n", ". ", " ", ""],
    )
    text_chunks = text_splitter.split_text(content_processed)

    # Cria um Document para cada chunk e associa os metadados corretos
    chunks = []
    for text_chunk in text_chunks:
        # Cria o metadata base com o nome do arquivo
        metadata = {"source": filename, "type": "markdown"}
        
        # Se é uma parte de documento grande, adiciona o índice da parte
        if part_index is not None:
            metadata["part"] = part_index
        
        doc = Document(
            page_content=text_chunk,
            metadata=metadata
        )
        chunks.append(doc)

    # Para cada chunk, verifica se ele contém tags de imagem/vídeo e adiciona os
    # nomes dos arquivos correspondentes aos seus metadados.
    # Também extrai timestamps quando disponíveis.
    for chunk in chunks:
        # Enriquece metadados automaticamente
        chunk = enhance_document_metadata(chunk)

        # Adiciona link do YouTube ao metadata se disponível
        if youtube_url:
            chunk.metadata["youtube_url"] = youtube_url

        chunk_images = []
        chunk_videos = []
        chunk_video_timestamps = {}

        # Procura por imagens
        for img_name in (img[1] for img in images_found):
            if f"[image: {img_name}]" in chunk.page_content:
                chunk_images.append(img_name)

        # Procura por vídeos
        for video_name in (video[1] for video in videos_found):
            if f"[video: {video_name}]" in chunk.page_content:
                chunk_videos.append(video_name)

                # Usa o mapa global de timestamps que foi extraído ANTES do chunking
                if (
                    video_name in video_timestamps_map
                    and video_timestamps_map[video_name]
                ):
                    # Armazena TODOS os timestamps encontrados para este vídeo
                    chunk_video_timestamps[video_name] = video_timestamps_map[
                        video_name
                    ]

        # NOVA LÓGICA: Se o documento tem timestamps JSON (mas não tem tags [video:]),
        # adiciona os timestamps a TODOS os chunks desse documento
        if video_timestamps_map and not chunk_video_timestamps:
            # Copia todos os timestamps para este chunk
            chunk_video_timestamps = video_timestamps_map.copy()

        # Adiciona os metadados ao chunk
        if chunk_images:
            chunk.metadata["images"] = ", ".join(chunk_images)

        if chunk_videos:
            chunk.metadata["videos"] = ", ".join(chunk_videos)

        chunk.metadata["images"] = ",".join(chunk_images)
        chunk.metadata["videos"] = ",".join(chunk_videos)

        # Adiciona timestamps aos metadados como string JSON
        # IMPORTANTE: Em vez de armazenar no metadata (que tem limite de tamanho no ChromaDB),
        # vamos adicionar ao conteúdo do chunk em um formato especial que pode ser extraído depois
        if chunk_video_timestamps:
            import json

            # Adiciona ao conteúdo em formato que pode ser recuperado
            timestamps_section = "\n\n[VIDEO_TIMESTAMPS_DATA]\n"
            timestamps_section += json.dumps(chunk_video_timestamps, ensure_ascii=False)
            timestamps_section += "\n[/VIDEO_TIMESTAMPS_DATA]\n"
            chunk.page_content += timestamps_section

            # Também adiciona uma flag simples no metadata para identificar chunks com timestamps
            chunk.metadata["has_timestamps"] = "true"

    return chunks


def process_multiple_files(files) -> List[Document]:
    """
    Processa múltiplos arquivos (PDF, TXT, Markdown)

    Args:
        files: Lista de objetos file-like

    Returns:
        Lista combinada de todos os chunks processados
    """
    all_chunks = []

    for file in files:
        # Detecta a extensão do arquivo
        file_extension = file.name.split(".")[-1].lower()

        try:
            if file_extension == "pdf":
                chunks = process_pdf_file(file)
            elif file_extension == "txt":
                chunks = process_txt_file(file)
            elif file_extension in ["md", "markdown"]:
                chunks = process_markdown_file(file)
            else:
                # Ignora arquivos não suportados
                print(f"⚠️ Tipo de arquivo não suportado: {file.name}")
                continue

            all_chunks.extend(chunks)

        except Exception as e:
            print(f"❌ Erro ao processar {file.name}: {str(e)}")
            continue

    return all_chunks


def process_multiple_pdfs(files) -> List[Document]:
    """
    DEPRECATED: Use process_multiple_files() ao invés desta função.
    Mantida para compatibilidade com código existente.

    Processa múltiplos arquivos PDF

    Args:
        files: Lista de objetos file-like

    Returns:
        Lista combinada de todos os chunks processados
    """
    return process_multiple_files(files)


def get_document_stats(chunks: List[Document]) -> dict:
    """
    Retorna estatísticas sobre os documentos processados

    Args:
        chunks: Lista de documentos

    Returns:
        Dicionário com estatísticas
    """
    total_chars = sum(len(doc.page_content) for doc in chunks)

    return {
        "total_chunks": len(chunks),
        "total_characters": total_chars,
        "avg_chunk_size": total_chars // len(chunks) if chunks else 0,
    }
