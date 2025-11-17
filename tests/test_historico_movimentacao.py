#!/usr/bin/env python3
"""
Teste específico para validar a busca de "histórico de movimentação"
"""

import sys
from pathlib import Path

# Adiciona o diretório raiz ao path
sys.path.append(str(Path(__file__).parent))

from backend.qa import _find_relevant_timestamp_for_query


def test_historico_movimentacao():
    """Testa a busca específica para histórico de movimentação"""
    print("=" * 80)
    print("🧪 TESTE: Busca de 'Histórico de Movimentação'")
    print("=" * 80)

    # Mapa de timestamps REAL do documento
    video_timestamps_map = {
        "Passo a passo - Módulo de Suprimentos": [
            {
                "start": "00:00",
                "end": "02:34",
                "line": "Olá, neste vídeo iremos realizar uma apresentação completa do módulo de suplementos. Nosso primeiro ",
            },
            {
                "start": "02:32",
                "end": "05:07",
                "line": "Na lateral também tem o campo de data limite de entrega. Essa data é configurada por vocês dentro de",
            },
            {
                "start": "05:04",
                "end": "07:37",
                "line": "quantidade real e o código da nota. Então, como dito, na entrada, vamos verificar se o previsto foi ",
            },
            {
                "start": "07:35",
                "end": "10:10",
                "line": "utilizada, mas normalmente ela vai servir para uma referência de devolução de estoque, de uma entrad",
            },
            {
                "start": "10:08",
                "end": "12:42",
                "line": "Ao definir o local de origem, ele irá trazer uma referência dos produtos que estão dentro desse esto",
            },
            {
                "start": "12:40",
                "end": "15:13",
                "line": "demonstrativo, irei vincular com a categoria de pinturas, texturas e tintas e a subcategoria tintas.",
            },
            {
                "start": "15:11",
                "end": "17:46",
                "line": "quanto aos produtos já cadastrados, também conseguimos visualizar um campo bem importante, que são o",
            },
            {
                "start": "17:46",
                "end": "20:21",
                "line": "temos um pouco abaixo a opção de iniciar a transferência. Então, para produto, a transferência é ini",
            },
            {
                "start": "20:18",
                "end": "22:52",
                "line": "pode definir é a relação de período. O balanço ele pode ser feito a cada 7, 14, 21 ou 28 dias. Aqui,",
            },
            {
                "start": "22:49",
                "end": "25:24",
                "line": "transferência entre as obras, é criado um relacionamento entre elas. Basta selecionar a obra e adici",
            },
            {
                "start": "25:21",
                "end": "26:02",
                "line": "Outro ponto, unidade de medida, que é utilizada no produto em alguns outros campos do sistema. Basta",
            },
        ]
    }

    # Testes com diferentes variações da pergunta
    perguntas = [
        "como verifico historico de movimentação do estoque?",
        "Como verificar o histórico de movimentação?",
        "Onde vejo o histórico de movimentações?",
        "Como consultar histórico do estoque?",
        "Como vejo as movimentações do estoque?",
    ]

    print("\n📝 Testando com diferentes variações da pergunta:\n")

    for i, query in enumerate(perguntas, 1):
        result = _find_relevant_timestamp_for_query(query, video_timestamps_map)

        print(f"{i}. Pergunta: '{query}'")

        if result:
            print(f"   ⏱️  Timestamp: {result['start']} → {result['end']}")
            print(f"   📄 Trecho: {result['line'][:80]}...")

            # Valida se é o timestamp correto (seção 10: 22:49)
            expected_start = "22:49"
            if result["start"] == expected_start:
                print(f"   ✅ CORRETO! Encontrou o timestamp da seção 10")
            else:
                print(
                    f"   ❌ INCORRETO! Esperado {expected_start}, obtido {result['start']}"
                )
        else:
            print("   ❌ ERRO: Nenhum timestamp encontrado")

        print()

    # Análise detalhada da query principal
    print("=" * 80)
    print("🔍 ANÁLISE DETALHADA DA QUERY PRINCIPAL")
    print("=" * 80)

    query = "como verifico historico de movimentação do estoque?"
    print(f"\nQuery: '{query}'")
    print("\n1. Remoção de stopwords:")

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
        "os",
        "as",
        "dos",
        "das",
        "nos",
        "nas",
    ]
    words = query.lower().split()
    filtered = [
        w.rstrip("?!.,;:")
        for w in words
        if w.rstrip("?!.,;:") not in stopwords and len(w) > 2
    ]

    print(f"   Original: {words}")
    print(f"   Filtrado: {filtered}")

    print("\n2. Bigramas importantes:")
    bigramas = []
    for i in range(len(words) - 1):
        bigrama = f"{words[i]} {words[i+1]}"
        if words[i] not in stopwords or words[i + 1] not in stopwords:
            bigramas.append(bigrama)

    for bigrama in bigramas:
        print(f"   - '{bigrama}'")

    print("\n3. Análise de match com seção 10 (22:49):")
    secao_10_line = "transferência entre as obras, é criado um relacionamento entre elas. Basta selecionar a obra e adici"

    score = 0
    # Bigramas
    for bigrama in bigramas:
        if bigrama in secao_10_line.lower():
            score += 5
            print(f"   ✅ Bigrama '{bigrama}' encontrado (+5)")

    # Palavras individuais
    for word in filtered:
        if word in secao_10_line.lower():
            score += 1
            print(f"   ✅ Palavra '{word}' encontrada (+1)")

    print(f"\n   📊 Score final: {score}")

    # Mostra o que DEVERIA ter matched
    print("\n4. Por que a seção 10 DEVE ser a correta:")
    print("   A seção 10 do documento fala sobre:")
    print("   - ✅ Gerenciamento de Estoque e Setores")
    print("   - ✅ Histórico de Movimentação (EXATAMENTE o que perguntamos!)")
    print("   - ✅ Visualizar histórico de movimentação")
    print("   - ✅ Data, Hora, Tipo de Movimentação, Produto, Quantidade")
    print("\n   ⏱️  Timestamp correto: 22:49 → 25:24")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    print("\n🚀 INICIANDO TESTE ESPECÍFICO\n")

    try:
        test_historico_movimentacao()

        print("\n" + "=" * 80)
        print("✅ TESTE CONCLUÍDO")
        print("=" * 80)
        print("\n💡 Se o teste NÃO passou:")
        print("   1. O documento precisa ser reprocessado")
        print("   2. A seção 10 deve ter as palavras 'histórico' e 'movimentação'")
        print("   3. O timestamp no JSON deve estar correto (22:49)")
        print("\n💡 Próximo passo:")
        print("   Execute: streamlit run frontend/main.py")
        print("   Pergunta: 'como verifico historico de movimentação do estoque?'")
        print("   Esperado: Vídeo deve iniciar em 22:49\n")

    except Exception as e:
        print(f"\n❌ ERRO NO TESTE: {e}")
        import traceback

        traceback.print_exc()
