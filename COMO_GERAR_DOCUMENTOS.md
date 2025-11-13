# 📹 Como Gerar Documentos com o Novo Padrão

Guia completo para criar documentação técnica estruturada com timestamps inteligentes para o Sistema Koper.

---

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Script gerar_documentacao_video.py](#script-gerar_documentacao_videopy)
- [Formato do Documento](#formato-do-documento)
- [Sistema de Timestamps](#sistema-de-timestamps)
- [Exemplos Práticos](#exemplos-práticos)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Visão Geral

O sistema utiliza documentos Markdown com estrutura específica que permite:

1. **Extração automática** de URLs do YouTube
2. **Timestamps inteligentes** vinculados a seções específicas
3. **Processamento otimizado** para busca semântica
4. **Embedamento de vídeos** nas respostas do chat

---

## 🔧 Script gerar_documentacao_video.py

### O que ele faz?

O script `gerar_documentacao_video.py` automatiza a criação de documentação a partir de vídeos do YouTube:

1. **Baixa a transcrição** do vídeo usando `youtube-transcript-api`
2. **Divide em chunks** baseados em timestamps
3. **Processa com GPT-4** para criar conteúdo estruturado
4. **Gera timestamps JSON** automaticamente
5. **Salva arquivo Markdown** pronto para usar

### Como Usar

1. **Execute o script**

```bash
python gerar_documentacao_video.py
```

2. **Insira a URL do vídeo** quando solicitado:

```
Digite a URL do vídeo do YouTube: https://www.youtube.com/watch?v=ABC123
```

3. **Aguarde o processamento**:

   - Download da transcrição
   - Divisão em seções
   - Geração de conteúdo com IA
   - Criação do arquivo Markdown

4. **Resultado**:
   - Arquivo salvo em `docs/`
   - Nome: `Passo a passo - [Título do Vídeo]_documentacao_gerada.md`

### Código Principal

```python
# gerar_documentacao_video.py

import os
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
import re
import json

def extrair_video_id(url):
    """Extrai o ID do vídeo da URL do YouTube"""
    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(pattern, url)
    return match.group(1) if match else None

def obter_transcricao(video_id):
    """Obtém a transcrição do vídeo"""
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt'])
    return transcript

def dividir_em_chunks(transcript, intervalo_segundos=60):
    """Divide a transcrição em chunks baseados em timestamps"""
    chunks = []
    current_chunk = {
        'start': transcript[0]['start'],
        'end': 0,
        'text': ''
    }

    for entry in transcript:
        if entry['start'] - current_chunk['start'] >= intervalo_segundos:
            current_chunk['end'] = entry['start']
            chunks.append(current_chunk)
            current_chunk = {
                'start': entry['start'],
                'end': 0,
                'text': ''
            }
        current_chunk['text'] += ' ' + entry['text']

    # Adiciona o último chunk
    current_chunk['end'] = transcript[-1]['start'] + transcript[-1]['duration']
    chunks.append(current_chunk)

    return chunks

def gerar_secao_com_ia(chunk, client, video_title):
    """Gera uma seção formatada usando GPT-4"""
    prompt = f"""
Você é um redator técnico especializado em documentação de sistemas.

Com base na transcrição abaixo, crie uma seção de documentação bem estruturada:

TÍTULO DO VÍDEO: {video_title}

TRANSCRIÇÃO (de {chunk['start']:.0f}s a {chunk['end']:.0f}s):
{chunk['text']}

INSTRUÇÕES:
1. Identifique o tema principal desta seção
2. Crie um título descritivo (## Título)
3. Escreva conteúdo detalhado em Markdown
4. Use formatação apropriada:
   - **Negrito** para termos importantes
   - `código` para nomes de botões/campos
   - Listas numeradas para procedimentos
   - Listas não-numeradas para características
5. Seja claro, objetivo e técnico
6. NÃO inclua timestamps no texto

FORMATO DE SAÍDA:
## Título da Seção

Conteúdo detalhado aqui...
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content

def gerar_timestamps_json(chunks, video_title):
    """Gera a seção JSON de timestamps"""
    timestamps = []

    for chunk in chunks:
        # Converte segundos para formato HH:MM:SS
        start_time = segundos_para_timestamp(chunk['start'])
        end_time = segundos_para_timestamp(chunk['end'])

        # Pega os primeiros 100 caracteres do texto como descrição
        description = chunk['text'].strip()[:100] + "..."

        timestamps.append({
            "start": start_time,
            "end": end_time,
            "line": description
        })

    return {video_title: timestamps}

def segundos_para_timestamp(segundos):
    """Converte segundos para formato HH:MM:SS"""
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segs = int(segundos % 60)

    if horas > 0:
        return f"{horas:02d}:{minutos:02d}:{segs:02d}"
    else:
        return f"{minutos:02d}:{segs:02d}"

def main():
    # Configuração
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Entrada do usuário
    video_url = input("Digite a URL do vídeo do YouTube: ")
    video_id = extrair_video_id(video_url)

    if not video_id:
        print("❌ URL inválida!")
        return

    print(f"✅ Video ID: {video_id}")

    # 1. Obter transcrição
    print("📥 Baixando transcrição...")
    transcript = obter_transcricao(video_id)
    print(f"✅ Transcrição obtida: {len(transcript)} entradas")

    # 2. Dividir em chunks
    print("✂️ Dividindo em seções...")
    chunks = dividir_em_chunks(transcript, intervalo_segundos=90)
    print(f"✅ Criadas {len(chunks)} seções")

    # 3. Gerar conteúdo
    print("🤖 Gerando documentação com IA...")
    video_title = f"Vídeo Tutorial {video_id}"

    markdown_content = f"# Passo a passo - {video_title}\n\n"
    markdown_content += f"[video:{video_url}]\n\n"

    for i, chunk in enumerate(chunks):
        print(f"   Processando seção {i+1}/{len(chunks)}...")
        secao = gerar_secao_com_ia(chunk, client, video_title)
        markdown_content += secao + "\n\n"

    # 4. Adicionar timestamps JSON
    timestamps_data = gerar_timestamps_json(chunks, video_title)
    markdown_content += "\n[VIDEO_TIMESTAMPS_DATA]\n"
    markdown_content += json.dumps(timestamps_data, ensure_ascii=False, indent=2)
    markdown_content += "\n[/VIDEO_TIMESTAMPS_DATA]\n"

    # 5. Salvar arquivo
    filename = f"docs/Passo a passo - {video_title}_documentacao_gerada.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"✅ Documentação gerada: {filename}")

if __name__ == "__main__":
    main()
```

---

## 📝 Formato do Documento

### Estrutura Básica

```markdown
# Título do Módulo

[video:URL_DO_YOUTUBE]

## Seção 1

Conteúdo detalhado da seção 1...

**Termo Importante**: Descrição

### Subseção 1.1

Mais detalhes...

## Seção 2

Conteúdo da seção 2...

[VIDEO_TIMESTAMPS_DATA]
{
"Nome do Vídeo": [
{"start": "00:00", "end": "01:30", "line": "Descrição da seção"},
{"start": "01:30", "end": "03:00", "line": "Outra descrição"}
]
}
[/VIDEO_TIMESTAMPS_DATA]
```

### Elementos Obrigatórios

1. **Título Principal** (`# Título`)
2. **Tag de Vídeo** (`[video:URL]`)
3. **Seções** (`## Seção`)
4. **Timestamps JSON** (`[VIDEO_TIMESTAMPS_DATA]`)

### Elementos Opcionais

- **Subseções** (`### Subseção`)
- **Imagens** (`![Alt](url)`)
- **Listas** (`- Item` ou `1. Item`)
- **Código** (`` `código` `` ou ` ```bloco``` `)
- **Tabelas** (formato Markdown)

---

## ⏱️ Sistema de Timestamps

### Formato JSON

```json
{
  "Nome do Vídeo": [
    {
      "start": "00:00",
      "end": "02:35",
      "line": "Introdução ao módulo de armazenamento e suas funcionalidades"
    },
    {
      "start": "02:35",
      "end": "04:56",
      "line": "Como criar e gerenciar pastas no sistema"
    }
  ]
}
```

### Campos Obrigatórios

- **start**: Timestamp inicial (formato `HH:MM:SS` ou `MM:SS`)
- **end**: Timestamp final (formato `HH:MM:SS` ou `MM:SS`)
- **line**: Descrição da seção (100-200 caracteres)

### Como Funciona a Seleção Inteligente

O sistema analisa a pergunta do usuário e seleciona o timestamp mais relevante:

1. **Extrai palavras-chave** da query (palavras com mais de 3 caracteres)
2. **Calcula score** para cada timestamp:
   - +1 ponto para cada palavra da query que aparece em `line`
   - +10 pontos se a descrição aparece no chunk mais relevante
3. **Seleciona** o timestamp com maior score
4. **Converte** para segundos e adiciona ao iframe do YouTube

**Exemplo:**

Query: "Como criar pasta?"

- Timestamp 1: "Introdução ao módulo" → Score: 0
- Timestamp 2: "Como criar e gerenciar pastas" → Score: 2
- **Selecionado**: Timestamp 2 ✅

---

## 💡 Exemplos Práticos

### Exemplo 1: Documento Completo

```markdown
# Passo a passo - Módulo de Armazenamento

[video:https://www.youtube.com/watch?v=ABC123]

## Introdução ao Módulo

O **Módulo de Armazenamento** é responsável por gerenciar toda a documentação digital da empresa. Nele você pode:

- Criar pastas organizadas
- Fazer upload de documentos
- Configurar permissões de acesso
- Buscar arquivos rapidamente

### Tela Principal

A tela principal apresenta:

1. **Barra de navegação** superior com menu
2. **Árvore de pastas** à esquerda
3. **Lista de documentos** ao centro
4. **Painel de detalhes** à direita

## Criando uma Nova Pasta

Para criar uma pasta, siga os passos:

1. Clique no botão `+ Nova Pasta` no canto superior
2. Digite o nome da pasta no campo `Nome`
3. Selecione a pasta pai (opcional)
4. Configure as permissões iniciais
5. Clique em `Salvar`

**Importante**: O nome da pasta não pode conter caracteres especiais.

## Configurando Permissões

As permissões controlam quem pode acessar cada pasta:

- **Leitura**: Visualizar documentos
- **Escrita**: Adicionar novos documentos
- **Edição**: Modificar documentos existentes
- **Exclusão**: Remover documentos
- **Admin**: Controle total

[VIDEO_TIMESTAMPS_DATA]
{
"Passo a passo - Módulo de Armazenamento": [
{
"start": "00:01",
"end": "02:37",
"line": "Introdução ao módulo de armazenamento e funcionalidades básicas do sistema"
},
{
"start": "02:35",
"end": "04:56",
"line": "Como criar e gerenciar pastas no sistema de armazenamento"
},
{
"start": "04:56",
"end": "07:20",
"line": "Configuração de permissões e controle de acesso aos documentos"
}
]
}
[/VIDEO_TIMESTAMPS_DATA]
```

### Exemplo 2: Adicionando Timestamps Manualmente

Se você tem um documento existente sem timestamps:

1. **Assista ao vídeo** e anote os momentos importantes
2. **Identifique as seções** principais
3. **Crie o JSON** com os timestamps
4. **Adicione ao final** do documento

```markdown
... (conteúdo existente) ...

[VIDEO_TIMESTAMPS_DATA]
{
"Nome do Seu Vídeo": [
{"start": "00:00", "end": "01:45", "line": "Primeira seção"},
{"start": "01:45", "end": "03:30", "line": "Segunda seção"},
{"start": "03:30", "end": "05:15", "line": "Terceira seção"}
]
}
[/VIDEO_TIMESTAMPS_DATA]
```

---

## 🔧 Troubleshooting

### Problema: Timestamps não aparecem

**Causa**: JSON malformado ou fora do padrão

**Solução**:

1. Valide o JSON em https://jsonlint.com/
2. Verifique se está entre `[VIDEO_TIMESTAMPS_DATA]` e `[/VIDEO_TIMESTAMPS_DATA]`
3. Confirme que os campos `start`, `end` e `line` existem

### Problema: Vídeo não aparece no chat

**Causa**: Tag `[video:URL]` ausente ou incorreta

**Solução**:

1. Adicione a tag no início do documento
2. Use o formato exato: `[video:https://www.youtube.com/watch?v=ID]`
3. Recarregue os documentos no sistema

### Problema: Timestamp errado selecionado

**Causa**: Descrição em `line` não corresponde ao conteúdo

**Solução**:

1. Melhore a descrição em `line` com palavras-chave relevantes
2. Use termos que o usuário provavelmente vai perguntar
3. Evite descrições genéricas como "Seção 1"

### Problema: Script gera erro de transcrição

**Causa**: Vídeo sem legendas ou legendas desabilitadas

**Solução**:

1. Verifique se o vídeo tem legendas em português
2. Tente com outro vídeo do mesmo canal
3. Crie a documentação manualmente

---

## 📚 Recursos Adicionais

### Documentação de Referência

- **Markdown Guide**: https://www.markdownguide.org/
- **YouTube Transcript API**: https://pypi.org/project/youtube-transcript-api/
- **LangChain Docs**: https://python.langchain.com/docs/

### Arquivos de Exemplo

Veja os documentos existentes em `docs/`:

- `Passo a passo - Módulo de Armazenamento_documentacao_gerada.md`
- `Passo a passo - Módulo de Compras_documentacao_gerada.md`
- `Passo a passo - Módulo de Engenharia_documentacao_gerada.md`

---

## ✅ Checklist de Qualidade

Antes de adicionar um documento ao sistema, verifique:

- [ ] Título descritivo no formato `# Passo a passo - [Nome]`
- [ ] Tag `[video:URL]` logo após o título
- [ ] Pelo menos 3 seções (`## Seção`)
- [ ] Formatação Markdown correta
- [ ] Timestamps JSON no final
- [ ] JSON válido (testar em jsonlint.com)
- [ ] Descrições em `line` com palavras-chave relevantes
- [ ] Arquivo salvo em `docs/` com nome descritivo

---

## 🚀 Próximos Passos

Após criar seu documento:

1. **Salve** em `docs/`
2. **Abra** o Assistente Koper
3. **Vá para** "Upload de Documentos"
4. **Clique** em "Carregar Todos os Documentos"
5. **Aguarde** o processamento
6. **Teste** fazendo perguntas no chat

---

**Dúvidas?** Consulte o [README.md](README.md) principal ou entre em contato com a equipe.
