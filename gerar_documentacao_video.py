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

YOUTUBE_URLS = [
    "https://youtu.be/VC6EkQJoLEY?si=k9wjmlsuMeBR7kmV",
    "https://youtu.be/lefybyzpmgY?si=YfjXcK_ZY3ZoekrC",
    "https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO",
    "https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ",
    "https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73",
    "https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb",
    # Adicione mais URLs aqui
]
MODEL_NAME = "gpt-4o-mini"  # pode usar gpt-4o ou gpt-3.5-turbo
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


def carregar_transcricao(url: str) -> str:
    print("🎥 Carregando e transcrevendo vídeo do YouTube...")

    # Extrai o ID do vídeo
    video_id = extrair_video_id(url)

    # Busca a transcrição em português
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=["pt", "pt-BR"])
    except Exception as e:
        print(f"Erro ao buscar transcrição em português: {e}")
        print("Tentando buscar em qualquer idioma disponível...")
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)

    # Concatena o texto da transcrição
    texto_completo = " ".join([entry.text for entry in transcript])

    return texto_completo


# === 2. Gerar documentação Markdown ===
def gerar_documentacao(transcricao: str) -> str:
    print("🧠 Gerando documentação estruturada e detalhada...")

    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,  # Permite respostas mais longas e detalhadas
    )
    parser = StrOutputParser()

    prompt = PromptTemplate(
        input_variables=["transcricao"],
        template="""
Você é um analista técnico especializado em criar documentação EXTREMAMENTE DETALHADA de sistemas a partir de vídeos tutoriais.

Esta documentação será usada em um sistema RAG (Retrieval-Augmented Generation), portanto precisa ser:
- MUITO DETALHADA e GRANULAR
- Dividida em PEQUENAS SEÇÕES (representando 2-3 minutos de vídeo cada)
- Cada seção deve ser AUTOCONTIDA e COMPLETA
- Rico em detalhes específicos, nomes de campos, botões, menus, etc.

Abaixo está a **transcrição completa de um vídeo**:
---
{transcricao}
---

**INSTRUÇÕES CRÍTICAS:**

1. **DIVIDA o conteúdo em MUITAS seções pequenas** (cada uma representando 2-3 minutos do vídeo)
2. **NÃO RESUMA** - Inclua TODOS os detalhes mencionados na transcrição
3. **Para cada ação**, descreva:
   - O que fazer exatamente
   - Onde clicar (nome exato do botão/menu)
   - O que acontece após a ação
   - Campos a preencher e seus valores
   - Validações e regras de negócio mencionadas

**ESTRUTURA OBRIGATÓRIA para cada seção:**

---

## [Número]. [Título Específico da Funcionalidade]

**Minutagem:** [XX:XX → XX:XX]

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

[Continue para cada ação mostrada nos 2-3 minutos]

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

---

**QUANTIDADE DE SEÇÕES:**
- Para um vídeo de 50 minutos, crie PELO MENOS 20-25 seções
- Para um vídeo de 30 minutos, crie PELO MENOS 12-15 seções
- Para um vídeo de 15 minutos, crie PELO MENOS 6-8 seções

**NÍVEL DE DETALHE:**
- Mencione TODOS os nomes de botões, menus, campos exatamente como aparecem
- Inclua TODAS as opções de cada dropdown/lista
- Descreva TODOS os passos, mesmo os óbvios
- Transcreva valores de exemplo mencionados
- Explique o PORQUÊ de cada ação quando mencionado

**FORMATO DA SAÍDA:**
- Markdown limpo e bem formatado
- Use tabelas para organizar informações estruturadas
- Use listas com marcadores para enumerações
- Use negrito para destacar elementos importantes da UI
- Use código inline com crases para nomes técnicos de campos

NÃO invente informações. Use APENAS o que está na transcrição, mas inclua TUDO que está lá.
Seja EXAUSTIVAMENTE detalhado - melhor pecar pelo excesso do que pela falta.
""",
    )

    chain = prompt | llm | parser
    resultado = chain.invoke({"transcricao": transcricao})
    return resultado.strip()


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

            # Carrega a transcrição
            transcricao = carregar_transcricao(url)

            # Gera a documentação
            markdown = gerar_documentacao(transcricao)

            # Salva o arquivo
            salvar_markdown(markdown, titulo)

            print(f"✅ Vídeo {index} processado com sucesso!")

        except Exception as e:
            print(f"❌ Erro ao processar vídeo {index}: {e}")
            continue

    print(f"\n{'='*60}")
    print("🎉 Processo concluído!")
    print(f"📂 Documentos salvos na pasta: {DOCS_FOLDER}/")
    print(f"{'='*60}")
