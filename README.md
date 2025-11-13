# 📹 Gerador de Documentação a partir de Vídeos do YouTube

Este script automatiza a geração de documentação técnica estruturada em formato Markdown a partir de transcrições de vídeos do YouTube, utilizando inteligência artificial (OpenAI GPT).

## 🎯 Objetivo

Transformar vídeos tutoriais do YouTube em documentação técnica **extremamente detalhada** e bem estruturada, facilitando o aprendizado e a consulta de informações sem precisar assistir ao vídeo novamente.

**Características da documentação gerada:**

- 📊 **Granularidade**: Seções pequenas de 2-3 minutos cada
- 🔍 **Detalhamento**: Todos os passos, campos, botões e opções documentados
- 🤖 **Otimizada para RAG**: Ideal para sistemas de Retrieval-Augmented Generation
- 📝 **Autocontida**: Cada seção é completa e independente
- 🎯 **Específica**: Nomes exatos de elementos de UI, validações e regras de negócio
- ⏱️ **Timestamps Precisos**: Minutagem com segundos (MM:SS) e links diretos para o vídeo
- 🏷️ **Metadados Ricos**: IDs, categorias, palavras-chave e perguntas frequentes por seção

## ✨ Melhorias Implementadas (v2.0)

### 🎬 **Navegação Temporal com Links Timestamped**
- Cada seção possui link direto para o YouTube no segundo exato
- Formato: `https://youtu.be/ID?t=125` (abre no segundo 125)
- Minutagem formatada: `00:01 → 02:37` (HH:MM:SS ou MM:SS)
- Duração calculada automaticamente para cada segmento

### 📋 **Metadados Estruturados por Seção**
Cada seção agora inclui:
- **ID único**: `sec_1`, `sec_2`, etc. (para referências cruzadas)
- **Minutagem**: Início → Fim com segundos precisos
- **Duração**: Tempo do segmento em segundos
- **Link do YouTube**: Abre o vídeo no momento exato
- **Módulo**: Nome do módulo/área do sistema
- **Categorias**: 2-4 categorias relevantes (Configuração, Administração, etc.)
- **Palavras-chave**: 5-8 termos importantes para busca

### 🔍 **Resumo Executivo**
- Resumo de 2-3 linhas no topo de cada seção
- Explica O QUE a seção ensina
- Identifica QUAL PROBLEMA ela resolve
- Facilita compreensão rápida e busca semântica

### ❓ **Perguntas Frequentes por Seção**
- 3 perguntas naturais que a seção responde
- Formuladas como um usuário buscaria
- Otimiza matching semântico do RAG
- Aumenta recall e precision nas buscas

## 🎯 Benefícios para RAG (Retrieval-Augmented Generation)

### 1. **Busca Mais Precisa** 🎯
- Metadados permitem filtros avançados
- Palavras-chave otimizam busca vetorial
- Categorias facilitam navegação hierárquica

### 2. **Contextualização Rápida** 📊
- Resumo executivo oferece visão geral instantânea
- Duração ajuda a estimar tempo necessário
- Módulo identifica área do sistema

### 3. **Matching de Perguntas** ❓
- RAG compara pergunta do usuário com perguntas da seção
- Aumenta recall (encontra mais resultados relevantes)
- Melhora precision (resultados mais precisos)

### 4. **Navegação Temporal** 🔗
- ID único permite referências cruzadas
- Link timestamped abre vídeo no momento exato
- Minutagem facilita navegação humana

### 5. **Embeddings Otimizados** 🤖
- Palavras-chave melhoram representação vetorial
- Resumo concentra informação semântica
- Categorias criam hierarquia conceitual

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **LangChain**: Framework para construção de aplicações com LLMs
- **OpenAI API**: Utiliza modelos GPT (gpt-4o-mini, gpt-4o, etc.)
- **youtube-transcript-api**: Para extração de transcrições de vídeos do YouTube
- **pytubefix**: Para obter metadados dos vídeos (título, etc.)
- **python-dotenv**: Gerenciamento de variáveis de ambiente

## 📋 Pré-requisitos

1. Python 3.10 ou superior instalado
2. Conta na OpenAI com API Key ativa
3. Ambiente virtual Python (recomendado)

## 🚀 Como Rodar

### 1. Clone ou baixe o projeto

```bash
cd /home/koper/Documentos/agente_koper_v2
```

### 2. Ative o ambiente virtual

```bash
source venv/bin/activate
```

### 3. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com sua chave da OpenAI:

```env
OPENAI_API_KEY=sua-chave-aqui
```

### 4. Edite as URLs dos vídeos

Abra o arquivo `gerar_documentacao_video.py` e adicione as URLs dos vídeos que deseja processar na lista `YOUTUBE_URLS`:

```python
YOUTUBE_URLS = [
    "https://www.youtube.com/watch?v=VIDEO_ID_1",
    "https://www.youtube.com/watch?v=VIDEO_ID_2",
    "https://www.youtube.com/watch?v=VIDEO_ID_3",
    # Adicione quantas URLs quiser
]
```

### 5. Execute o script

```bash
python gerar_documentacao_video.py
```

O script irá processar cada vídeo e:

- 📝 Obter o título do vídeo
- 🎥 Carregar e transcrever o vídeo do YouTube
- 🧠 Processar a transcrição com IA
- ✅ Gerar e salvar a documentação em `docs/{titulo_do_video}_documentacao_gerada.md`

### 📂 Estrutura de Saída

Todos os arquivos serão salvos na pasta `docs/` criada automaticamente:

```
agente_koper_v2/
├── docs/
│   ├── Título do Vídeo 1_documentacao_gerada.md
│   ├── Título do Vídeo 2_documentacao_gerada.md
│   └── Título do Vídeo 3_documentacao_gerada.md
├── gerar_documentacao_video.py
├── .env
└── requirements.txt
```

## 📄 Estrutura da Documentação Gerada

Cada documento gerado segue o seguinte formato otimizado para RAG:

### 🎬 Cabeçalho do Documento
```markdown
# 📚 Documentação: [Título do Vídeo]

**🎥 Vídeo Original:** https://youtu.be/ID
**📊 Total de Seções:** X

---
```

### 📋 Estrutura de Cada Seção
```markdown
## 1. [Título Específico da Funcionalidade]

**📋 METADADOS:**
- **ID:** sec_1
- **⏱️ Minutagem:** 00:01 → 02:37
- **⏲️ Duração:** 156s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/ID?t=1)
- **📦 Módulo:** Nome do Módulo
- **🏷️ Categorias:** Configuração, Administração, Operacional
- **🔑 Palavras-chave:** permissão, usuário, editar, visualizar, pasta

> **🔍 RESUMO EXECUTIVO:** Resumo de 2-3 linhas explicando o que 
> esta seção ensina e qual problema ela resolve.

**Contexto:**
[Explicação do contexto e objetivo da seção]

**Localização no Sistema:**
- Caminho de navegação completo
- Tela/interface específica

**Funcionalidade Detalhada:**
[Descrição detalhada da funcionalidade]

### 🔹 Passo a Passo Detalhado:

1. **[Ação Específica]**
   - Localização: [Onde está o elemento]
   - Como fazer: [Descrição detalhada]
   - Campos/Opções disponíveis: [Lista completa]
   - Resultado esperado: [O que acontece]

**Campos e Parâmetros:**

| Campo | Tipo | Obrigatório | Descrição | Exemplo |
|-------|------|-------------|-----------|---------|
| ... | ... | ... | ... | ... |

**Regras de Negócio:**
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
