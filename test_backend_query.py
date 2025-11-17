"""
Teste direto do backend para verificar o documento e timestamp retornados
"""

import sys

sys.path.insert(0, "/home/koper/Documentos/agente_koper_v2")

from backend.vector_store import load_existing_vector_store
from backend.qa import ask_question


def test_query():
    print("=" * 80)
    print("TESTE DE QUERY NO BACKEND")
    print("=" * 80)

    # Carrega vector store
    print("\n📚 Carregando vector store...")
    vector_store = load_existing_vector_store()

    if not vector_store:
        print("❌ Erro: Vector store não encontrado!")
        return

    # Cria retriever
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    # Query de teste
    query = "como verifico historico de movimentação do estoque?"
    print(f"\n🔍 Query: {query}\n")

    # Busca documentos
    print("📄 Documentos recuperados:")
    print("-" * 80)
    docs = retriever.invoke(query)

    for i, doc in enumerate(docs, 1):
        print(f"\n{'='*80}")
        print(f"DOCUMENTO {i}")
        print(f"{'='*80}")
        print(f"Source: {doc.metadata.get('source', 'N/A')}")
        print(f"YouTube URL: {doc.metadata.get('youtube_url', 'N/A')}")  # DEBUG
        print(f"Metadados completos: {doc.metadata}")  # DEBUG
        print(f"\nConteúdo (primeiros 500 caracteres):")
        print(doc.page_content[:500])
        print("\n...")

        # Verifica se tem timestamps
        if "VIDEO_TIMESTAMPS_DATA" in doc.page_content:
            print("\n✅ Este documento contém VIDEO_TIMESTAMPS_DATA")
            # Extrai a parte do timestamp 22:49
            if "22:49" in doc.page_content:
                print("✅ Contém timestamp 22:49")
                # Mostra a linha do timestamp
                for line in doc.page_content.split("\n"):
                    if "22:49" in line:
                        print(f"   Linha: {line[:200]}")
            else:
                print("❌ NÃO contém timestamp 22:49")
        else:
            print("\n❌ Este documento NÃO contém VIDEO_TIMESTAMPS_DATA")

    # Agora testa a resposta completa
    print(f"\n{'='*80}")
    print("TESTE COM ASK_QUESTION")
    print(f"{'='*80}")

    response = ask_question(query, vector_store)

    print("\n📝 Resposta:")
    print(f"Tipo: {type(response)}")

    if isinstance(response, dict) and "answer" in response:
        answer_text = response["answer"]
        print(f"Tamanho da resposta: {len(answer_text)} caracteres")
        print(f"\nConteúdo (primeiros 1500 caracteres):")
        print(answer_text[:1500])

        # Verifica se tem embed de vídeo
        if "[YOUTUBE_EMBED:" in answer_text:
            print("\n✅ Resposta contém embed do YouTube")
            # Extrai o URL do embed
            import re

            embeds = re.findall(r"\[YOUTUBE_EMBED:([^\]]+)\]", answer_text)
            for embed_url in embeds:
                print(f"   URL: {embed_url}")
                if "t=1369" in embed_url or "t=22" in embed_url:
                    print("   ✅ URL contém timestamp correto (22:49 = 1369s)")
                else:
                    print(
                        f"   ⚠️  URL contém timestamp: {embed_url.split('t=')[-1] if 't=' in embed_url else 'nenhum'}"
                    )
        else:
            print("\n❌ Resposta NÃO contém embed do YouTube")
            print("   Verificando se há menção de vídeo...")
            if "vídeo" in answer_text.lower() or "video" in answer_text.lower():
                print("   ⚠️  Resposta menciona vídeo mas não tem embed")
    else:
        print(f"Conteúdo: {str(response)[:1000]}")


if __name__ == "__main__":
    test_query()
