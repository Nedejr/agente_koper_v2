# 🚨 GUIA DE SOLUÇÃO - Erro de Quota OpenAI

## 📋 Resumo do Problema

Você recebeu este erro ao tentar processar um documento:

```
Error code: 429 - You exceeded your current quota
```

**✅ Diagnóstico realizado:**

- Sua chave da API está válida e funcionando
- A conexão com OpenAI está OK
- Seus documentos têm tamanho apropriado
- **Problema:** Falta de créditos na conta OpenAI

---

## 🎯 Solução Recomendada: Adicionar Créditos

### Passo a Passo Completo

1. **Acesse o portal de billing da OpenAI:**

   ```
   https://platform.openai.com/account/billing
   ```

2. **Faça login com sua conta**

3. **Clique em "Add to credit balance"**

4. **Adicione créditos:**

   - Valor mínimo: **$5.00**
   - Valor recomendado para uso confortável: **$10.00**
   - Com $10 você processa aproximadamente **2.000 documentos**

5. **Configure método de pagamento:**

   - Cartão de crédito
   - PayPal (em algumas regiões)

6. **Aguarde processamento:**

   - Normalmente leva **5-15 minutos**
   - Você receberá um email de confirmação

7. **Teste novamente:**
   ```bash
   python diagnosticar_openai.py
   ```

---

## 💵 Custos e Estimativas

### Para Seu Projeto Atual

| Item                           | Quantidade | Custo Estimado |
| ------------------------------ | ---------- | -------------- |
| Processar 1 documento (100KB)  | 1x         | ~$0.005        |
| Processar seus 7 documentos    | 7x         | ~$0.035        |
| Fazer 100 perguntas ao sistema | 100x       | ~$0.10         |
| **Total mensal estimado**      | -          | **$1-3**       |

### Preços Oficiais (Jan 2024)

| Serviço                  | Custo             |
| ------------------------ | ----------------- |
| `gpt-4o-mini` (input)    | $0.15 / 1M tokens |
| `gpt-4o-mini` (output)   | $0.60 / 1M tokens |
| `text-embedding-3-small` | $0.02 / 1M tokens |
| `gpt-3.5-turbo` (input)  | $0.50 / 1M tokens |

**💡 Dica:** O modelo `gpt-4o-mini` que você está usando é o mais barato e eficiente para seu caso de uso.

---

## 🆓 Alternativa Gratuita: Embeddings Locais

Se você quer uma solução **100% gratuita** (sem OpenAI), siga estes passos:

### 1. Instalar Dependências

```bash
pip install sentence-transformers
```

### 2. Atualizar Configuração

Edite o arquivo `.env` e adicione:

```env
USE_LOCAL_EMBEDDINGS=True
```

### 3. Atualizar Código (backend/vector_store.py)

Adicione no início do arquivo:

```python
from langchain_huggingface import HuggingFaceEmbeddings

# Na função que cria embeddings, adicione:
if Config.USE_LOCAL_EMBEDDINGS:
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
else:
    embeddings = OpenAIEmbeddings()
```

### ⚠️ Limitações

- ✅ **Upload de documentos:** FUNCIONA
- ✅ **Busca semântica:** FUNCIONA
- ❌ **Fazer perguntas:** NÃO FUNCIONA (ainda precisa da OpenAI)
- 📊 **Performance:** ~80% da qualidade da OpenAI

---

## 🔧 Outras Otimizações (Opcional)

### Reduzir Custos Ainda Mais

Se você já tem créditos mas quer economizar:

#### 1. Usar gpt-3.5-turbo (mais barato)

Edite `backend/config.py`:

```python
DEFAULT_MODEL = "gpt-3.5-turbo"
```

**Economia:** ~70% mais barato
**Trade-off:** Respostas ligeiramente menos precisas

#### 2. Reduzir tamanho dos chunks

Edite `.env`:

```env
CHUNK_SIZE=500
CHUNK_OVERLAP=50
```

**Economia:** ~40% menos tokens
**Trade-off:** Pode perder algum contexto

#### 3. Reduzir quantidade de chunks recuperados

Edite `.env`:

```env
K_RETRIEVER=3
K_BEFORE_RERANK=6
```

**Economia:** ~50% menos tokens por pergunta
**Trade-off:** Respostas podem ser menos completas

---

## 📊 Monitoramento de Uso

### Painel de Controle OpenAI

Acesse regularmente para monitorar:

1. **Saldo atual:**

   ```
   https://platform.openai.com/account/billing/overview
   ```

2. **Uso diário/mensal:**

   ```
   https://platform.openai.com/usage
   ```

3. **Limites da conta:**
   ```
   https://platform.openai.com/account/limits
   ```

### Script de Monitoramento

Execute periodicamente:

```bash
python verificar_saldo.py
```

---

## 🚀 Próximos Passos

### Opção 1: Adicionar Créditos (RECOMENDADO)

✅ **Prós:**

- Solução completa e profissional
- Todas funcionalidades disponíveis
- Melhor qualidade de respostas
- Custo baixo ($1-3/mês)

❌ **Contras:**

- Requer cartão de crédito
- Não é gratuito

**➡️ Ação:**

1. Adicione $10 em https://platform.openai.com/account/billing
2. Aguarde 15 minutos
3. Execute: `python diagnosticar_openai.py`
4. Teste seu sistema

---

### Opção 2: Embeddings Locais

✅ **Prós:**

- 100% gratuito
- Funciona offline
- Sem limites de uso

❌ **Contras:**

- Não responde perguntas (só faz upload)
- Qualidade ~80% da OpenAI
- Requer mais memória RAM

**➡️ Ação:**

1. Execute: `pip install sentence-transformers`
2. Configure: `USE_LOCAL_EMBEDDINGS=True` no `.env`
3. Atualize `backend/vector_store.py` (código acima)
4. Reinicie: `./restart_streamlit.sh`

---

## 📞 Suporte e Links Úteis

### OpenAI

- **Billing:** https://platform.openai.com/account/billing
- **Usage:** https://platform.openai.com/usage
- **API Keys:** https://platform.openai.com/api-keys
- **Pricing:** https://openai.com/pricing
- **Status:** https://status.openai.com
- **Documentação:** https://platform.openai.com/docs

### Comunidade

- **Discord OpenAI:** https://discord.gg/openai
- **Forum:** https://community.openai.com

### Diagnóstico Local

```bash
# Verificar configuração
python diagnosticar_openai.py

# Verificar saldo
python verificar_saldo.py

# Ver logs do sistema
cat logs/app.log  # se existir
```

---

## ✅ Checklist de Resolução

Marque conforme for completando:

- [ ] Li e entendi o problema
- [ ] Escolhi uma solução (créditos ou local)
- [ ] Executei `python diagnosticar_openai.py`
- [ ] **Se escolhi créditos:**
  - [ ] Acessei o billing da OpenAI
  - [ ] Adicionei créditos ($5-10)
  - [ ] Aguardei confirmação por email
  - [ ] Testei novamente
- [ ] **Se escolhi embeddings locais:**
  - [ ] Instalei sentence-transformers
  - [ ] Configurei USE_LOCAL_EMBEDDINGS=True
  - [ ] Atualizei backend/vector_store.py
  - [ ] Reiniciei o sistema
- [ ] Sistema funcionando! 🎉

---

## 💡 Dica Final

**Para uso contínuo e profissional:**

- Adicione $10-20 de créditos
- Configure alertas de uso no painel OpenAI
- Monitore uso semanalmente
- Custo mensal típico: $1-5 para uso moderado

**Para testes e desenvolvimento:**

- Use embeddings locais
- Quando precisar testar perguntas, adicione $5
- Economize créditos fazendo perguntas específicas

---

**Criado em:** 17 de novembro de 2025
**Última atualização:** 17 de novembro de 2025
