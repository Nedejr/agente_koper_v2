# 📚 Guia Completo - Documentação Técnica do Sistema

Documentação técnica detalhada de todas as funções e módulos do Assistente Koper.

---

## 📋 Índice

- [backend/config.py](#backendconfigpy)
- [backend/vector_store.py](#backendvector_storepy)
- [backend/processing.py](#backendprocessingpy)
- [backend/metadata_enhancer.py](#backendmetadata_enhancerpy)
- [backend/hybrid_retriever.py](#backendhybrid_retrieverpy)
- [backend/improved_prompts.py](#backendimproved_promptspy)
- [backend/qa.py](#backendqapy)
- [frontend/main.py](#frontendmainpy)
- [gerar_documentacao_video.py](#gerar_documentacao_videopy)

---

## backend/config.py

### Descrição

Arquivo de configuração central com todas as constantes e parâmetros do sistema.

### Variáveis

#### Modelo OpenAI

```python
DEFAULT_MODEL = "gpt-4o-mini"
```

- **O que faz**: Define o modelo GPT padrão para geração de respostas
- **Valores possíveis**: `"gpt-4o-mini"`, `"gpt-4"`, `"gpt-3.5-turbo"`
- **Custo**: gpt-4o-mini é mais barato e rápido

#### Temperatura

```python
TEMPERATURE = 0.3
```

- **O que faz**: Controla a criatividade das respostas
- **Range**: 0.0 (determinístico) a 2.0 (muito criativo)
- **Recomendado**: 0.3 para documentação técnica (baixa criatividade, alta precisão)

#### Modelo de Embeddings

```python
EMBEDDING_MODEL = "text-embedding-3-small"
```

- **O que faz**: Define o modelo para gerar vetores de documentos
- **Dimensões**: 1536 dimensões
- **Custo**: $0.02 por 1M tokens

#### Chunking

```python
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200
```

- **CHUNK_SIZE**: Tamanho de cada pedaço de documento em caracteres
- **CHUNK_OVERLAP**: Sobreposição entre chunks para manter contexto
- **Por que 1200?**: Balance entre contexto e precisão (muito grande = perda de relevância, muito pequeno = perda de contexto)

#### Retrieval

```python
K_DOCUMENTS = 6
LAMBDA_MULT = 0.7
```

- **K_DOCUMENTS**: Quantos documentos recuperar para compor o contexto
- **LAMBDA_MULT**: Balance no MMR (0 = máxima diversidade, 1 = máxima relevância)

#### ChromaDB

```python
CHROMA_PERSIST_DIR = "./db"
COLLECTION_NAME = "koper_docs"
```

- **CHROMA_PERSIST_DIR**: Pasta onde o banco vetorial é salvo
- **COLLECTION_NAME**: Nome da coleção no ChromaDB

---

## backend/vector_store.py

### Descrição

Gerencia o ChromaDB (banco de dados vetorial) onde os documentos são armazenados.

### Funções

#### `create_vector_store(documents: List[Document]) -> Chroma`

**O que faz**: Cria ou atualiza o vector store com novos documentos

**Parâmetros**:

- `documents`: Lista de objetos `Document` do LangChain

**Retorna**: Objeto `Chroma` (vector store)

**Como funciona**:

1. Cria embeddings model (OpenAI)
2. Verifica se o diretório `./db` existe
3. Se existir: carrega o vector store existente e adiciona novos docs
4. Se não existir: cria novo vector store do zero
5. Persiste no disco

**Exemplo**:

```python
from backend.vector_store import create_vector_store
from langchain.schema import Document

docs = [Document(page_content="Texto", metadata={"source": "arquivo.md"})]
vector_store = create_vector_store(docs)
```

#### `load_vector_store() -> Optional[Chroma]`

**O que faz**: Carrega um vector store existente do disco

**Retorna**: Objeto `Chroma` ou `None` se não existir

**Quando usar**: Ao iniciar o sistema, para recuperar documentos já processados

**Exemplo**:

```python
from backend.vector_store import load_vector_store

vector_store = load_vector_store()
if vector_store:
    print("Vector store carregado com sucesso!")
else:
    print("Nenhum vector store encontrado. Carregue documentos primeiro.")
```

---

## backend/processing.py

### Descrição

Pipeline de processamento de documentos: leitura, parsing, chunking e extração de metadados.

### Funções

#### `process_documents(file_paths: List[str]) -> Tuple[List[Document], dict]`

**O que faz**: Processa uma lista de arquivos e retorna documentos prontos para o vector store

**Parâmetros**:

- `file_paths`: Lista de caminhos completos dos arquivos

**Retorna**:

- `documents`: Lista de `Document` objetos
- `stats`: Dicionário com estatísticas (`{"total_chunks": 42, "total_documents": 7}`)

**Como funciona**:

1. **Para cada arquivo**:
   - Detecta tipo (MD, TXT, PDF)
   - Lê o conteúdo
   - Extrai metadados (YouTube URL, título, imagens)
   - Extrai timestamps JSON se disponível
2. **Chunking**:
   - Divide documento em chunks de 1200 caracteres
   - Mantém sobreposição de 200 caracteres
   - Preserva quebras de parágrafo
3. **Enriquecimento**:
   - Adiciona metadados técnicos (metadata_enhancer)
   - Adiciona timestamps JSON ao page_content de todos os chunks
   - Marca chunks com `has_timestamps='true'`

**Exemplo**:

```python
from backend.processing import process_documents

file_paths = ["docs/arquivo1.md", "docs/arquivo2.md"]
documents, stats = process_documents(file_paths)

print(f"Processados {stats['total_documents']} documentos")
print(f"Gerados {stats['total_chunks']} chunks")
```

#### `extract_youtube_url(content: str) -> Optional[str]`

**O que faz**: Extrai URL do YouTube do conteúdo markdown

**Procura por**:

- `[video:URL]`
- `[youtube:URL]`
- Links diretos do YouTube

**Retorna**: String com a URL ou `None`

**Exemplo**:

```python
content = "[video:https://www.youtube.com/watch?v=ABC123]"
url = extract_youtube_url(content)
# url = "https://www.youtube.com/watch?v=ABC123"
```

#### `extract_timestamps_from_document(content: str) -> Optional[dict]`

**O que faz**: Extrai timestamps do formato JSON no documento

**Formato esperado**:

```markdown
[VIDEO_TIMESTAMPS_DATA]
{
"Nome do Vídeo": [
{"start": "00:00", "end": "01:30", "line": "Descrição"}
]
}
[/VIDEO_TIMESTAMPS_DATA]
```

**Retorna**: Dicionário Python ou `None`

**Exemplo**:

```python
content = """
[VIDEO_TIMESTAMPS_DATA]
{"Video 1": [{"start": "00:00", "end": "01:00", "line": "Intro"}]}
[/VIDEO_TIMESTAMPS_DATA]
"""
timestamps = extract_timestamps_from_document(content)
# timestamps = {"Video 1": [{"start": "00:00", "end": "01:00", "line": "Intro"}]}
```

---

## backend/metadata_enhancer.py

### Descrição

Adiciona metadados técnicos aos documentos para melhorar a busca.

### Funções

#### `enhance_metadata(doc: Document, doc_index: int, total_docs: int) -> Document`

**O que faz**: Enriquece os metadados de um documento

**Adiciona**:

- `chunk_index`: Posição do chunk no documento (0, 1, 2...)
- `total_chunks`: Total de chunks do documento
- `relative_position`: Posição relativa ("start", "middle", "end")
- `content_type`: Tipo de conteúdo detectado
- `technical_terms`: Lista de termos técnicos encontrados

**Detecção de Tipos**:

- `procedural`: Se contém palavras como "passo", "clique", "selecione"
- `conceptual`: Se contém "conceito", "definição", "significa"
- `reference`: Se contém "tabela", "lista", "referência"
- `troubleshooting`: Se contém "erro", "problema", "solução"

**Exemplo**:

```python
from langchain.schema import Document
from backend.metadata_enhancer import enhance_metadata

doc = Document(
    page_content="Para criar uma pasta, clique no botão `Nova Pasta`",
    metadata={"source": "arquivo.md"}
)

enhanced = enhance_metadata(doc, doc_index=0, total_docs=5)

print(enhanced.metadata)
# {
#   "source": "arquivo.md",
#   "chunk_index": 0,
#   "total_chunks": 5,
#   "relative_position": "start",
#   "content_type": "procedural",
#   "technical_terms": ["criar", "pasta", "botão"]
# }
```

---

## backend/hybrid_retriever.py

### Descrição

Implementa busca híbrida combinando busca semântica (vetores) e busca por keywords (BM25).

### Classe `HybridRetriever`

#### `__init__(vector_store: Chroma, k: int = 6, alpha: float = 0.7)`

**Parâmetros**:

- `vector_store`: ChromaDB vector store
- `k`: Número de documentos a recuperar
- `alpha`: Peso da busca semântica (0.7 = 70% semântica, 30% keyword)

#### `get_relevant_documents(query: str) -> List[Document]`

**O que faz**: Busca documentos relevantes usando estratégia híbrida

**Como funciona**:

1. **Busca Semântica** (70%):
   - Converte query em embedding
   - Busca por similaridade de cosseno
   - Recupera top-k documentos mais similares
2. **Busca por Keywords** (30%):
   - Usa algoritmo BM25
   - Busca por palavras exatas da query
   - Recupera top-k documentos mais relevantes
3. **Combinação**:
   - Normaliza scores de ambas as buscas
   - Combina com pesos (0.7 e 0.3)
   - Ordena por score final
   - Remove duplicatas
   - Retorna top-k documentos

**Exemplo**:

```python
from backend.hybrid_retriever import HybridRetriever
from backend.vector_store import load_vector_store

vector_store = load_vector_store()
retriever = HybridRetriever(vector_store, k=6, alpha=0.7)

docs = retriever.get_relevant_documents("Como criar pasta?")
# Retorna 6 documentos mais relevantes
```

**Por que híbrido?**:

- **Semântica**: Captura intenção e contexto ("como fazer X" = "procedimento para X")
- **Keywords**: Encontra termos específicos ("botão Salvar" deve conter exatamente "Salvar")
- **Combinado**: Melhor precisão e cobertura

---

## backend/improved_prompts.py

### Descrição

Sistema de prompts adaptativos que detecta o tipo de pergunta e ajusta o prompt.

### Funções

#### `detect_prompt_type(query: str) -> str`

**O que faz**: Analisa a query e classifica em uma categoria

**Categorias**:

- `procedural`: "Como fazer X", "Passos para Y"
- `conceptual`: "O que é X", "Definição de Y"
- `troubleshooting`: "Erro X", "Problema Y", "Não funciona"
- `comparison`: "Diferença entre X e Y", "X vs Y"
- `general`: Outros casos

**Exemplo**:

```python
from backend.improved_prompts import detect_prompt_type

tipo = detect_prompt_type("Como criar uma pasta?")
# tipo = "procedural"

tipo = detect_prompt_type("O que é o módulo de compras?")
# tipo = "conceptual"

tipo = detect_prompt_type("Deu erro ao salvar")
# tipo = "troubleshooting"
```

#### `get_prompt_by_type(prompt_type: str) -> str`

**O que faz**: Retorna o prompt otimizado para cada tipo

**Prompts Disponíveis**:

1. **PROCEDURAL_PROMPT**:

```
Você é um assistente técnico especializado.
Forneça instruções passo a passo CLARAS e OBJETIVAS.
Use listas numeradas.
Destaque botões com `código`.
```

2. **CONCEPTUAL_PROMPT**:

```
Você é um professor técnico.
Explique conceitos de forma CLARA e DIDÁTICA.
Use analogias quando apropriado.
Defina termos técnicos.
```

3. **TROUBLESHOOTING_PROMPT**:

```
Você é um especialista em suporte técnico.
Identifique a CAUSA RAIZ do problema.
Forneça SOLUÇÕES específicas e testadas.
Liste possíveis causas.
```

4. **COMPARISON_PROMPT**:

```
Você é um analista técnico.
Compare de forma OBJETIVA e ESTRUTURADA.
Use tabelas quando possível.
Destaque diferenças principais.
```

**Exemplo**:

```python
from backend.improved_prompts import get_prompt_by_type

prompt = get_prompt_by_type("procedural")
# Retorna prompt otimizado para procedimentos
```

---

## backend/qa.py

### Descrição

Módulo principal de QA (Questions & Answers) com RAG chain e seleção de timestamps.

### Funções

#### `ask_question(query, vector_store, model_name=None, chat_history=None, system_prompt=None, temperature=None) -> dict`

**O que faz**: Processa uma pergunta e retorna resposta com contexto

**Parâmetros**:

- `query`: Pergunta do usuário (string)
- `vector_store`: ChromaDB vector store
- `model_name`: Modelo GPT (opcional, usa default)
- `chat_history`: Histórico de conversa (opcional)
- `system_prompt`: Prompt customizado (opcional, detecta automaticamente)
- `temperature`: Temperatura do modelo (opcional, usa default)

**Retorna**:

```python
{
    "answer": "Resposta formatada em Markdown...",
    "source_documents": [doc1, doc2, doc3, ...]
}
```

**Fluxo Completo**:

1. **Configuração**:

   - Usa valores default se não fornecidos
   - Detecta tipo de prompt baseado na query
   - Cria modelo LLM (ChatOpenAI)

2. **Retrieval (Busca)**:

   - Cria retriever MMR do vector store
   - Parâmetros: `k=6`, `lambda_mult=0.7`
   - Busca documentos relevantes

3. **Contexto**:
   - Para cada documento recuperado:
     - Extrai source name
     - Extrai YouTube URL se disponível
     - Extrai timestamps JSON se disponível
     - Remove timestamps do conteúdo para o LLM
     - Monta string de contexto
4. **Geração de Resposta**:

   - Monta prompt com: system_prompt + contexto + query
   - Chama GPT-4
   - Recebe resposta em Markdown

5. **Pós-processamento**:

   - **Se há YouTube URL**:
     - Procura timestamps do documento mais relevante
     - Calcula score de relevância para cada timestamp:
       - +1 ponto: cada palavra da query (>3 chars) que aparece em `line`
       - +10 pontos: se `line` aparece no conteúdo do chunk
     - Seleciona timestamp com maior score
     - Converte timestamp para segundos
     - Cria iframe do YouTube com `?start=SEGUNDOS`
     - Adiciona ao final da resposta

6. **Retorno**:
   - Dicionário com `answer` e `source_documents`

**Exemplo**:

```python
from backend.qa import ask_question
from backend.vector_store import load_vector_store

vector_store = load_vector_store()
result = ask_question(
    query="Como criar uma pasta?",
    vector_store=vector_store
)

print(result["answer"])
# Resposta formatada com iframe do vídeo se disponível
```

#### Seleção Inteligente de Timestamps

**Algoritmo**:

```python
for timestamp in timestamps:
    score = 0

    # Score 1: Palavras da query na descrição
    for word in query.split():
        if len(word) > 3 and word.lower() in timestamp['line'].lower():
            score += 1

    # Score 2: Descrição aparece no chunk relevante
    if timestamp['line'][:50] in first_doc_content.lower():
        score += 10

    if score > best_score:
        best_score = score
        best_timestamp = timestamp
```

**Exemplo Prático**:

```
Query: "onde está o botão para criar pasta?"

Timestamps disponíveis:
1. {"start": "00:01", "line": "Introdução ao módulo de armazenamento"}
   → Score: 0 (nenhuma palavra relevante)

2. {"start": "02:35", "line": "Como criar e gerenciar pastas no sistema"}
   → Score: 3 ("criar" + "pasta" + "gerenciar" na descrição)

Selecionado: Timestamp 2 (02:35) ✅
```

---

## frontend/main.py

### Descrição

Interface Streamlit com 2 abas: Chat e Upload de Documentos.

### Estrutura

#### Session State

```python
st.session_state.docs_loaded = False  # Documentos carregados?
st.session_state.vector_store = None  # ChromaDB instance
st.session_state.messages = []        # Histórico do chat
```

#### Menu Lateral

- Logo do Koper
- Título do assistente
- Botão "Limpar Histórico"
- Perguntas sugeridas (6 exemplos)

#### Aba 1: 💬 Chat

**Componentes**:

1. **Verificação**: Checa se `docs_loaded == True`
2. **Histórico**: Exibe todas as mensagens (`st.chat_message`)
3. **Input**: Campo de texto (`st.chat_input`)
4. **Processamento**:
   - Adiciona mensagem do usuário ao histórico
   - Chama `ask_question()`
   - Adiciona resposta ao histórico
   - `st.rerun()` para atualizar interface

**Fluxo**:

```
Usuário digita → Adiciona ao histórico → ask_question() →
Adiciona resposta → st.rerun() → Interface atualizada
```

#### Aba 2: 📤 Upload de Documentos

**Opção A: Carregar pasta docs/**

```python
def load_docs_folder():
    file_paths = [f"docs/{f}" for f in os.listdir("docs") if f.endswith(".md")]
    documents, stats = process_documents(file_paths)
    vector_store = create_vector_store(documents)
    st.session_state.vector_store = vector_store
    st.session_state.docs_loaded = True
```

**Opção B: Upload manual**

```python
uploaded_files = st.file_uploader("Arraste arquivos aqui", type=["md", "txt", "pdf"])
def process_uploaded_files(files):
    # Salva arquivos temporários
    # Processa com process_documents()
    # Atualiza vector_store
```

### Funções Auxiliares

#### `load_docs_folder() -> Tuple[bool, str]`

- Lista arquivos `.md` em `docs/`
- Processa todos com `process_documents()`
- Cria/atualiza vector store
- Retorna `(sucesso, mensagem)`

#### `process_uploaded_files(files) -> Tuple[bool, str]`

- Salva arquivos temporários
- Processa com `process_documents()`
- Cria/atualiza vector store
- Retorna `(sucesso, mensagem)`

---

## gerar_documentacao_video.py

### Descrição

Script para gerar documentação estruturada a partir de vídeos do YouTube.

### Funções Principais

#### `extrair_video_id(url: str) -> Optional[str]`

- Extrai ID do vídeo de URLs do YouTube
- Suporta formatos: `watch?v=ID`, `youtu.be/ID`, etc.

#### `obter_transcricao(video_id: str) -> List[dict]`

- Usa `youtube-transcript-api`
- Baixa transcrição em português
- Retorna lista de entries: `[{"start": 0.0, "duration": 2.5, "text": "..."}]`

#### `dividir_em_chunks(transcript, intervalo_segundos=60) -> List[dict]`

- Agrupa transcrição em chunks temporais
- Cada chunk: `{"start": 0.0, "end": 60.0, "text": "..."}`
- Padrão: chunks de 60 segundos

#### `gerar_secao_com_ia(chunk, client, video_title) -> str`

- Envia chunk para GPT-4
- Gera seção Markdown estruturada
- Retorna texto formatado com título e conteúdo

#### `gerar_timestamps_json(chunks, video_title) -> dict`

- Converte chunks em formato JSON de timestamps
- Cria descrições a partir do texto (primeiros 100 chars)
- Retorna: `{"Video Title": [{"start": "00:00", "end": "01:00", "line": "..."}]}`

#### `segundos_para_timestamp(segundos: float) -> str`

- Converte segundos para formato `HH:MM:SS` ou `MM:SS`
- Exemplo: `125.5` → `"02:05"`

### Fluxo de Execução

```
1. Usuário informa URL do YouTube
2. Extrai video_id
3. Baixa transcrição
4. Divide em chunks (60s cada)
5. Para cada chunk:
   - Envia para GPT-4
   - Gera seção Markdown
6. Cria JSON de timestamps
7. Salva arquivo em docs/
```

**Exemplo de Output**:

```markdown
# Passo a passo - Tutorial XYZ

[video:https://www.youtube.com/watch?v=ABC123]

## Introdução ao Sistema

Conteúdo gerado pela IA...

## Criando Registros

Mais conteúdo...

[VIDEO_TIMESTAMPS_DATA]
{
"Tutorial XYZ": [
{"start": "00:00", "end": "01:00", "line": "Introdução..."},
{"start": "01:00", "end": "02:00", "line": "Criando..."}
]
}
[/VIDEO_TIMESTAMPS_DATA]
```

---

## 🔧 Fluxo Completo do Sistema

### 1. Processamento de Documentos

```
Arquivo .md → process_documents() →
  ↓
  - Extrai YouTube URL
  - Extrai timestamps JSON
  - Divide em chunks (1200 chars, overlap 200)
  - Adiciona metadados (metadata_enhancer)
  - Adiciona timestamps a TODOS os chunks
  ↓
Documents → create_vector_store() →
  ↓
  - Gera embeddings (OpenAI)
  - Armazena no ChromaDB
  ↓
Vector Store salvo em ./db
```

### 2. Query & Response

```
Usuário faz pergunta →
  ↓
ask_question() →
  ↓
  1. Detecção de tipo de prompt
  2. Retrieval (MMR, k=6)
  3. Extração de timestamps dos docs recuperados
  4. Montagem de contexto
  5. Chamada GPT-4
  6. Seleção inteligente de timestamp:
     - Calcula score para cada timestamp
     - Seleciona com maior score
  7. Conversão para segundos
  8. Criação de iframe do YouTube
  ↓
Resposta com vídeo embedado → Interface Streamlit
```

### 3. Seleção de Timestamp

```
Documentos recuperados →
  ↓
Extrai timestamps do doc mais relevante →
  ↓
Para cada timestamp:
  - Score baseado em palavras da query
  - Bonus se descrição aparece no chunk
  ↓
Seleciona timestamp com maior score →
  ↓
Converte "MM:SS" para segundos →
  ↓
Cria URL: youtube.com/embed/ID?start=SEGUNDOS →
  ↓
Iframe HTML adicionado à resposta
```

---

## 📊 Métricas e Performance

### Chunking

- **Tamanho**: 1200 caracteres
- **Overlap**: 200 caracteres
- **Documentos típicos**: 5-10 chunks por arquivo
- **Total no sistema**: ~2500 chunks

### Retrieval

- **Documentos recuperados**: 6
- **Estratégia**: MMR (Maximal Marginal Relevance)
- **Lambda**: 0.7 (70% relevância, 30% diversidade)

### Embeddings

- **Modelo**: text-embedding-3-small
- **Dimensões**: 1536
- **Custo**: $0.02 por 1M tokens

### LLM

- **Modelo**: gpt-4o-mini
- **Temperatura**: 0.3
- **Tokens médios por resposta**: ~500-800
- **Custo**: $0.15 por 1M tokens input, $0.60 por 1M tokens output

---

## 🚀 Otimizações Implementadas

### 1. Busca Híbrida

- Combina semântica (70%) + keywords (30%)
- Melhor recall e precision

### 2. Timestamps nos Chunks

- Todos os chunks do documento incluem timestamps
- Não precisa achar chunk específico com tag `[video:]`

### 3. Seleção Inteligente

- Score baseado em relevância
- Não usa sempre o primeiro timestamp

### 4. MMR Retrieval

- Evita documentos muito similares
- Aumenta diversidade no contexto

### 5. Prompts Adaptativos

- Detecta tipo de pergunta
- Usa prompt especializado

---

**Documentação atualizada em**: Novembro 2025
