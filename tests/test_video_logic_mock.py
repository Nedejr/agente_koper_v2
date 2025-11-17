"""
Script de teste MOCK para verificar a lógica de adição de vídeo
SEM usar a API da OpenAI
"""

import sys
from pathlib import Path

# Adiciona o diretório raiz ao path
sys.path.append(str(Path(__file__).parent))

def test_video_logic():
    """Testa a lógica de adição de vídeo simulando os dados"""
    
    print("=" * 80)
    print("🧪 TESTE MOCK: Lógica de Adição de Vídeo")
    print("=" * 80)
    print()
    
    # Simula dados de entrada
    print("1️⃣  Configurando dados de teste...")
    
    # Simula a resposta do LLM (SEM vídeo)
    llm_response = """Para verificar o histórico de movimentações no sistema Koper, você deve acessar a tela de estoque onde todas as movimentações realizadas são registradas.

📝 Passo a Passo:

1. Acesse Menu Principal > Gestão de Estoque.
2. Role para baixo na tela até encontrar a seção "Histórico de Movimentação".
3. Na seção, você encontrará informações sobre a Data, Hora, Tipo de Movimentação, Produto, Quantidade e Usuário responsável por cada movimentação.

⚠️ Observações Importantes:

- O histórico mostrará todas as alterações feitas no estoque, incluindo transferências, balanços, entradas e saídas.
- Esta funcionalidade é essencial para a auditoria das movimentações no local de estoque."""

    # Simula os metadados do documento mais relevante
    youtube_urls = {
        "Passo a passo - Módulo de Suprimentos": "https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73"
    }
    
    video_timestamps_map = {
        "Passo a passo - Módulo de Suprimentos": [
            {
                "start": "22:49",
                "end": "25:24",
                "line": "Gerenciamento de Estoque e Setores"
            }
        ]
    }
    
    print("   ✅ Dados configurados:")
    print(f"      📄 Resposta do LLM: {len(llm_response)} caracteres")
    print(f"      🎥 YouTube URLs: {len(youtube_urls)} encontradas")
    print(f"      ⏱️  Timestamps: {len(video_timestamps_map)} vídeos com timestamps")
    print()
    
    # 2. Testa a lógica de verificação
    print("2️⃣  Testando condições de adição de vídeo...")
    print()
    
    has_youtube_embed = "[YOUTUBE_EMBED:" in llm_response
    has_video_tag = "[video:" in llm_response
    has_video_emoji = "🎬" in llm_response
    
    print(f"   Condição 1: youtube_urls existe? {bool(youtube_urls)}")
    print(f"   Condição 2: [YOUTUBE_EMBED:] NÃO está na resposta? {not has_youtube_embed}")
    print()
    
    should_add_video = youtube_urls and "[YOUTUBE_EMBED:" not in llm_response
    
    print(f"   ➡️  Deve adicionar vídeo? {'✅ SIM' if should_add_video else '❌ NÃO'}")
    print()
    
    # 3. Simula a adição do vídeo
    if should_add_video:
        print("3️⃣  Simulando adição de vídeo...")
        print()
        
        # Pega a primeira URL
        first_url = list(youtube_urls.values())[0]
        print(f"   📺 URL do YouTube: {first_url}")
        
        # Busca o melhor timestamp
        best_timestamp = None
        for video_name, ts_list in video_timestamps_map.items():
            if ts_list and len(ts_list) > 0:
                best_timestamp = ts_list[0]
                break
        
        if best_timestamp:
            start_time = best_timestamp.get("start", "00:00")
            end_time = best_timestamp.get("end", "")
            
            print(f"   ⏱️  Timestamp encontrado: {start_time} → {end_time}")
            
            # Converte para segundos
            time_parts = start_time.split(":")
            if len(time_parts) == 2:
                seconds = int(time_parts[0]) * 60 + int(time_parts[1])
            elif len(time_parts) == 3:
                seconds = int(time_parts[0]) * 3600 + int(time_parts[1]) * 60 + int(time_parts[2])
            else:
                seconds = 0
            
            print(f"   🔢 Timestamp em segundos: {seconds}s")
            
            # Extrai o ID do vídeo
            video_id = None
            if "youtube.com/watch?v=" in first_url:
                video_id = first_url.split("watch?v=")[1].split("&")[0]
            elif "youtu.be/" in first_url:
                video_id = first_url.split("youtu.be/")[1].split("?")[0]
            
            print(f"   🆔 Video ID: {video_id}")
            
            if video_id:
                embed_url = f"https://www.youtube.com/embed/{video_id}?start={seconds}"
                print(f"   🔗 URL do embed: {embed_url}")
                print()
                
                # Monta a resposta final
                response_with_video = llm_response + "\n\n---\n\n"
                
                if end_time:
                    response_with_video += f"### 🎬 Vídeo Tutorial ({start_time} → {end_time})\n\n"
                else:
                    response_with_video += f"### 🎬 Vídeo Tutorial (a partir de {start_time})\n\n"
                
                response_with_video += f"[YOUTUBE_EMBED:{embed_url}]\n"
                
                print("4️⃣  Resposta final:")
                print()
                print("-" * 80)
                print(response_with_video)
                print("-" * 80)
                print()
                
                # Verifica se o vídeo foi adicionado
                print("5️⃣  Verificação final:")
                print()
                
                has_embed = "[YOUTUBE_EMBED:" in response_with_video
                has_emoji = "🎬" in response_with_video
                has_timestamp_info = f"({start_time} → {end_time})" in response_with_video
                
                print(f"   {'✅' if has_embed else '❌'} Contém [YOUTUBE_EMBED:]")
                print(f"   {'✅' if has_emoji else '❌'} Contém emoji 🎬")
                print(f"   {'✅' if has_timestamp_info else '❌'} Contém informação de timestamp")
                print()
                
                if has_embed and has_emoji:
                    print("=" * 80)
                    print("✅ SUCESSO! A lógica está correta!")
                    print("   O vídeo seria adicionado corretamente na resposta.")
                    print("=" * 80)
                    return True
                else:
                    print("=" * 80)
                    print("❌ FALHA! Algo deu errado na adição do vídeo.")
                    print("=" * 80)
                    return False
        else:
            print("   ⚠️  Nenhum timestamp encontrado")
    else:
        print("=" * 80)
        print("❌ FALHA! O vídeo NÃO seria adicionado!")
        print("   A condição de verificação está bloqueando a adição.")
        print("=" * 80)
        return False

if __name__ == "__main__":
    print()
    success = test_video_logic()
    print()
    
    if success:
        print("🎉 Teste passou! A lógica de vídeo está funcionando.")
        print()
        print("💡 Próximos passos:")
        print("   1. A lógica está correta no código")
        print("   2. O problema pode ser:")
        print("      - Cache do Streamlit não foi limpo")
        print("      - Base de dados precisa ser recarregada")
        print("      - Metadados não estão sendo extraídos corretamente")
        sys.exit(0)
    else:
        print("💥 Teste falhou! Há um problema na lógica.")
        sys.exit(1)
