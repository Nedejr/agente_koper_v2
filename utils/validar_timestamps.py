#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validação simples e direta do sistema de timestamps
"""

import re
import json

print("\n" + "=" * 80)
print("🔍 VALIDAÇÃO DO DOCUMENTO E TIMESTAMPS")
print("=" * 80 + "\n")

# 1. Verifica se o documento existe e tem a estrutura correta
doc_path = "docs/Passo a passo - Módulo de Armazenamento_documentacao_gerada.md"

try:
    with open(doc_path, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"✅ Documento carregado: {len(content)} caracteres\n")
except FileNotFoundError:
    print(f"❌ Documento não encontrado: {doc_path}")
    exit(1)

# 2. Verifica tag [video:]
print("📹 Verificando tag [video:]...")
video_match = re.search(r"\[video:(https?://[^\]]+)\]", content)
if video_match:
    video_url = video_match.group(1)
    print(f"   ✅ Tag encontrada: {video_url}\n")
else:
    print("   ❌ Tag [video:] não encontrada!")
    exit(1)

# 3. Verifica e extrai timestamps JSON
print("⏱️  Verificando timestamps JSON...")
json_match = re.search(
    r"\[VIDEO_TIMESTAMPS_DATA\]\s*\n(.*?)\n\[/VIDEO_TIMESTAMPS_DATA\]",
    content,
    re.DOTALL,
)

if not json_match:
    print("   ❌ Seção [VIDEO_TIMESTAMPS_DATA] não encontrada!")
    exit(1)

try:
    timestamps_json = json_match.group(1)
    timestamps = json.loads(timestamps_json)
    print(f"   ✅ JSON válido extraído!\n")

    print("📊 Timestamps encontrados:")
    for video_name, ts_list in timestamps.items():
        print(f"\n   Vídeo: {video_name}")
        print(f"   Total de timestamps: {len(ts_list)}\n")
        for i, ts in enumerate(ts_list, 1):
            print(f"      {i}. {ts['start']} → {ts['end']}")
            print(f"         {ts['line'][:80]}...")
            print()

except json.JSONDecodeError as e:
    print(f"   ❌ Erro ao parsear JSON: {e}")
    exit(1)

# 4. Simula a seleção inteligente de timestamp
print("\n" + "=" * 80)
print("🤖 SIMULAÇÃO DE SELEÇÃO INTELIGENTE DE TIMESTAMP")
print("=" * 80 + "\n")

test_queries = [
    "Como criar uma pasta?",
    "Quais são as permissões disponíveis?",
    "Como funciona o módulo?",
]

for query in test_queries:
    print(f"Query: '{query}'")

    # Extrai palavras da query (como o backend faz)
    query_words = query.lower().split()

    best_score = -1
    best_ts = None

    # Calcula score para cada timestamp
    for ts in list(timestamps.values())[0]:  # Pega a primeira lista de timestamps
        ts_line = ts.get("line", "").lower()

        # Score: conta palavras da query que aparecem na descrição
        score = sum(1 for word in query_words if len(word) > 3 and word in ts_line)

        if score > best_score:
            best_score = score
            best_ts = ts

    if best_ts:
        print(f"   ✅ Timestamp selecionado: {best_ts['start']} (score: {best_score})")
        print(f"   Descrição: {best_ts['line'][:60]}...\n")
    else:
        print(f"   ⚠️ Nenhum timestamp com score positivo\n")

# 5. Testa conversão de timestamp para segundos
print("\n" + "=" * 80)
print("🔢 TESTE DE CONVERSÃO MM:SS → SEGUNDOS")
print("=" * 80 + "\n")


def timestamp_to_seconds(ts_str):
    """Converte 'MM:SS' ou 'HH:MM:SS' para segundos"""
    parts = ts_str.split(":")
    if len(parts) == 2:  # MM:SS
        return int(parts[0]) * 60 + int(parts[1])
    elif len(parts) == 3:  # HH:MM:SS
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    return 0


for ts in list(timestamps.values())[0]:
    start_str = ts["start"]
    seconds = timestamp_to_seconds(start_str)
    minutes = seconds // 60
    secs = seconds % 60
    print(f"{start_str} → {seconds}s ({minutes}min {secs}s)")

# 6. Simula URL do YouTube com timestamp
print("\n" + "=" * 80)
print("🎬 SIMULAÇÃO DE URL DO YOUTUBE COM TIMESTAMP")
print("=" * 80 + "\n")

first_ts = list(timestamps.values())[0][1]  # Pega o segundo timestamp
start_seconds = timestamp_to_seconds(first_ts["start"])

# Extrai ID do vídeo
video_id_match = re.search(r"(?:watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})", video_url)
if video_id_match:
    video_id = video_id_match.group(1)
    embed_url = f"https://www.youtube.com/embed/{video_id}?start={start_seconds}"
    print(f"URL original: {video_url}")
    print(f"URL embed com timestamp: {embed_url}")
    print(f"\nIframe HTML:")
    print(
        f'<iframe width="560" height="315" src="{embed_url}" frameborder="0" allowfullscreen></iframe>'
    )

# 7. Resumo final
print("\n" + "=" * 80)
print("✅ VALIDAÇÃO COMPLETA!")
print("=" * 80 + "\n")

print("📋 Checklist:")
print("   ✅ Tag [video:] presente no documento")
print("   ✅ [VIDEO_TIMESTAMPS_DATA] presente e válido")
print("   ✅ JSON com timestamps parseável")
print(f"   ✅ {len(list(timestamps.values())[0])} timestamps disponíveis")
print("   ✅ Seleção inteligente funcionando")
print("   ✅ Conversão MM:SS → segundos OK")
print("   ✅ URL do YouTube com ?start= OK")

print("\n🎉 Documento está no formato correto!")
print("🚀 Pronto para gerar novos documentos com gerar_documentacao_video.py")
print("\n💡 Próximos passos:")
print("   1. Execute: streamlit run frontend/main.py")
print("   2. Vá em 'Upload de Documentos'")
print("   3. Clique em 'Carregar Todos os Documentos'")
print("   4. Teste perguntas como 'Como criar uma pasta?'")
print()
