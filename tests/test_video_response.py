"""
Script de teste para verificar se o vídeo está sendo adicionado corretamente na resposta
"""

import sys
from pathlib import Path

# Adiciona o diretório raiz ao path
sys.path.append(str(Path(__file__).parent))

from backend.vector_store import load_existing_vector_store
from backend.qa import ask_question


def test_video_in_response():
    """Testa se o vídeo aparece na resposta"""

    print("=" * 80)
    print("🧪 TESTE: Verificação de Vídeo na Resposta")
    print("=" * 80)
    print()

    # 1. Carrega o vector store
    print("1️⃣  Carregando vector store...")
    try:
        vector_store = load_existing_vector_store()
        print("   ✅ Vector store carregado com sucesso!")
    except Exception as e:
        print(f"   ❌ Erro ao carregar vector store: {e}")
        print("   💡 Execute o Streamlit primeiro para criar a base de dados")
        return False

    print()

    # 2. Faz a pergunta de teste
    print("2️⃣  Fazendo pergunta de teste...")
    query = "Como verifico o histórico de movimentações?"
    print(f"   📝 Pergunta: '{query}'")
    print()

    try:
        result = ask_question(
            query=query,
            vector_store=vector_store,
            model_name="gpt-5-nano",
            chat_history=None,
        )

        response = result["answer"]
        source_docs = result["source_documents"]

        print("3️⃣  Analisando resposta...")
        print()
        print("-" * 80)
        print("📄 RESPOSTA COMPLETA:")
        print("-" * 80)
        print(response)
        print("-" * 80)
        print()

        # 3. Verifica se há vídeo na resposta
        print("4️⃣  Verificações:")
        print()

        has_youtube_embed = "[YOUTUBE_EMBED:" in response
        has_video_emoji = "🎬" in response
        has_video_tag = "[video:" in response

        print(
            f"   {'✅' if has_youtube_embed else '❌'} Contém [YOUTUBE_EMBED:] - {has_youtube_embed}"
        )
        print(
            f"   {'✅' if has_video_emoji else '❌'} Contém emoji 🎬 - {has_video_emoji}"
        )
        print(
            f"   {'✅' if has_video_tag else '❌'} Contém tag [video:] - {has_video_tag}"
        )
        print()

        # 4. Extrai informações dos documentos recuperados
        print("5️⃣  Documentos recuperados (top 3):")
        print()
        for i, doc in enumerate(source_docs[:3], 1):
            source = doc.metadata.get("source", "Unknown")
            youtube_url = doc.metadata.get("youtube_url", "N/A")
            video_timestamps = doc.metadata.get("video_timestamps", [])

            print(f"   Documento {i}:")
            print(f"      📁 Source: {source}")
            print(f"      🎥 YouTube URL: {youtube_url}")
            print(f"      ⏱️  Timestamps: {len(video_timestamps)} encontrados")
            if video_timestamps:
                first_ts = video_timestamps[0]
                print(
                    f"         Primeiro: {first_ts.get('start', 'N/A')} → {first_ts.get('end', 'N/A')}"
                )
            print()

        # 5. Resultado final
        print("=" * 80)
        if has_youtube_embed:
            print("✅ SUCESSO! O vídeo está sendo adicionado corretamente!")
            print()

            # Extrai o URL do embed
            import re

            embed_match = re.search(r"\[YOUTUBE_EMBED:([^\]]+)\]", response)
            if embed_match:
                embed_url = embed_match.group(1)
                print(f"   🎬 URL do vídeo: {embed_url}")

                # Verifica se tem timestamp
                if "?start=" in embed_url:
                    start_seconds = embed_url.split("?start=")[1].split("&")[0]
                    minutes = int(start_seconds) // 60
                    seconds = int(start_seconds) % 60
                    print(f"   ⏱️  Timestamp: {minutes:02d}:{seconds:02d}")
                else:
                    print("   ⏱️  Timestamp: Não especificado (vídeo completo)")
        else:
            print("❌ FALHA! O vídeo NÃO está sendo adicionado!")
            print()
            print("   Possíveis causas:")
            print("   1. youtube_urls não está sendo passado corretamente")
            print("   2. A condição de verificação está bloqueando a adição")
            print("   3. Erro na extração de metadados dos documentos")
        print("=" * 80)

        return has_youtube_embed

    except Exception as e:
        print(f"   ❌ Erro ao processar pergunta: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    print()
    success = test_video_in_response()
    print()

    if success:
        print("🎉 Teste passou! O vídeo está funcionando corretamente.")
        sys.exit(0)
    else:
        print("💥 Teste falhou! O vídeo não está sendo adicionado.")
        sys.exit(1)
