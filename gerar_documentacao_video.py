# -*- coding: utf-8 -*-
"""
Gera documentação Markdown estruturada com base na transcrição de um vídeo do YouTube,
usando LangChain (versão 0.2+) e o modelo ChatGPT (OpenAI API).
"""

import os
import re
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from pytubefix import YouTube
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# === CONFIGURAÇÃO ===
load_dotenv()  # carrega OPENAI_API_KEY do .env

# Processar todos os vídeos com as melhorias implementadas
YOUTUBE_URLS = [
    "https://youtu.be/VC6EkQJoLEY?si=k9wjmlsuMeBR7kmV",  # Módulo de Armazenamento
    "https://youtu.be/lefybyzpmgY?si=YfjXcK_ZY3ZoekrC",  # Módulo de Qualidade
    "https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO",  # Módulo de RH
    "https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ",  # Módulo Financeiro
    "https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73",  # Módulo de Suprimentos
    "https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb",  # Módulo de Compras
    "https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_",  # Módulo de Engenharia
]

MODEL_NAME = "gpt-5-nano"  # pode usar gpt-4o ou gpt-3.5-turbo
TEMPERATURE = 0.2
MAX_TOKENS = 16000  # Tokens máximos para respostas detalhadas (aumentado para documentação completa)
DOCS_FOLDER = "docs"  # Pasta onde os documentos serão salvos


# === 1. Carregar transcrição ===
def extrair_video_id(url: str) -> str:
    """Extrai o ID do vídeo de uma URL do YouTube."""
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    raise ValueError(f"Não foi possível extrair o ID do vídeo da URL: {url}")


def obter_titulo_video(url: str) -> str:
    """Obtém o título do vídeo do YouTube."""
    try:
        yt = YouTube(url)
        titulo = yt.title
        # Remove caracteres inválidos para nome de arquivo
        titulo_limpo = re.sub(r'[<>:"/\\|?*]', "", titulo)
        titulo_limpo = titulo_limpo.strip()
        return titulo_limpo
    except Exception as e:
        print(f"⚠️ Erro ao obter título do vídeo: {e}")
        # Usa o ID do vídeo como fallback
        return extrair_video_id(url)


def formatar_tempo(segundos: float) -> str:
    """Converte segundos (float) para string HH:MM:SS ou MM:SS."""
    total = int(round(segundos))
    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60
    if h > 0:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def segmentar_transcricao(transcript_entries, segmento_segundos: int = 150):
    """
    Agrupa entradas da transcrição em segmentos contínuos de ~segmento_segundos.
    Retorna lista de dicts: {'start': float, 'end': float, 'texto': str}
    """
    if not transcript_entries:
        return []

    segmentos = []
    current_start = transcript_entries[0]["start"]
    current_texts = []
    current_end = current_start

    for entry in transcript_entries:
        start = entry.get("start", 0.0)
        duration = entry.get("duration", 0.0)
        end = start + duration

        # Se ultrapassar o limite do segmento, fechar segmento atual e iniciar novo
        if (start - current_start) >= segmento_segundos and current_texts:
            segmentos.append(
                {
                    "start": current_start,
                    "end": current_end,
                    "texto": " ".join(current_texts).strip(),
                }
            )
            current_start = start
            current_texts = []

        current_texts.append(entry.get("text", ""))
        current_end = end

    # Adicionar último segmento
    if current_texts:
        segmentos.append(
            {
                "start": current_start,
                "end": current_end,
                "texto": " ".join(current_texts).strip(),
            }
        )

    return segmentos


def build_timestamped_url(original_url: str, start_seconds: float) -> str:
    """Retorna a URL do YouTube que inicia no tempo fornecido (em segundos)."""
    t = int(round(start_seconds))
    if "youtu.be/" in original_url:
        # youtu.be/ID?param... -> adicionar ?t= ou &t=
        sep = "&" if "?" in original_url else "?"
        return f"{original_url}{sep}t={t}"
    # Para URLs longas (www.youtube.com/watch?v=ID)
    sep = "&" if "?" in original_url else "?"
    return f"{original_url}{sep}t={t}"


def carregar_transcricao(url: str) -> list:
    """
    Carrega a transcrição do YouTube preservando timestamps.
    Retorna lista de dicts com 'text', 'start', 'duration'.
    """
    print("🎥 Carregando e transcrevendo vídeo do YouTube...")

    # Extrai o ID do vídeo
    video_id = extrair_video_id(url)

    # Busca a transcrição usando a API correta
    try:
        # Tenta buscar em português primeiro usando o método fetch
        api = YouTubeTranscriptApi()
        transcript_data = api.fetch(video_id, languages=["pt", "pt-BR"])
        # Converte para lista de dicts
        return [
            {"text": entry.text, "start": entry.start, "duration": entry.duration}
            for entry in transcript_data
        ]
    except Exception as e:
        print(f"Erro ao buscar transcrição em português: {e}")
        print("Tentando buscar em qualquer idioma disponível...")
        try:
            # Tenta qualquer idioma disponível
            api = YouTubeTranscriptApi()
            transcript_data = api.fetch(video_id)
            # Converte para lista de dicts
            return [
                {"text": entry.text, "start": entry.start, "duration": entry.duration}
                for entry in transcript_data
            ]
        except Exception as e_final:
            print(f"❌ Erro fatal ao buscar transcrição: {e_final}")
            raise


# === 2. Gerar documentação Markdown ===
def gerar_documentacao(segmentos: list, video_url: str, titulo_video: str) -> str:
    """
    Gera documentação estruturada por segmentos temporais.
    Cada segmento vira uma seção detalhada com minutagem e link timestamped.
    """
    print(
        f"🧠 Gerando documentação estruturada e detalhada por seção (total: {len(segmentos)} segmentos)..."
    )

    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )
    parser = StrOutputParser()

    # Prompt por seção individual (OTIMIZADO PARA RAG V2.0)
    prompt = PromptTemplate(
        input_variables=[
            "transcricao_segmento",
            "minutagem",
            "jump_url",
            "section_index",
            "total_sections",
            "duracao_segundos",
        ],
        template="""
Você é um analista técnico especializado em criar documentação EXTREMAMENTE DETALHADA de sistemas a partir de vídeos tutoriais.

Esta documentação será usada em um sistema RAG (Retrieval-Augmented Generation), portanto precisa ser:
- MUITO DETALHADA e GRANULAR
- Cada seção deve ser AUTOCONTIDA e COMPLETA
- Rico em detalhes específicos, nomes de campos, botões, menus, etc.
- Otimizada para busca semântica e recuperação de informações
- **NOVO:** Incluir troubleshooting, variações linguísticas e exemplos práticos
- **NOVO:** Estabelecer relações com outras funcionalidades

**Transcrição deste segmento:**
---
{transcricao_segmento}
---

**INSTRUÇÕES CRÍTICAS:**

Gere UMA seção seguindo a estrutura exata abaixo. NÃO RESUMA - Inclua TODOS os detalhes mencionados na transcrição deste segmento.

INICIE A RESPOSTA EXATAMENTE COM AS LINHAS ABAIXO (copie exatamente como está):

---

## {section_index}. [Título Específico da Funcionalidade]

**📋 METADADOS:**
- **ID:** sec_{section_index}
- **⏱️ Minutagem:** {minutagem}
- **⏲️ Duração:** {duracao_segundos}s
- **🎬 Link:** [Assistir este trecho]({jump_url})
- **📦 Módulo:** [Nome do Módulo mencionado na transcrição]
- **🏷️ Categorias:** [Liste 2-4 categorias relevantes separadas por vírgula]
- **🔑 Palavras-chave:** [Liste 5-8 palavras-chave importantes separadas por vírgula]

> **🔍 RESUMO EXECUTIVO:** [Escreva um resumo de 2-3 linhas explicando o que esta seção ensina e qual problema ela resolve]

**Contexto:**
[Explique brevemente onde estamos no sistema e o objetivo desta seção]

**Localização no Sistema:**
- Caminho de navegação completo (ex: Menu Principal > Módulo X > Submenu Y)
- Tela/interface específica

**Funcionalidade Detalhada:**

[Descreva em DETALHES o que esta funcionalidade faz, para que serve, quando usar]

### 🔹 Passo a Passo Detalhado:

1. **[Ação Específica]**
   - Localização: [Onde exatamente está o elemento]
   - Como fazer: [Descrição detalhada]
   - Campos/Opções disponíveis:
     * `Campo 1`: [descrição e tipo]
     * `Campo 2`: [descrição e tipo]
   - Resultado esperado: [O que acontece]

2. **[Próxima Ação]**
   - Localização: [Onde exatamente está o elemento]
   - Como fazer: [Descrição detalhada]
   - Observações importantes: [Validações, restrições, dicas]
   - Resultado esperado: [O que acontece]

[Continue para cada ação mostrada neste segmento]

**Campos e Parâmetros:**

| Campo | Tipo | Obrigatório | Descrição | Exemplo |
|-------|------|-------------|-----------|---------|
| [Nome] | [Tipo] | [Sim/Não] | [Descrição completa] | [Exemplo de valor] |

**Regras de Negócio:**
- [Liste TODAS as regras, validações e restrições mencionadas]
- [Comportamentos especiais]
- [Casos de uso específicos]

**Observações Importantes:**
- [Dicas mencionadas no vídeo]
- [Erros comuns a evitar]
- [Requisitos ou dependências]

**Conceitos-Chave:**
- **[Termo Técnico]**: [Definição clara]
- **[Outro Termo]**: [Definição clara]

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema | Causa Provável | Solução | Prevenção |
|----------|---------------|---------|-----------|
| [Erro comum mencionado ou inferível] | [Por que acontece] | [Como resolver passo a passo] | [Como evitar] |
| [Ex: Botão desabilitado] | [Ex: Sem permissão] | [Ex: Verificar em Admin > Usuários] | [Ex: Configurar permissões primeiro] |

**💡 DICAS E BOAS PRÁTICAS:**
- [Dica importante mencionada no vídeo]
- [Atalho ou forma mais eficiente]
- [Erro comum a evitar]
- [Recomendação de uso]

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: [Caso de Uso Comum]**
```
Situação: [Contexto realista]
Ação: [Passo a passo com valores concretos]
  • Campo X: "Valor de Exemplo Real"
  • Campo Y: "Outro Exemplo"
Resultado: [O que acontece]
```

**Exemplo 2: [Outro Caso de Uso]**
```
Situação: [Contexto diferente]
Ação: [Passo a passo com valores concretos]
Resultado: [O que acontece]
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** [O que precisa estar configurado/feito antes]
- **Habilita:** [Quais funcionalidades esta ação permite usar depois]
- **Relacionado a:** [Outras funcionalidades ou módulos conectados]

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "[Como fazer X?]"
- **Com problema:** "[Não consigo fazer X, o que fazer?]"
- **Informal:** "[Versão coloquial da pergunta]"
- **Por sintoma:** "[Quando acontece Y, como resolver?]"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- [Lista de sinônimos e variações: ex: "criar pasta", "adicionar pasta", "nova pasta", "cadastrar pasta"]
- [Termos técnicos equivalentes]
- [Termos coloquiais que usuários podem usar]

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- [Pergunta 1 que um usuário faria sobre este tópico?]
- [Pergunta 2 que um usuário faria sobre este tópico?]
- [Pergunta 3 que um usuário faria sobre este tópico?]
- [Pergunta 4 sobre troubleshooting: "O que fazer se/quando...?"]
- [Pergunta 5 sobre pré-requisitos: "O que preciso ter/fazer antes?"]

---

**NÍVEL DE DETALHE:**
- Mencione TODOS os nomes de botões, menus, campos exatamente como aparecem
- Inclua TODAS as opções de cada dropdown/lista
- Descreva TODOS os passos, mesmo os óbvios
- Transcreva valores de exemplo mencionados
- Explique o PORQUÊ de cada ação quando mencionado
- **NOVO:** Antecipe problemas comuns e forneça soluções
- **NOVO:** Use exemplos CONCRETOS com valores reais (não genéricos)
- **NOVO:** Liste todas as formas que usuário pode buscar esta informação

**FORMATO:**
- Markdown limpo e bem formatado
- Use tabelas para organizar informações estruturadas
- Use listas com marcadores para enumerações
- Use negrito para destacar elementos importantes da UI
- Use código inline com crases para nomes técnicos de campos
- Use emojis consistentemente para identificação visual rápida

**IMPORTANTE PARA METADADOS:**
- Categorias: Use termos como "Configuração", "Cadastro", "Relatório", "Administração", "Operacional", etc.
- Palavras-chave: Use substantivos e verbos importantes mencionados (ex: "permissão", "usuário", "editar", "visualizar", "pasta")
- Perguntas: Formule perguntas naturais que um usuário faria ao buscar essa informação, incluindo variações linguísticas

**IMPORTANTE PARA TROUBLESHOOTING:**
- Liste erros que PODEM acontecer (mesmo se não explícitos no vídeo)
- Para cada erro, forneça causa, solução E prevenção
- Inclua validações e restrições como possíveis problemas

**IMPORTANTE PARA EXEMPLOS:**
- NÃO use "exemplo", "teste", "xxx" como valores
- USE valores realistas: "Contratos_2024", "João Silva", "Departamento_RH"
- Mostre pelo menos 2 exemplos de casos de uso diferentes

**IMPORTANTE PARA VARIAÇÕES:**
- Liste pelo menos 5 formas diferentes de perguntar sobre este tópico
- Inclua versão formal, informal, com problema, por sintoma
- Liste todos os sinônimos e termos alternativos

NÃO invente informações técnicas. Use APENAS o que está na transcrição para funcionalidades.
MAS PODE inferir problemas comuns, exemplos realistas e variações de busca baseado no contexto.
Seja EXAUSTIVAMENTE detalhado - melhor pecar pelo excesso do que pela falta.
""",
    )

    # Cabeçalho do documento
    documentacao_completa = [f"# 📚 Documentação: {titulo_video}\n\n"]
    documentacao_completa.append(f"[video:{video_url}]\n\n")
    documentacao_completa.append(f"**🎥 Vídeo Original:** {video_url}\n")
    documentacao_completa.append(f"**📊 Total de Seções:** {len(segmentos)}\n")
    documentacao_completa.append("---\n")

    # Gera cada seção
    chain = prompt | llm | parser
    total = len(segmentos)

    for i, seg in enumerate(segmentos, start=1):
        minutagem = f"{formatar_tempo(seg['start'])} → {formatar_tempo(seg['end'])}"
        jump_url = build_timestamped_url(video_url, seg["start"])
        duracao_segundos = int(seg["end"] - seg["start"])

        print(f"   📝 Gerando seção {i}/{total} ({minutagem})...")

        try:
            secao_md = chain.invoke(
                {
                    "transcricao_segmento": seg["texto"],
                    "minutagem": minutagem,
                    "jump_url": jump_url,
                    "section_index": str(i),
                    "total_sections": str(total),
                    "duracao_segundos": str(duracao_segundos),
                }
            )
            documentacao_completa.append(secao_md.strip())
            documentacao_completa.append("\n\n---\n\n")
        except Exception as e:
            print(f"   ⚠️ Erro ao gerar seção {i}: {e}")
            documentacao_completa.append(f"<!-- Erro ao gerar seção {i}: {e} -->\n\n")

    # ADICIONA SEÇÃO DE TIMESTAMPS ESTRUTURADOS PARA O RAG
    print("\n📝 Adicionando timestamps estruturados para otimização RAG...")
    documentacao_completa.append("\n\n---\n\n")
    documentacao_completa.append("## 🎬 DADOS DE TIMESTAMPS (Para Sistema RAG)\n\n")
    documentacao_completa.append("[VIDEO_TIMESTAMPS_DATA]\n")

    import json

    timestamps_dict = {titulo_video: []}
    for i, seg in enumerate(segmentos, 1):
        timestamps_dict[titulo_video].append(
            {
                "start": formatar_tempo(seg["start"]),
                "end": formatar_tempo(seg["end"]),
                "line": seg["texto"][:100],  # Primeiros 100 caracteres como preview
            }
        )

    documentacao_completa.append(
        json.dumps(timestamps_dict, ensure_ascii=False, indent=2)
    )
    documentacao_completa.append("\n[/VIDEO_TIMESTAMPS_DATA]\n")
    print("✅ Timestamps estruturados adicionados!")

    return "\n".join(documentacao_completa)


# === 3. Gravar arquivo Markdown ===
def salvar_markdown(conteudo: str, titulo_video: str):
    # Cria a pasta docs se não existir
    if not os.path.exists(DOCS_FOLDER):
        os.makedirs(DOCS_FOLDER)
        print(f"📁 Pasta '{DOCS_FOLDER}' criada.")

    # Define o nome do arquivo
    nome_arquivo = f"{titulo_video}_documentacao_gerada.md"
    caminho_completo = os.path.join(DOCS_FOLDER, nome_arquivo)

    # Salva o arquivo
    with open(caminho_completo, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print(f"✅ Documentação salva em: {caminho_completo}")


# === 4. Execução principal ===
if __name__ == "__main__":
    print(f"🚀 Iniciando processamento de {len(YOUTUBE_URLS)} vídeo(s)...\n")

    for index, url in enumerate(YOUTUBE_URLS, 1):
        print(f"\n{'='*60}")
        print(f"📹 Vídeo {index}/{len(YOUTUBE_URLS)}")
        print(f"{'='*60}")

        try:
            # Obtém o título do vídeo
            print("📝 Obtendo título do vídeo...")
            titulo = obter_titulo_video(url)
            print(f"📌 Título: {titulo}")

            # Carrega a transcrição com timestamps
            transcricao_entries = carregar_transcricao(url)
            print(f"✅ Transcrição carregada: {len(transcricao_entries)} entradas")

            # Segmenta a transcrição (padrão: 150 segundos = 2min30s por segmento)
            print("📊 Segmentando transcrição...")
            segmentos = segmentar_transcricao(
                transcricao_entries, segmento_segundos=150
            )
            print(f"✅ {len(segmentos)} segmentos criados")

            # Gera a documentação
            markdown = gerar_documentacao(segmentos, url, titulo)

            # Salva o arquivo
            salvar_markdown(markdown, titulo)

            print(f"✅ Vídeo {index} processado com sucesso!")

        except Exception as e:
            print(f"❌ Erro ao processar vídeo {index}: {e}")
            import traceback

            traceback.print_exc()
            continue

    print(f"\n{'='*60}")
    print("🎉 Processo concluído!")
    print(f"📂 Documentos salvos na pasta: {DOCS_FOLDER}/")
    print(f"{'='*60}")
