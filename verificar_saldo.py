#!/usr/bin/env python3
"""
Verifica saldo e uso da API OpenAI
"""

import os
from dotenv import load_dotenv

load_dotenv()

try:
    from openai import OpenAI

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    print("\n" + "=" * 60)
    print("💰 VERIFICAÇÃO DE SALDO E USO")
    print("=" * 60)

    print("\n📊 Para ver seu saldo e uso, acesse:")
    print("   • Saldo: https://platform.openai.com/account/billing/overview")
    print("   • Uso: https://platform.openai.com/usage")
    print("   • Limites: https://platform.openai.com/account/limits")

    print("\n💡 O erro 429 (quota exceeded) indica:")
    print("   ❌ Você não tem créditos suficientes")
    print("   ❌ Ou atingiu o limite de uso do período")

    print("\n✅ SOLUÇÃO IMEDIATA:")
    print("   1. Acesse: https://platform.openai.com/account/billing")
    print("   2. Clique em 'Add to credit balance'")
    print("   3. Adicione no mínimo $5.00")
    print("   4. Aguarde alguns minutos para processar")

    print("\n💵 CUSTOS ESTIMADOS para seu projeto:")
    print("   • Processar 1 documento (100KB): ~$0.005")
    print("   • Processar 7 documentos atuais: ~$0.035")
    print("   • Com $5.00 você processa ~1.000 documentos")

    print("\n🎯 ALTERNATIVAS GRATUITAS:")
    print("   • Use embeddings locais (sentence-transformers)")
    print("   • Configure: USE_LOCAL_EMBEDDINGS=True")
    print("   • Instale: pip install sentence-transformers")

    print("\n" + "=" * 60 + "\n")

except Exception as e:
    print(f"\n❌ Erro: {e}\n")
