#!/usr/bin/env python3
"""
Script para reprocessar APENAS o documento de Suprimentos com as correções
"""

import sys
from pathlib import Path

# Adiciona o diretório raiz ao path
sys.path.append(str(Path(__file__).parent))

from backend.vector_store import delete_vector_store, create_vector_store
from backend.processing import process_multiple_files


class FileWrapper:
    """Wrapper para simular um objeto file-like"""

    def __init__(self, filepath):
        self.filepath = filepath
        self.name = filepath.name
        with open(filepath, "rb") as f:
            self._content = f.read()

    def read(self):
        return self._content


def reprocess_suprimentos():
    """Reprocessa o documento de Suprimentos"""
    print("=" * 80)
    print("🔄 REPROCESSANDO DOCUMENTO DE SUPRIMENTOS")
    print("=" * 80)

    # Caminho do documento
    doc_path = (
        Path(__file__).parent
        / "docs"
        / "Passo a passo - Módulo de Suprimentos_documentacao_gerada.md"
    )

    if not doc_path.exists():
        print(f"\n❌ ERRO: Documento não encontrado em {doc_path}")
        return False

    print(f"\n📄 Documento: {doc_path.name}")
    print(f"📐 Tamanho: {doc_path.stat().st_size / 1024:.2f} KB")

    try:
        # 1. LIMPAR base de dados antiga
        print("\n🗑️  Passo 1/3: Limpando base de dados antiga...")
        try:
            delete_vector_store()
            print("   ✅ Base de dados limpa")
        except Exception as e:
            print(f"   ⚠️  Aviso ao limpar: {e}")

        # 2. PROCESSAR documento
        print("\n📄 Passo 2/3: Processando documento...")
        file_obj = FileWrapper(doc_path)
        chunks = process_multiple_files([file_obj])
        print(f"   ✅ {len(chunks)} chunks criados")

        # 3. INDEXAR no vector store
        print("\n🔍 Passo 3/3: Indexando chunks no vector store...")
        vector_store = create_vector_store(chunks)
        print("   ✅ Chunks indexados com sucesso")

        # 4. VALIDAR
        print("\n✅ VALIDAÇÃO:")
        collection = vector_store._collection
        total_docs = collection.count()
        print(f"   📊 Total de chunks indexados: {total_docs}")

        # Busca usando o retriever (que usa os embeddings corretos do OpenAI)
        print(f"\n🔍 Testando busca por 'histórico de movimentação estoque':")
        try:
            retriever = vector_store.as_retriever(search_kwargs={"k": 3})
            docs = retriever.invoke("histórico de movimentação estoque")

            if docs:
                for i, doc in enumerate(docs, 1):
                    print(f"\n   Resultado {i}:")
                    content_preview = doc.page_content[:150].replace("\n", " ")
                    print(f"   {content_preview}...")
            else:
                print("   ⚠️  Nenhum resultado encontrado")
        except Exception as e:
            print(f"   ⚠️  Erro na busca: {e}")

        return True

    except Exception as e:
        print(f"\n❌ ERRO durante o reprocessamento: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("\n🚀 INICIANDO REPROCESSAMENTO\n")

    success = reprocess_suprimentos()

    print("\n" + "=" * 80)
    if success:
        print("✅ REPROCESSAMENTO CONCLUÍDO COM SUCESSO!")
        print("=" * 80)
        print("\n💡 Próximos passos:")
        print("   1. Inicie o Streamlit: streamlit run frontend/main.py")
        print(
            "   2. Faça a pergunta: 'como verifico historico de movimentação do estoque?'"
        )
        print("   3. ✅ Vídeo deve iniciar em 22:49")
        print("   4. ✅ Resposta deve mencionar a seção 'Histórico de Movimentação'\n")
    else:
        print("❌ REPROCESSAMENTO FALHOU")
        print("=" * 80)
        print("\n💡 Tente:")
        print("   1. Verificar se o documento existe em docs/")
        print("   2. Verificar permissões de escrita no diretório db/")
        print("   3. Executar novamente o script\n")
