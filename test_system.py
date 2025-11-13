#!/usr/bin/env python3
"""
Script de teste para verificar se o sistema está funcionando
"""

import sys
from pathlib import Path

# Adiciona o diretório raiz ao path
sys.path.append(str(Path(__file__).parent))

print("🔍 Testando o sistema...")
print()

# Teste 1: Importações
print("1️⃣ Testando importações...")
try:
    from backend.processing import process_multiple_files
    from backend.vector_store import create_vector_store, load_existing_vector_store
    from backend.qa import ask_question

    print("   ✅ Todas as importações OK")
except Exception as e:
    print(f"   ❌ Erro nas importações: {e}")
    sys.exit(1)

# Teste 2: Verificar documentos
print()
print("2️⃣ Verificando documentos na pasta docs/...")
docs_path = Path(__file__).parent / "docs"
if docs_path.exists():
    doc_files = list(docs_path.glob("*.md"))
    print(f"   ✅ Encontrados {len(doc_files)} arquivos .md")
    for doc in doc_files[:3]:
        print(f"      - {doc.name}")
    if len(doc_files) > 3:
        print(f"      ... e mais {len(doc_files) - 3} arquivos")
else:
    print("   ❌ Pasta docs/ não encontrada")
    sys.exit(1)

# Teste 3: Tentar carregar vector store existente
print()
print("3️⃣ Verificando vector store existente...")
try:
    vector_store = load_existing_vector_store()
    if vector_store:
        collection = vector_store._collection
        total_docs = collection.count()
        print(f"   ✅ Vector store carregado com {total_docs} chunks")

        # Teste 4: Fazer uma pergunta de teste
        print()
        print("4️⃣ Testando pergunta...")
        result = ask_question("Como funciona o módulo de armazenamento?", vector_store)
        response = result["answer"]
        print(f"   ✅ Resposta gerada ({len(response)} caracteres)")
        print()
        print("   📝 Primeiros 200 caracteres da resposta:")
        print(f"   {response[:200]}...")

    else:
        print("   ⚠️  Nenhum vector store encontrado")
        print("   💡 Você precisa carregar os documentos primeiro")
except Exception as e:
    print(f"   ⚠️  Erro ao carregar vector store: {e}")
    print("   💡 Você precisa carregar os documentos primeiro")

print()
print("✅ Teste concluído!")
