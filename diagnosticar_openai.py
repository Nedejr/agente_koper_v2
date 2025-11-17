#!/usr/bin/env python3
"""
Script para diagnosticar e resolver problemas com a API OpenAI
"""

import os
import sys
from dotenv import load_dotenv


def verificar_configuracao():
    """Verifica a configuração da OpenAI API"""
    print("=" * 60)
    print("🔍 DIAGNÓSTICO DA CONFIGURAÇÃO OPENAI")
    print("=" * 60)

    # Carrega .env
    load_dotenv()

    # Verifica se a chave existe
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("❌ ERRO: OPENAI_API_KEY não encontrada no arquivo .env")
        print("\n📝 Solução:")
        print("1. Crie um arquivo .env na raiz do projeto")
        print("2. Adicione: OPENAI_API_KEY=sua_chave_aqui")
        print("3. Obtenha sua chave em: https://platform.openai.com/api-keys")
        return False

    # Verifica se a chave parece válida
    if api_key == "sua_chave_aqui" or len(api_key) < 20:
        print("❌ ERRO: OPENAI_API_KEY parece inválida")
        print(f"   Chave atual: {api_key[:10]}...")
        print("\n📝 Solução:")
        print("1. Acesse: https://platform.openai.com/api-keys")
        print("2. Crie uma nova chave ou copie uma existente")
        print("3. Cole no arquivo .env: OPENAI_API_KEY=sk-...")
        return False

    print(f"✅ Chave encontrada: {api_key[:10]}...{api_key[-4:]}")

    # Tenta fazer uma requisição simples
    print("\n🔄 Testando conexão com a API...")

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)

        # Tenta listar modelos disponíveis
        models = client.models.list()
        print("✅ Conexão bem-sucedida!")
        print(f"   {len(models.data)} modelos disponíveis")

        return True

    except Exception as e:
        error_msg = str(e)
        print(f"❌ ERRO ao conectar: {error_msg}")

        if "429" in error_msg or "quota" in error_msg.lower():
            print("\n🚨 ERRO DE QUOTA DETECTADO")
            print("\n📝 Soluções:")
            print(
                "1. Adicione créditos em: https://platform.openai.com/account/billing"
            )
            print("2. Valor mínimo: $5.00")
            print("3. Verifique uso em: https://platform.openai.com/usage")
            print("\n💡 Alternativas:")
            print("- Use embeddings locais (gratuito)")
            print("- Troque para gpt-3.5-turbo (mais barato)")
            print("- Processe documentos menores")

        elif "401" in error_msg or "invalid" in error_msg.lower():
            print("\n🚨 CHAVE DA API INVÁLIDA")
            print("\n📝 Soluções:")
            print("1. Verifique se copiou a chave completa")
            print("2. Crie uma nova chave em: https://platform.openai.com/api-keys")
            print("3. Atualize o arquivo .env")

        return False


def verificar_documentos():
    """Verifica tamanho dos documentos"""
    print("\n" + "=" * 60)
    print("📄 ANÁLISE DE DOCUMENTOS")
    print("=" * 60)

    docs_folder = "docs"

    if not os.path.exists(docs_folder):
        print(f"⚠️ Pasta '{docs_folder}' não encontrada")
        return

    try:
        import tiktoken

        encoding = tiktoken.encoding_for_model("gpt-4o-mini")
        has_tiktoken = True
    except ImportError:
        print("⚠️ tiktoken não instalado (usando estimativa)")
        has_tiktoken = False

    documentos = []
    for filename in os.listdir(docs_folder):
        if filename.endswith(".md"):
            filepath = os.path.join(docs_folder, filename)
            size_bytes = os.path.getsize(filepath)
            size_kb = size_bytes / 1024

            # Lê conteúdo para contar tokens
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            if has_tiktoken:
                tokens = len(encoding.encode(content))
            else:
                tokens = len(content) // 4  # Estimativa

            documentos.append(
                {"nome": filename, "tamanho_kb": size_kb, "tokens": tokens}
            )

    if not documentos:
        print("⚠️ Nenhum documento .md encontrado")
        return

    # Ordena por tamanho
    documentos.sort(key=lambda x: x["tokens"], reverse=True)

    print(f"\n📊 Total de documentos: {len(documentos)}")
    print("\n🔝 Top 5 maiores documentos:\n")

    for i, doc in enumerate(documentos[:5], 1):
        status = "⚠️" if doc["tokens"] > 250000 else "✅"
        print(f"{i}. {status} {doc['nome']}")
        print(f"   Tamanho: {doc['tamanho_kb']:.2f} KB")
        print(f"   Tokens: {doc['tokens']:,}")

        if doc["tokens"] > 250000:
            print(f"   ⚠️ MUITO GRANDE! Será dividido em partes")
        print()


def recomendar_solucao():
    """Recomenda a melhor solução baseada no diagnóstico"""
    print("\n" + "=" * 60)
    print("💡 RECOMENDAÇÕES")
    print("=" * 60)

    print("\n🎯 Solução Rápida (5 minutos):")
    print("   • Use embeddings locais (gratuito)")
    print("   • Comando: pip install sentence-transformers")
    print("   • Configure: USE_LOCAL_EMBEDDINGS=True no .env")
    print("   • Limitação: Não fará perguntas, só upload")

    print("\n🎯 Solução Completa (30 minutos):")
    print("   • Adicione créditos OpenAI ($5 mínimo)")
    print("   • Acesse: https://platform.openai.com/account/billing")
    print("   • Todas funcionalidades disponíveis")

    print("\n🎯 Solução Econômica:")
    print("   • Troque para gpt-3.5-turbo (mais barato)")
    print("   • Edite backend/config.py")
    print("   • Reduza CHUNK_SIZE no .env")

    print("\n" + "=" * 60)


def main():
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "DIAGNÓSTICO AGENTE KOPER V2" + " " * 20 + "║")
    print("╚" + "=" * 58 + "╝")
    print("\n")

    # Verifica configuração
    config_ok = verificar_configuracao()

    # Verifica documentos
    verificar_documentos()

    # Recomenda solução
    if not config_ok:
        recomendar_solucao()

    print("\n" + "=" * 60)
    print("🔗 LINKS ÚTEIS")
    print("=" * 60)
    print("• Billing: https://platform.openai.com/account/billing")
    print("• Usage: https://platform.openai.com/usage")
    print("• API Keys: https://platform.openai.com/api-keys")
    print("• Pricing: https://openai.com/pricing")
    print("=" * 60)
    print("\n✅ Diagnóstico concluído!\n")


if __name__ == "__main__":
    main()
