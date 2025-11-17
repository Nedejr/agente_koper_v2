"""
Script para verificar se os metadados estão corretos na base de dados
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from backend.vector_store import load_existing_vector_store

def test_metadata():
    """Verifica os metadados dos documentos na base"""
    
    print("=" * 80)
    print("🔍 TESTE: Verificação de Metadados na Base de Dados")
    print("=" * 80)
    print()
    
    try:
        print("1️⃣  Carregando vector store...")
        vector_store = load_existing_vector_store()
        print("   ✅ Vector store carregado!")
        print()
        
        print("2️⃣  Buscando documentos sobre 'movimentação estoque'...")
        docs = vector_store.similarity_search("movimentação estoque histórico", k=5)
        print(f"   ✅ Encontrados {len(docs)} documentos")
        print()
        
        print("3️⃣  Analisando metadados:")
        print()
        
        for i, doc in enumerate(docs, 1):
            print(f"   📄 Documento {i}:")
            print(f"      Source: {doc.metadata.get('source', 'N/A')}")
            print(f"      YouTube URL: {doc.metadata.get('youtube_url', '❌ NÃO ENCONTRADO')}")
            
            video_timestamps = doc.metadata.get('video_timestamps', [])
            print(f"      Video Timestamps: {len(video_timestamps)} encontrados")
            
            if video_timestamps:
                print(f"         ✅ Primeiro timestamp:")
                first_ts = video_timestamps[0]
                print(f"            Start: {first_ts.get('start', 'N/A')}")
                print(f"            End: {first_ts.get('end', 'N/A')}")
                print(f"            Line: {first_ts.get('line', 'N/A')[:50]}...")
            else:
                print(f"         ❌ Nenhum timestamp encontrado!")
            
            print(f"      Conteúdo (primeiros 100 chars): {doc.page_content[:100]}...")
            print()
        
        # Verifica se algum documento tem os metadados necessários
        has_youtube = any(doc.metadata.get('youtube_url') for doc in docs)
        has_timestamps = any(doc.metadata.get('video_timestamps') for doc in docs)
        
        print("=" * 80)
        print("4️⃣  Resultado:")
        print()
        print(f"   {'✅' if has_youtube else '❌'} Pelo menos um documento tem youtube_url")
        print(f"   {'✅' if has_timestamps else '❌'} Pelo menos um documento tem video_timestamps")
        print()
        
        if has_youtube and has_timestamps:
            print("✅ SUCESSO! Os metadados estão corretos na base!")
            print("   O problema deve estar no Streamlit ou no cache.")
            return True
        else:
            print("❌ PROBLEMA ENCONTRADO! Os metadados NÃO estão na base!")
            print()
            print("💡 Solução:")
            print("   1. Apague a pasta db/")
            print("   2. Reinicie o Streamlit")
            print("   3. Recarregue os documentos pela interface")
            return False
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print()
    success = test_metadata()
    print("=" * 80)
    print()
    sys.exit(0 if success else 1)
