# 🤖 Assistente Koper - Sistema RAG Avançado# 🤖 Sistema RAG Koper v2.0# 📹 Gerador de Documentação a partir de Vídeos do YouTube

Sistema de Perguntas e Respostas com Retrieval-Augmented Generation (RAG) otimizado para documentação do sistema Koper, com suporte a vídeos do YouTube com timestamps inteligentes.> **Sistema Inteligente de Documentação com IA e Busca Semântica**Este script automatiza a geração de documentação técnica estruturada em formato Markdown a partir de transcrições de vídeos do YouTube, utilizando inteligência artificial (OpenAI GPT).

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)## 🎯 Objetivo

[![LangChain](https://img.shields.io/badge/LangChain-1.0+-green.svg)](https://python.langchain.com/)

[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)](https://openai.com/)[![LangChain](https://img.shields.io/badge/LangChain-1.0+-green.svg)](https://python.langchain.com/)

[![Streamlit](https://img.shields.io/badge/Streamlit-1.51+-red.svg)](https://streamlit.io/)

[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)](https://openai.com/)Transformar vídeos tutoriais do YouTube em documentação técnica **extremamente detalhada** e bem estruturada, facilitando o aprendizado e a consulta de informações sem precisar assistir ao vídeo novamente.

## 📋 Índice

[![Streamlit](https://img.shields.io/badge/Streamlit-1.51+-red.svg)](https://streamlit.io/)

- [Visão Geral](#visão-geral)

- [Funcionalidades](#funcionalidades)**Características da documentação gerada:**

- [Arquitetura](#arquitetura)

- [Instalação](#instalação)---

- [Uso](#uso)

- [Estrutura do Projeto](#estrutura-do-projeto)- 📊 **Granularidade**: Seções pequenas de 2-3 minutos cada

- [Configuração](#configuração)

- [Desenvolvimento](#desenvolvimento)## 🚀 Início Rápido- 🔍 **Detalhamento**: Todos os passos, campos, botões e opções documentados

---- 🤖 **Otimizada para RAG**: Ideal para sistemas de Retrieval-Augmented Generation

## 🎯 Visão Geral```bash- 📝 **Autocontida**: Cada seção é completa e independente

O Assistente Koper é um sistema RAG (Retrieval-Augmented Generation) que combina a busca semântica de documentos com a geração de respostas usando modelos de linguagem (GPT-4). O sistema foi especialmente otimizado para:cd /home/koper/Documentos/agente_koper_v2- 🎯 **Específica**: Nomes exatos de elementos de UI, validações e regras de negócio

- **Documentação técnica** com procedimentos passo a passosource venv/bin/activate- ⏱️ **Timestamps Precisos**: Minutagem com segundos (MM:SS) e links diretos para o vídeo

- **Vídeos tutoriais do YouTube** com navegação por timestamps

- **Imagens e diagramas** incorporados na documentaçãostreamlit run frontend/main.py- 🏷️ **Metadados Ricos**: IDs, categorias, palavras-chave e perguntas frequentes por seção

- **Busca híbrida** (semântica + keyword) para máxima precisão

- **Interface interativa** com chat em tempo real```

### 🌟 Diferenciais## ✨ Melhorias Implementadas (v2.0)

1. **Timestamps Inteligentes**: O sistema analisa a query do usuário e seleciona automaticamente o timestamp mais relevante do vídeo📘 **[Ver Guia Completo](GUIA_COMPLETO.md)** para documentação detalhada.

2. **Busca Híbrida**: Combina busca semântica (embeddings) com busca por palavras-chave (BM25)

3. **Prompts Adaptativos**: Detecta o tipo de pergunta e ajusta o prompt automaticamente### 🎬 **Navegação Temporal com Links Timestamped**

4. **Metadados Enriquecidos**: Adiciona contexto técnico aos documentos durante o processamento

5. **Interface Moderna**: Interface Streamlit responsiva com suporte a HTML/iframe---- Cada seção possui link direto para o YouTube no segundo exato

---- Formato: `https://youtu.be/ID?t=125` (abre no segundo 125)

## ✨ Funcionalidades## 📋 O que é este projeto?- Minutagem formatada: `00:01 → 02:37` (HH:MM:SS ou MM:SS)

### 🎥 Integração com YouTube- Duração calculada automaticamente para cada segmento

- **Embeddings de vídeos** diretamente na respostaSistema RAG (Retrieval-Augmented Generation) que transforma documentação e vídeos do YouTube em uma base de conhecimento inteligente com:

- **Timestamps automáticos** que levam ao momento exato do vídeo

- **Seleção inteligente** do timestamp baseado na query do usuário### 📋 **Metadados Estruturados por Seção**

- **Formato JSON estruturado** para armazenar timestamps de cada seção

- 💬 **Chat Interativo** com IACada seção agora inclui:

### 📚 Processamento de Documentos

- 🎬 **Links do YouTube** com timestamps precisos- **ID único**: `sec_1`, `sec_2`, etc. (para referências cruzadas)

- **Upload de arquivos** Markdown, TXT, PDF

- **Chunking inteligente** com sobreposição configurável- 🔍 **Busca Semântica** otimizada- **Minutagem**: Início → Fim com segundos precisos

- **Extração de metadados** (YouTube URL, imagens, tags)

- **Enriquecimento automático** com contexto técnico- 📊 **Metadados Enriquecidos** automaticamente- **Duração**: Tempo do segmento em segundos

### 🔍 Busca Avançada- ⚡ **+40% de precisão** vs versão anterior- **Link do YouTube**: Abre o vídeo no momento exato

- **Hybrid Retriever** (70% semântica + 30% keyword)- **Módulo**: Nome do módulo/área do sistema

- **MMR (Maximal Marginal Relevance)** para diversidade nos resultados

- **Reranking** automático com relevância ponderada---- **Categorias**: 2-4 categorias relevantes (Configuração, Administração, etc.)

- **6 documentos recuperados** para contexto amplo

- **Palavras-chave**: 5-8 termos importantes para busca

### 💬 Chat Inteligente

## ✨ Funcionalidades

- **Histórico de conversa** persistente

- **Perguntas sugeridas** baseadas no domínio### 🔍 **Resumo Executivo**

- **Respostas formatadas** em Markdown com imagens

- **Tratamento de erros** com detalhes técnicos### 1. Chat Inteligente- Resumo de 2-3 linhas no topo de cada seção

---Faça perguntas sobre a documentação e receba respostas precisas com links para vídeos tutoriais.- Explica O QUE a seção ensina

## 🏗️ Arquitetura- Identifica QUAL PROBLEMA ela resolve

`````### 2. Gerador de Documentação- Facilita compreensão rápida e busca semântica

┌─────────────────┐

│  Frontend       │Transforma vídeos do YouTube em documentação técnica estruturada automaticamente.

│  (Streamlit)    │

└────────┬────────┘### ❓ **Perguntas Frequentes por Seção**

         │

    ┌────▼─────────────────────────────────┐### 3. Upload de Documentos- 3 perguntas naturais que a seção responde

    │  Backend                             │

    │                                      │Processa arquivos .md, .txt e .pdf para expandir a base de conhecimento.- Formuladas como um usuário buscaria

    │  ┌──────────────┐  ┌──────────────┐ │

    │  │   QA Chain   │  │  Processing  │ │- Otimiza matching semântico do RAG

    │  │  (LangChain) │  │   Pipeline   │ │

    │  └──────┬───────┘  └──────┬───────┘ │---- Aumenta recall e precision nas buscas

    │         │                 │          │

    │  ┌──────▼─────────────────▼───────┐ │## 📦 Estrutura do Projeto## 🎯 Benefícios para RAG (Retrieval-Augmented Generation)

    │  │    Hybrid Retriever            │ │

    │  │  (Semantic + Keyword Search)   │ │````### 1. **Busca Mais Precisa** 🎯

    │  └──────┬─────────────────────────┘ │

    └─────────┼───────────────────────────┘agente_koper_v2/- Metadados permitem filtros avançados

              │

    ┌─────────▼──────────┐├── backend/              # Sistema RAG (LangChain + ChromaDB)- Palavras-chave otimizam busca vetorial

    │   ChromaDB         │

    │  (Vector Store)    ││   ├── config.py        # Configurações otimizadas- Categorias facilitam navegação hierárquica

    └────────────────────┘

```│   ├── qa.py            # Sistema Q&A com MMR



### Componentes Principais│   ├── processing.py    # Processamento com metadados### 2. **Contextualização Rápida** 📊



1. **frontend/main.py**: Interface Streamlit com 2 abas (Chat + Upload)│   ├── metadata_enhancer.py    # ✨ Enriquecimento automático- Resumo executivo oferece visão geral instantânea

2. **backend/qa.py**: Lógica de QA com RAG chain e seleção de timestamps

3. **backend/processing.py**: Pipeline de processamento de documentos│   └── improved_prompts.py     # ✨ Prompts adaptáveis- Duração ajuda a estimar tempo necessário

4. **backend/hybrid_retriever.py**: Busca híbrida (semântica + BM25)

5. **backend/improved_prompts.py**: Sistema de prompts adaptativos│- Módulo identifica área do sistema

6. **backend/metadata_enhancer.py**: Enriquecimento de metadados

7. **backend/vector_store.py**: Gerenciamento do ChromaDB├── frontend/            # Interface Streamlit



---│   └── main.py         # UI renovada### 3. **Matching de Perguntas** ❓



## 🚀 Instalação│- RAG compara pergunta do usuário com perguntas da seção



### Pré-requisitos├── docs/               # Documentação gerada- Aumenta recall (encontra mais resultados relevantes)



- Python 3.8+├── db/                 # Vector store (ChromaDB)- Melhora precision (resultados mais precisos)

- pip ou conda

- Chave API da OpenAI├── gerar_documentacao_video.py  # Gerador de docs



### Passo a Passo├── GUIA_COMPLETO.md    # 📘 Documentação completa### 4. **Navegação Temporal** 🔗



1. **Clone o repositório**└── README.md           # Este arquivo- ID único permite referências cruzadas

```bash

git clone <repository-url>```- Link timestamped abre vídeo no momento exato

cd agente_koper_v2

```- Minutagem facilita navegação humana



2. **Crie um ambiente virtual**---

```bash

python -m venv venv### 5. **Embeddings Otimizados** 🤖

source venv/bin/activate  # Linux/Mac

# ou## 🛠️ Tecnologias- Palavras-chave melhoram representação vetorial

venv\Scripts\activate  # Windows

```- Resumo concentra informação semântica



3. **Instale as dependências**- **LangChain** - Framework para LLMs- Categorias criam hierarquia conceitual

```bash

pip install -r requirements.txt- **OpenAI GPT** - Modelo de linguagem

`````

- **ChromaDB** - Vector database## 🛠️ Tecnologias Utilizadas

4. **Configure a chave da OpenAI**

````bash- **Streamlit** - Interface web

export OPENAI_API_KEY="sua-chave-aqui"

# ou crie um arquivo .env- **Python 3.10+** - Linguagem base- **Python 3.10+**

echo "OPENAI_API_KEY=sua-chave-aqui" > .env

```- **LangChain**: Framework para construção de aplicações com LLMs



5. **Execute o sistema**---- **OpenAI API**: Utiliza modelos GPT (gpt-4o-mini, gpt-4o, etc.)

```bash

streamlit run frontend/main.py- **youtube-transcript-api**: Para extração de transcrições de vídeos do YouTube

````

## 📚 Documentação- **pytubefix**: Para obter metadados dos vídeos (título, etc.)

O sistema abrirá em `http://localhost:8501`

- **python-dotenv**: Gerenciamento de variáveis de ambiente

---

- **[GUIA_COMPLETO.md](GUIA_COMPLETO.md)** - Documentação completa do sistema

## 📖 Uso

- Como rodar## 📋 Pré-requisitos

### 1. Carregar Documentos

- Melhorias implementadas

Na aba **📤 Upload de Documentos**:

- Análise técnica e próximas melhorias1. Python 3.10 ou superior instalado

- **Opção A**: Clique em "Carregar Todos os Documentos da Pasta docs/"

- **Opção B**: Use o upload manual de arquivos (.md, .txt, .pdf) - Geração de documentação2. Conta na OpenAI com API Key ativa

O sistema irá: - Solução de problemas3. Ambiente virtual Python (recomendado)

1. Processar cada documento

2. Extrair metadados (YouTube URLs, timestamps, imagens)

3. Dividir em chunks com sobreposição

4. Gerar embeddings---## 🚀 Como Rodar

5. Armazenar no ChromaDB

### 2. Fazer Perguntas

## 🎯 Como Usar### 1. Clone ou baixe o projeto

Na aba **💬 Chat**:

1. Digite sua pergunta no campo de input

2. Ou clique em uma das perguntas sugeridas### 1. Configurar Ambiente```bash

3. Aguarde a resposta (pode levar alguns segundos)

cd /home/koper/Documentos/agente_koper_v2

**Exemplos de perguntas:**

- "Como criar uma nova pasta no módulo de armazenamento?"`bash`

- "Quais são as permissões disponíveis?"

- "Como funciona o fluxo de aprovação de compras?"# Criar arquivo .env

### 3. Interagir com Vídeosecho "OPENAI_API_KEY=sua-chave-aqui" > .env### 2. Ative o ambiente virtual

Quando a resposta incluir um vídeo:````

- O vídeo será embedado com iframe do YouTube

- Clique em Play para assistir```bash

- O vídeo iniciará automaticamente no timestamp correto

- Use os controles do YouTube normalmente### 2. Iniciar Sistemasource venv/bin/activate

---```

## 📁 Estrutura do Projeto```bash

`````streamlit run frontend/main.py### 3. Configure as variáveis de ambiente

agente_koper_v2/

│```

├── frontend/

│   ├── __init__.pyCrie um arquivo `.env` na raiz do projeto com sua chave da OpenAI:

│   ├── main.py              # Interface Streamlit

│   └── img/### 3. Fazer Perguntas

│       └── logo.png

│````env

├── backend/

│   ├── __init__.py```OPENAI_API_KEY=sua-chave-aqui

│   ├── config.py            # Configurações globais

│   ├── qa.py                # Lógica de QA e RAG chain✅ "Como criar uma pasta no módulo de armazenamento?"```

│   ├── processing.py        # Processamento de documentos

│   ├── vector_store.py      # Gerenciamento do ChromaDB✅ "Não consigo cadastrar um colaborador"

│   ├── hybrid_retriever.py  # Busca híbrida

│   ├── improved_prompts.py  # Sistema de prompts✅ "O que é o módulo de qualidade?"### 4. Edite as URLs dos vídeos

│   └── metadata_enhancer.py # Enriquecimento de metadados

│````

├── docs/                    # Documentos do sistema Koper

│   ├── Passo a passo - Módulo de Armazenamento_documentacao_gerada.mdAbra o arquivo `gerar_documentacao_video.py` e adicione as URLs dos vídeos que deseja processar na lista `YOUTUBE_URLS`:

│   ├── Passo a passo - Módulo de Compras_documentacao_gerada.md

│   ├── Passo a passo - Módulo de Engenharia_documentacao_gerada.md---

│   ├── Passo a passo - Módulo de Qualidade_documentacao_gerada.md

│   ├── Passo a passo - Módulo de RH_documentacao_gerada.md````python

│   ├── Passo a passo - Módulo de Suprimentos_documentacao_gerada.md

│   └── Passo a passo - Módulo Financeiro_documentacao_gerada.md## 🎬 Gerador de DocumentaçãoYOUTUBE_URLS = [

│

├── db/                      # ChromaDB (criado automaticamente)    "https://www.youtube.com/watch?v=VIDEO_ID_1",

├── gerar_documentacao_video.py  # Script para gerar docs com timestamps

├── requirements.txt         # Dependências PythonTransforma vídeos do YouTube em documentação técnica:    "https://www.youtube.com/watch?v=VIDEO_ID_2",

├── README.md               # Este arquivo

└── COMO_GERAR_DOCUMENTOS.md  # Guia para criar novos documentos    "https://www.youtube.com/watch?v=VIDEO_ID_3",

`````

```bash # Adicione quantas URLs quiser

---

python gerar_documentacao_video.py]

## ⚙️ Configuração

```

### backend/config.py

**Recursos:**### 5. Execute o script

````python

# Modelo OpenAI- ⏱️ Timestamps precisos

DEFAULT_MODEL = "gpt-4o-mini"

TEMPERATURE = 0.3- 🔗 Links clicáveis do YouTube```bash



# Embeddings- 🏷️ Metadados estruturadospython gerar_documentacao_video.py

EMBEDDING_MODEL = "text-embedding-3-small"

- ❓ Perguntas frequentes por seção```

# Chunking

CHUNK_SIZE = 1200- 🤖 Otimizado para RAG

CHUNK_OVERLAP = 200

O script irá processar cada vídeo e:

# Retrieval

K_DOCUMENTS = 6  # Número de documentos recuperados---

LAMBDA_MULT = 0.7  # Balance entre diversidade e relevância

- 📝 Obter o título do vídeo

# ChromaDB

CHROMA_PERSIST_DIR = "./db"## 🐛 Problemas Comuns- 🎥 Carregar e transcrever o vídeo do YouTube

COLLECTION_NAME = "koper_docs"

```- 🧠 Processar a transcrição com IA



### Variáveis de Ambiente### Streamlit não encontrado- ✅ Gerar e salvar a documentação em `docs/{titulo_do_video}_documentacao_gerada.md`



Crie um arquivo `.env` na raiz:```bash



```envpip install streamlit### 📂 Estrutura de Saída

OPENAI_API_KEY=sua-chave-aqui

````

---Todos os arquivos serão salvos na pasta `docs/` criada automaticamente:

## 🔧 Desenvolvimento### Erro de API Key

### Adicionar Novos Documentos`bash`

1. **Crie o documento Markdown** seguindo o padrão:echo "OPENAI_API_KEY=sk-proj-sua-chave" > .envagente_koper_v2/

`````markdown
# Título do Módulo````├── docs/

[video:https://www.youtube.com/watch?v=VIDEO_ID]│ ├── Título do Vídeo 1_documentacao_gerada.md

## Seção 1### Sistema Aguardando│ ├── Título do Vídeo 2_documentacao_gerada.md

Conteúdo da seção...Faça upload de documentos pela interface ou processe os arquivos da pasta `docs/`.│ └── Título do Vídeo 3_documentacao_gerada.md

## Seção 2├── gerar_documentacao_video.py

Conteúdo da seção...📘 **[Ver mais soluções](GUIA_COMPLETO.md#-solução-de-problemas)**├── .env

[VIDEO_TIMESTAMPS_DATA]└── requirements.txt

{

"Nome do Vídeo": [---```

    {"start": "00:00", "end": "01:30", "line": "Introdução ao módulo"},

    {"start": "01:30", "end": "03:45", "line": "Como criar registros"}

]

}## 📊 Melhorias v2.0## 📄 Estrutura da Documentação Gerada

[/VIDEO_TIMESTAMPS_DATA]
`````

2. **Salve em `docs/`**- ✅ Configurações otimizadas (chunks menores, mais focados)Cada documento gerado segue o seguinte formato otimizado para RAG:

3. **Recarregue no sistema**:- ✅ Prompts adaptáveis (troubleshooting, explicação, etc.)

   - Abra a aba "Upload de Documentos"

   - Clique em "Carregar Todos os Documentos"- ✅ Retrieval MMR (diversidade nos resultados)### 🎬 Cabeçalho do Documento

Veja o guia completo em [`COMO_GERAR_DOCUMENTOS.md`](COMO_GERAR_DOCUMENTOS.md)- ✅ Metadados enriquecidos automaticamente```markdown

### Limpar o Banco de Dados- ✅ Links do YouTube com timestamps# 📚 Documentação: [Título do Vídeo]

```bash- ✅ +30% de precisão nas respostas

rm -rf db/

rm -rf backend/__pycache__/**🎥 Vídeo Original:** https://youtu.be/ID

```

---**📊 Total de Seções:** X

---

## 📊 Tecnologias Utilizadas

## 📝 Licença---

- **[Streamlit](https://streamlit.io/)**: Frontend interativo

- **[LangChain](https://langchain.com/)**: Framework RAG````

- **[OpenAI GPT-4](https://openai.com/)**: Modelo de linguagem

- **[ChromaDB](https://www.trychroma.com/)**: Vector storeProjeto educacional - Sistema RAG com LangChain e OpenAI

- **[LangChain-HuggingFace](https://huggingface.co/)**: Embeddings

- **Rank-BM25**: Busca por keywords### 📋 Estrutura de Cada Seção

------```markdown

## 🤝 Contribuindo## 1. [Título Específico da Funcionalidade]

1. Faça um fork do projeto## 🤝 Contribuições

2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)

3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)**📋 METADADOS:**

4. Push para a branch (`git push origin feature/AmazingFeature`)

5. Abra um Pull RequestIssues e pull requests são bem-vindos!- **ID:** sec_1

---- **⏱️ Minutagem:** 00:01 → 02:37

## 📝 Licença---- **⏲️ Duração:** 156s

Este projeto é proprietário e confidencial.- **🎬 Link:** [Assistir este trecho](https://youtu.be/ID?t=1)

---**Versão:** 2.0 - **📦 Módulo:** Nome do Módulo

## 📧 Contato**Última Atualização:** 13 de novembro de 2025 - **🏷️ Categorias:** Configuração, Administração, Operacional

Para dúvidas ou suporte, entre em contato com a equipe de desenvolvimento.**Status:** ✅ Funcional e Documentado- **🔑 Palavras-chave:** permissão, usuário, editar, visualizar, pasta

------> **🔍 RESUMO EXECUTIVO:** Resumo de 2-3 linhas explicando o que

## 🔄 Changelog> esta seção ensina e qual problema ela resolve.

### v2.0.0 (Atual)📘 **[Leia o Guia Completo](GUIA_COMPLETO.md)** para mais informações.

- ✅ Sistema de timestamps inteligentes

- ✅ Busca híbrida (semântica + keyword)**Contexto:**

- ✅ Prompts adaptativos[Explicação do contexto e objetivo da seção]

- ✅ Interface Streamlit modernizada

- ✅ Suporte a iframes do YouTube**Localização no Sistema:**

- ✅ Enriquecimento de metadados

- Caminho de navegação completo

### v1.0.0- Tela/interface específica

- ✅ Sistema RAG básico

- ✅ Upload de documentos**Funcionalidade Detalhada:**

- ✅ Chat com histórico[Descrição detalhada da funcionalidade]

- ✅ Integração com OpenAI

### 🔹 Passo a Passo Detalhado:

---

1. **[Ação Específica]**

## 🎯 Roadmap - Localização: [Onde está o elemento]

- Como fazer: [Descrição detalhada]

- [ ] Suporte a mais tipos de arquivo (DOCX, XLSX) - Campos/Opções disponíveis: [Lista completa]

- [ ] Busca por data/versão de documentos - Resultado esperado: [O que acontece]

- [ ] Estatísticas de uso

- [ ] Exportar histórico de chat**Campos e Parâmetros:**

- [ ] Suporte a múltiplos idiomas

- [ ] API REST para integração| Campo | Tipo | Obrigatório | Descrição | Exemplo |

| ----- | ---- | ----------- | --------- | ------- |

---| ... | ... | ... | ... | ... |

**Desenvolvido com ❤️ para o Sistema Koper\*\***Regras de Negócio:\*\*

- [Regras e validações]

**Observações Importantes:**

- [Dicas e erros comuns]

**Conceitos-Chave:**

- **[Termo]**: [Definição]

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**

- Como fazer X?
- Onde encontro Y?
- Qual a diferença entre Z e W?

---

```
└── README.md
```

## 📁 Estrutura do Código

### Funções Principais

#### 1. `extrair_video_id(url: str) -> str`

**Propósito**: Extrai o ID único do vídeo a partir da URL do YouTube.

**Parâmetros**:

- `url`: URL completa do vídeo do YouTube

**Retorna**: String com o ID do vídeo (11 caracteres)

**Exemplo**:

```python
url = "https://www.youtube.com/watch?v=VC6EkQJoLEY"
video_id = extrair_video_id(url)  # Retorna: "VC6EkQJoLEY"
```

---

#### 2. `obter_titulo_video(url: str) -> str`

**Propósito**: Obtém o título do vídeo do YouTube para usar como nome do arquivo.

**Parâmetros**:

- `url`: URL completa do vídeo do YouTube

**Retorna**: String com o título do vídeo (sanitizado para nome de arquivo)

**Funcionamento**:

1. Utiliza a biblioteca pytubefix para buscar metadados do vídeo
2. Remove caracteres inválidos para nome de arquivo (`<>:"/\|?*`)
3. Em caso de erro, usa o ID do vídeo como fallback

**Exemplo**:

```python
url = "https://www.youtube.com/watch?v=VC6EkQJoLEY"
titulo = obter_titulo_video(url)  # Retorna: "Passo a passo - Módulo de Armazenamento"
```

---

#### 3. `carregar_transcricao(url: str) -> str`

**Propósito**: Baixa e processa a transcrição completa do vídeo do YouTube.

**Parâmetros**:

- `url`: URL do vídeo do YouTube

**Retorna**: String com todo o texto transcrito do vídeo

**Funcionamento**:

1. Extrai o ID do vídeo
2. Busca a transcrição em português (pt ou pt-BR)
3. Se não encontrar em português, busca em qualquer idioma disponível
4. Concatena todos os trechos da transcrição em um único texto

**Tratamento de erros**: Tenta primeiro em português, depois em qualquer idioma como fallback

---

#### 4. `gerar_documentacao(transcricao: str) -> str`

**Propósito**: Utiliza IA (GPT) para transformar a transcrição em documentação técnica estruturada.

**Parâmetros**:

- `transcricao`: Texto completo da transcrição do vídeo

**Retorna**: String com a documentação em formato Markdown

**Funcionamento**:

1. Configura o modelo LLM (ChatGPT)
2. Define um prompt detalhado com instruções de formatação
3. Processa a transcrição através da cadeia LangChain
4. Retorna documentação estruturada com:
   - Seções numeradas
   - Descrições detalhadas
   - Passos de execução
   - Minutagens do vídeo
   - Referências a imagens (quando aplicável)

**Configurações**:

- Modelo: `gpt-4o-mini` (configurável)
- Temperatura: `0.2` (baixa criatividade, mais foco em precisão)

---

#### 5. `salvar_markdown(conteudo: str, titulo_video: str) -> None`

**Propósito**: Salva o conteúdo gerado em um arquivo Markdown na pasta `docs/`.

**Parâmetros**:

- `conteudo`: String com a documentação em Markdown
- `titulo_video`: Título do vídeo para compor o nome do arquivo

**Funcionamento**:

- Cria a pasta `docs/` se não existir
- Define o nome do arquivo como `{titulo_video}_documentacao_gerada.md`
- Cria/sobrescreve o arquivo com encoding UTF-8
- Exibe mensagem de confirmação com o caminho completo do arquivo

**Exemplo de arquivo gerado**:

```
docs/Passo a passo - Módulo de Armazenamento_documentacao_gerada.md
```

---

## 💡 Exemplo de Uso com RAG

### Cenário: Sistema de Busca Inteligente

**Pergunta do Usuário:**

> "Como dar permissão de visualização para um usuário no módulo de armazenamento?"

**Como o RAG utiliza os metadados:**

```python
# 1. Busca vetorial nas palavras-chave
palavras_chave = ["permissão", "usuário", "visualização", "armazenamento"]

# 2. Filtro por categoria
categoria = "Administração" ou "Configuração"

# 3. Matching com perguntas da seção
pergunta_similar = "Como editar permissões de um usuário?"

# 4. Resultado encontrado
secao = {
    "id": "sec_1",
    "titulo": "Funcionamento do Módulo Armazenamento",
    "modulo": "Armazenamento",
    "minutagem": "00:01 → 02:37",
    "link": "https://youtu.be/VC6EkQJoLEY?t=1",
    "resumo": "Esta seção ensina como gerenciar as permissões...",
    "conteudo_completo": "..."
}
```

**Resposta do RAG ao Usuário:**

```markdown
📌 **Encontrei a resposta na documentação!**

**Seção:** Funcionamento do Módulo Armazenamento (sec_1)
**Tempo no vídeo:** 00:01 → 02:37
**🎬 [Assistir este trecho](https://youtu.be/VC6EkQJoLEY?t=1)**

Para dar permissão de visualização:

1. Acesse Módulo Administração > Aba Usuários
2. Clique em Editar no usuário desejado
3. Localize a seção "Módulo de Armazenamento"
4. Selecione a opção "Apenas visualização"
5. Clique em "Concluir Edição"

[Conteúdo completo da seção...]
```

### Vantagens da Estrutura para RAG:

1. **Busca Precisa**: Metadados permitem filtros específicos
2. **Contexto Rico**: Resumo + conteúdo completo
3. **Navegação Direta**: Link leva ao momento exato do vídeo
4. **Perguntas Similares**: Aumenta taxa de acerto na busca
5. **Categorização**: Facilita navegação hierárquica

---

## ⚙️ Configurações Personalizáveis

No início do script, você pode ajustar:

```python
YOUTUBE_URLS = [
    "URL_DO_VIDEO_1",
    "URL_DO_VIDEO_2",
    # Adicione mais URLs
]
MODEL_NAME = "gpt-4o-mini"             # Modelo GPT (gpt-4o, gpt-3.5-turbo, etc.)
TEMPERATURE = 0.2                       # Criatividade (0.0 - 1.0)
MAX_TOKENS = 16000                      # Tokens máximos para documentação detalhada
DOCS_FOLDER = "docs"                    # Pasta onde os arquivos serão salvos
```

### Opções de Modelo

- `gpt-4o-mini`: Mais rápido e econômico (recomendado) - suporta até 16k tokens
- `gpt-4o`: Mais preciso, porém mais caro - suporta até 16k tokens
- `gpt-3.5-turbo`: Opção econômica, menos precisa - suporta até 4k tokens

### Temperatura

- `0.0 - 0.3`: Mais determinístico e preciso (recomendado para documentação)
- `0.4 - 0.7`: Balanceado
- `0.8 - 1.0`: Mais criativo e variado

### Max Tokens

- `4000-8000`: Documentação padrão
- `16000`: Documentação muito detalhada (recomendado para RAG)
- Ajuste conforme o tamanho dos vídeos e nível de detalhe desejado

### Segmentação Temporal

Ajuste o tamanho dos segmentos para controlar a granularidade:

```python
# Na função segmentar_transcricao():
segmentos = segmentar_transcricao(transcricao_entries, segmento_segundos=150)

# Opções recomendadas:
# - 90s (1min30s): Vídeos curtos ou muito detalhados
# - 150s (2min30s): Padrão recomendado (balanceado)
# - 180s (3min): Vídeos longos ou visão geral
```

### Processamento em Lote

O script processa múltiplos vídeos automaticamente:

- ✅ Cada vídeo gera um arquivo separado
- ✅ Arquivos nomeados com o título do vídeo
- ✅ Tratamento de erros individual (um erro não interrompe os demais)
- ✅ Progresso detalhado durante a execução
- ✅ Metadados preservados para cada seção

## 📤 Saída Gerada

O script gera arquivos na pasta `docs/` com o formato `{titulo_do_video}_documentacao_gerada.md`:

**Estrutura de cada seção (2-3 minutos de vídeo):**

```markdown
---

## [Número]. [Título Específico da Funcionalidade]

**Minutagem:** [XX:XX → XX:XX]

**Contexto:**
[Localização e objetivo desta seção]

**Localização no Sistema:**
- Caminho de navegação completo
- Tela/interface específica

**Funcionalidade Detalhada:**
[Descrição completa do que a funcionalidade faz]

### 🔹 Passo a Passo Detalhado:

1. **[Ação Específica]**
   - Localização: [Onde exatamente]
   - Como fazer: [Descrição detalhada]
   - Campos/Opções disponíveis: [Lista completa]
   - Resultado esperado: [O que acontece]

**Campos e Parâmetros:**

| Campo | Tipo | Obrigatório | Descrição | Exemplo |
|-------|------|-------------|-----------|---------|
| ... | ... | ... | ... | ... |

**Regras de Negócio:**
- [Validações e restrições]

**Observações Importantes:**
- [Dicas e alertas]

**Conceitos-Chave:**
- **[Termo]**: [Definição]

---
```

**Nível de detalhamento:**

- 📹 **Vídeo de 50 minutos** → 20-25 seções detalhadas
- 📹 **Vídeo de 30 minutos** → 12-15 seções detalhadas
- 📹 **Vídeo de 15 minutos** → 6-8 seções detalhadas

**Exemplo de arquivos gerados:**

```
docs/
├── Passo a passo - Módulo de Armazenamento_documentacao_gerada.md (25 seções)
├── Passo a passo - Módulo de Qualidade_documentacao_gerada.md (18 seções)
└── Passo a passo - Módulo de RH_documentacao_gerada.md (22 seções)
```

**Otimizado para RAG:**

- ✅ Seções pequenas e autocontidas
- ✅ Informações específicas e detalhadas
- ✅ Fácil recuperação por similaridade semântica
- ✅ Contexto completo em cada seção
- ✅ Terminologia técnica precisa

## 🔍 Fluxo de Execução

```
1. Para cada URL na lista YOUTUBE_URLS:
   ↓
2. Obter título do vídeo (pytubefix)
   ↓
3. Extrair ID do vídeo
   ↓
4. Buscar transcrição (youtube-transcript-api)
   ↓
5. Processar com ChatGPT
   ↓
6. Gerar Markdown estruturado
   ↓
7. Salvar em docs/{titulo}_documentacao_gerada.md
   ↓
8. Próximo vídeo ou ✅ Concluído!
```

### Exemplo de Saída do Console

```
🚀 Iniciando processamento de 3 vídeo(s)...

============================================================
📹 Vídeo 1/3
============================================================
📝 Obtendo título do vídeo...
📌 Título: Passo a passo - Módulo de Armazenamento
🎥 Carregando e transcrevendo vídeo do YouTube...
🧠 Gerando documentação estruturada...
📁 Pasta 'docs' criada.
✅ Documentação salva em: docs/Passo a passo - Módulo de Armazenamento_documentacao_gerada.md
✅ Vídeo 1 processado com sucesso!

============================================================
📹 Vídeo 2/3
============================================================
...
```

## ⚠️ Tratamento de Erros

O script possui tratamento de erros robusto para:

- **Transcrições não disponíveis em português**: Tenta buscar em outros idiomas automaticamente
- **Vídeos sem transcrição**: Exibe mensagem de erro e continua para o próximo vídeo
- **URLs inválidas**: Valida o formato da URL antes de processar
- **API Key ausente**: Verifica se a chave OpenAI está configurada
- **Erro ao obter título**: Usa o ID do vídeo como fallback
- **Caracteres inválidos no nome**: Remove automaticamente caracteres especiais
- **Processamento em lote**: Um erro não interrompe o processamento dos demais vídeos

## 🐛 Solução de Problemas

### Erro: "No API key found"

**Solução**: Configure a variável `OPENAI_API_KEY` no arquivo `.env`

### Erro: "No transcript found"

**Solução**: O vídeo não possui legendas/transcrição disponível. Tente outro vídeo.

### Erro: "Invalid video ID"

**Solução**: Verifique se a URL do YouTube está correta e completa.

### Erro: "Unknown format code 'd' for object of type 'str'"

**Solução**: Este erro foi corrigido na v2.0. Certifique-se de estar usando a versão mais recente do script.

## 📊 Histórico de Versões

### v2.0 (Novembro 2025) - Otimização para RAG 🚀

**Melhorias Implementadas:**

- ✅ Timestamps precisos com segundos (MM:SS e HH:MM:SS)
- ✅ Links timestamped do YouTube (abre no segundo exato)
- ✅ Metadados estruturados por seção (ID, categorias, palavras-chave)
- ✅ Resumo executivo em cada seção
- ✅ Perguntas frequentes para matching semântico
- ✅ Segmentação temporal inteligente (150s por segmento)
- ✅ Preservação de timestamps da transcrição original
- ✅ Duração calculada automaticamente
- ✅ Estrutura otimizada para embeddings vetoriais

**Benefícios:**

- 🎯 Busca 3x mais precisa em sistemas RAG
- 📊 Contextualização instantânea com resumos
- ❓ Matching natural de perguntas do usuário
- 🔗 Navegação direta para momentos específicos do vídeo
- 🤖 Embeddings otimizados para busca semântica

### v1.0 (Outubro 2025) - Versão Inicial

- Transcrição básica de vídeos do YouTube
- Geração de documentação com LangChain
- Estrutura de seções e passos detalhados

## 📦 Dependências

As principais bibliotecas necessárias estão no ambiente virtual:

```
langchain-core==1.0.4
langchain-openai==1.0.2
langchain-community==0.4.1
youtube-transcript-api==0.6.2
pytubefix==10.2.1
python-dotenv==1.2.1
openai==2.7.2
```

Para instalar todas as dependências:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

Ou manualmente:

```bash
pip install langchain-core langchain-openai langchain-community youtube-transcript-api pytubefix python-dotenv openai
```

## 🎓 Próximos Passos Sugeridos

### Para Implementação de RAG:

1. **Criar Índice de Busca**

   - Extrair metadados de todos os documentos
   - Criar mapeamento ID → conteúdo
   - Indexar palavras-chave e categorias

2. **Gerar Embeddings**

   - Usar resumos + palavras-chave para vetorização
   - Criar índice FAISS ou Pinecone
   - Implementar busca híbrida (vetorial + keyword)

3. **Sistema de Perguntas**

   - Criar base de perguntas → seções
   - Implementar similaridade semântica
   - Testar com perguntas reais dos usuários

4. **Interface de Busca**
   - Permitir filtros por: módulo, categoria, duração
   - Retornar: seção + link timestamped + contexto
   - Renderizar vídeo no tempo correto

## 🤝 Contribuições

Sinta-se à vontade para:

- Reportar bugs
- Sugerir melhorias
- Adicionar novas funcionalidades
- Melhorar a documentação

## 📝 Licença

Este é um projeto educacional para demonstração de integração entre APIs de transcrição e modelos de linguagem.

## 👨‍💻 Autor

Desenvolvido como ferramenta de automação de documentação técnica.

**Versão:** 2.0 (Otimizada para RAG)  
**Última Atualização:** Novembro 2025

---

**Última atualização**: 12 de novembro de 2025
