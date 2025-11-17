#!/usr/bin/env python3
"""
Script de teste para validar as correções de timestamp e tamanho do vídeo
"""

import sys
from pathlib import Path

# Adiciona o diretório raiz ao path
sys.path.append(str(Path(__file__).parent))

from backend.qa import _find_relevant_timestamp_for_query


def test_timestamp_relevance():
    """Testa a busca de timestamp relevante"""
    print("=" * 60)
    print("🧪 TESTE 1: Busca de Timestamp Relevante")
    print("=" * 60)

    # Exemplo de mapa de timestamps (simulando dados reais)
    video_timestamps_map = {
        "Passo a passo - Módulo de Suprimentos": [
            {
                "start": "00:00",
                "end": "02:34",
                "line": "Módulo de Suplementos - Aba de Solicitações",
            },
            {
                "start": "02:32",
                "end": "05:07",
                "line": "Configuração de Data Limite de Entrega e Comentários",
            },
            {
                "start": "05:04",
                "end": "07:37",
                "line": "Registro de Entradas e Tratamento de Divergências",
            },
            {
                "start": "07:35",
                "end": "10:10",
                "line": "Registro de Entrada e Consumo de Produtos no Estoque",
            },
            {
                "start": "10:08",
                "end": "12:42",
                "line": "Solicitação e Transferência de Produtos",
            },
            {
                "start": "22:49",
                "end": "25:24",
                "line": "Gerenciamento de Estoque e Setores - Histórico de Movimentação",
            },
        ]
    }

    # Teste 1: Pergunta sobre histórico
    print("\n📝 Teste 1.1: Pergunta sobre histórico de movimentação")
    query1 = "Como verifico o histórico de movimentação nos locais de estoque?"
    result1 = _find_relevant_timestamp_for_query(query1, video_timestamps_map)

    print(f"   Pergunta: {query1}")
    if result1:
        print(f"   ✅ Timestamp encontrado: {result1['start']} → {result1['end']}")
        print(f"   📄 Descrição: {result1['line']}")

        # Valida se é o timestamp correto (deve ser o da seção 10)
        expected_start = "22:49"
        if result1["start"] == expected_start:
            print(f"   ✅ PASSOU: Timestamp correto ({expected_start})")
        else:
            print(f"   ❌ FALHOU: Esperado {expected_start}, obtido {result1['start']}")
    else:
        print("   ❌ FALHOU: Nenhum timestamp encontrado")

    # Teste 2: Pergunta sobre solicitação
    print("\n📝 Teste 1.2: Pergunta sobre solicitações")
    query2 = "Como criar uma solicitação de produto?"
    result2 = _find_relevant_timestamp_for_query(query2, video_timestamps_map)

    print(f"   Pergunta: {query2}")
    if result2:
        print(f"   ✅ Timestamp encontrado: {result2['start']} → {result2['end']}")
        print(f"   📄 Descrição: {result2['line']}")

        # Valida se é o timestamp correto (deve ser o primeiro)
        expected_start = "00:00"
        if result2["start"] == expected_start:
            print(f"   ✅ PASSOU: Timestamp correto ({expected_start})")
        else:
            print(f"   ❌ FALHOU: Esperado {expected_start}, obtido {result2['start']}")
    else:
        print("   ❌ FALHOU: Nenhum timestamp encontrado")

    # Teste 3: Pergunta sobre transferência
    print("\n📝 Teste 1.3: Pergunta sobre transferência")
    query3 = "Como transferir produtos entre estoques?"
    result3 = _find_relevant_timestamp_for_query(query3, video_timestamps_map)

    print(f"   Pergunta: {query3}")
    if result3:
        print(f"   ✅ Timestamp encontrado: {result3['start']} → {result3['end']}")
        print(f"   📄 Descrição: {result3['line']}")

        # Valida se é o timestamp correto (deve ser seção 5)
        expected_start = "10:08"
        if result3["start"] == expected_start:
            print(f"   ✅ PASSOU: Timestamp correto ({expected_start})")
        else:
            print(f"   ❌ FALHOU: Esperado {expected_start}, obtido {result3['start']}")
    else:
        print("   ❌ FALHOU: Nenhum timestamp encontrado")

    print("\n" + "=" * 60)


def test_stopwords_removal():
    """Testa a remoção de stopwords"""
    print("\n" + "=" * 60)
    print("🧪 TESTE 2: Remoção de Stopwords")
    print("=" * 60)

    test_queries = [
        "Como verifico o histórico de movimentação?",
        "O que fazer para transferir produtos?",
        "Onde eu encontro as solicitações?",
    ]

    stopwords = [
        "como",
        "o",
        "a",
        "de",
        "em",
        "para",
        "do",
        "da",
        "no",
        "na",
        "que",
        "fazer",
        "onde",
        "eu",
    ]

    for query in test_queries:
        words = query.lower().split()
        filtered = [w for w in words if w not in stopwords]

        print(f"\n📝 Query: {query}")
        print(f"   Antes: {words}")
        print(f"   Depois: {filtered}")
        print(f"   ✅ Removidas: {set(words) - set(filtered)}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    print("\n🚀 INICIANDO TESTES DE CORREÇÃO\n")

    try:
        test_timestamp_relevance()
        test_stopwords_removal()

        print("\n" + "=" * 60)
        print("✅ TODOS OS TESTES CONCLUÍDOS")
        print("=" * 60)
        print("\n💡 Próximos passos:")
        print("   1. Inicie o Streamlit: streamlit run frontend/main.py")
        print(
            "   2. Faça a pergunta: 'Como verifico o histórico de movimentação nos locais de estoque?'"
        )
        print("   3. Verifique se o vídeo inicia no timestamp correto (22:49)")
        print("   4. Confirme se o tamanho do player está adequado (max 640px)\n")

    except Exception as e:
        print(f"\n❌ ERRO NOS TESTES: {e}")
        import traceback

        traceback.print_exc()
