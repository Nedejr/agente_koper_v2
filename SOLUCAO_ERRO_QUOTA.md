# 🔧 Solução para Erro de Quota OpenAI (429)

## ❌ Erro Encontrado

```
Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details.'}}
```

Este erro ocorre quando:

- Você atingiu o limite de uso da sua conta OpenAI
- Sua conta não possui créditos suficientes
- Você está usando o plano gratuito (que tem limites muito restritos)

## ✅ Soluções

### Solução 1: Adicionar Créditos à Conta OpenAI (RECOMENDADO)

1. **Acesse o portal de billing:**
   - URL: https://platform.openai.com/account/billing
2. **Verifique seu saldo atual:**

   - Na seção "Credits balance"
   - Veja também o "Usage" (uso mensal)

3. **Adicione créditos:**

   - Clique em "Add to credit balance"
   - Valor mínimo: $5.00
   - Configure um método de pagamento

4. **Verifique seus limites:**
   - URL: https://platform.openai.com/account/limits
   - Confira o RPM (Requests Per Minute) e TPM (Tokens Per Minute)

### Solução 2: Otimizar o Uso de Tokens

O arquivo que você está processando é muito grande (101.19 KB). Vamos otimizar:

#### A) Dividir o Processamento

O código já possui uma função para dividir documentos grandes, mas podemos melhorá-la:

```python
# O código atual já divide documentos com mais de 250k tokens
# Mas podemos ser mais agressivos:
if token_count > 100000:  # Reduzir o limite
    content_parts = split_large_content(content, max_tokens=100000)
```

#### B) Usar Modelo Mais Barato

Edite o arquivo `backend/config.py`:

```python
# Trocar de gpt-4o-mini para gpt-3.5-turbo (mais barato)
DEFAULT_MODEL = "gpt-3.5-turbo"
```

#### C) Reduzir Chunk Size

Edite o arquivo `.env`:

```env
# Reduzir o tamanho dos chunks
CHUNK_SIZE=500  # Em vez de 1000
CHUNK_OVERLAP=50  # Em vez de 200
```

### Solução 3: Usar Embeddings Locais (GRATUITO)

Se você só precisa fazer upload de documentos (não fazer perguntas), pode usar embeddings locais:

1. **Instale o modelo local:**

```bash
pip install sentence-transformers
```

2. **Configure no `.env`:**

```env
USE_LOCAL_EMBEDDINGS=True
```

3. **Atualize `backend/vector_store.py`** para usar `HuggingFaceEmbeddings`:

```python
from langchain_huggingface import HuggingFaceEmbeddings

if Config.USE_LOCAL_EMBEDDINGS:
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
else:
    embeddings = OpenAIEmbeddings()
```

### Solução 4: Processar em Lotes Menores

Se você tem muitos documentos para processar:

1. **Processe um de cada vez** (não todos juntos)
2. **Espere alguns segundos entre cada processamento**
3. **Use a função de sleep:**

```python
import time

for doc in documentos:
    processar(doc)
    time.sleep(2)  # Espera 2 segundos entre cada
```

## 📊 Monitoramento de Uso

### Verificar Uso Atual

1. **Acesse:** https://platform.openai.com/usage
2. **Veja o consumo por:**
   - Dia
   - Modelo (gpt-4o-mini, gpt-3.5-turbo, etc.)
   - Tipo (embeddings, completions)

### Calcular Custos

**Preços aproximados (Jan 2024):**

- `gpt-4o-mini`: $0.15 / 1M tokens input, $0.60 / 1M tokens output
- `gpt-3.5-turbo`: $0.50 / 1M tokens input, $1.50 / 1M tokens output
- `text-embedding-ada-002`: $0.10 / 1M tokens

**Exemplo de cálculo:**

- Documento de 100KB ≈ 25.000 tokens
- Processar com gpt-4o-mini ≈ $0.004
- 100 documentos ≈ $0.40

## 🚨 Ações Imediatas

### Para Continuar Trabalhando AGORA:

1. **Opção A - Adicionar $5 de crédito** (15-30 minutos)
   - Mais rápido se você tem cartão de crédito
2. **Opção B - Usar embeddings locais** (5 minutos)

   ```bash
   pip install sentence-transformers
   # Editar .env: USE_LOCAL_EMBEDDINGS=True
   ```

3. **Opção C - Processar documento menor primeiro** (imediato)
   - Escolha um documento menor para testar
   - Depois adicione créditos e processe o grande

## 📝 Checklist

- [ ] Verificar saldo em https://platform.openai.com/account/billing
- [ ] Verificar chave da API está correta no `.env`
- [ ] Decidir qual solução usar
- [ ] Aplicar a solução escolhida
- [ ] Testar com documento pequeno primeiro
- [ ] Monitorar uso em https://platform.openai.com/usage

## 🔗 Links Úteis

- **Billing:** https://platform.openai.com/account/billing
- **Usage:** https://platform.openai.com/usage
- **API Keys:** https://platform.openai.com/api-keys
- **Limits:** https://platform.openai.com/account/limits
- **Pricing:** https://openai.com/pricing
- **Documentação de Erros:** https://platform.openai.com/docs/guides/error-codes/api-errors
