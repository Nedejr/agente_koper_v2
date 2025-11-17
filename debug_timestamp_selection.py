"""
Script para debugar a seleção de timestamps
"""

import json

# Simulação dos timestamps
timestamps_data = {
    "Passo a passo - Módulo de Suprimentos": [
        {
            "start": "07:35",
            "end": "10:10",
            "line": "utilizada, mas normalmente ela vai servir para uma referência de devolução de estoque, de uma entrad",
        },
        {
            "start": "22:49",
            "end": "25:24",
            "line": "Gerenciamento de Estoque e Setores - Visualizar Histórico de Movimentação - transferência entre as obras, é criado um relacionamento entre elas. Basta selecionar a obra e adicionar. Role para baixo até encontrar a seção Histórico de Movimentação.",
        },
    ]
}


def score_timestamp(query: str, ts_info: dict) -> int:
    """Calcula score de um timestamp"""
    query_lower = query.lower()
    line = ts_info.get("line", "").lower()

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
        "um",
        "uma",
        "uns",
        "umas",
        "ao",
        "aos",
        "à",
        "às",
        "pelo",
        "pela",
        "pelos",
        "pelas",
        "é",
        "são",
        "foi",
        "foram",
        "fazer",
        "eu",
        "tu",
        "ele",
        "ela",
        "nós",
        "vós",
        "eles",
        "elas",
        "que",
        "qual",
        "onde",
        "quando",
    ]

    # Extrai palavras-chave
    query_words = [
        w.strip().rstrip("?!.,;:")
        for w in query_lower.split()
        if w.strip().rstrip("?!.,;:") not in stopwords and len(w.strip()) > 2
    ]

    # Bigramas
    bigramas_importantes = []
    words_list = query_lower.split()
    for i in range(len(words_list) - 1):
        bigrama = f"{words_list[i]} {words_list[i+1]}"
        bigrama = bigrama.rstrip("?!.,;:")
        if words_list[i] not in stopwords or words_list[i + 1] not in stopwords:
            bigramas_importantes.append(bigrama)

    score = 0
    details = []

    # 1. Bigramas - PESO 5
    for bigrama in bigramas_importantes:
        if bigrama in line:
            score += 5
            details.append(f"  + Bigrama '{bigrama}': +5")

    # 2. Palavras individuais - PESO 1
    for word in query_words:
        if word in line:
            score += 1
            details.append(f"  + Palavra '{word}': +1")

    # 3. Todas palavras principais - PESO 10
    palavras_principais = [w for w in query_words if len(w) > 4]
    if palavras_principais and all(palavra in line for palavra in palavras_principais):
        score += 10
        details.append(
            f"  + Todas palavras principais ({', '.join(palavras_principais)}): +10"
        )

    # 4. Termos técnicos - PESO 8
    termos_tecnicos = [
        "histórico",
        "movimentação",
        "estoque",
        "transferência",
        "balanço",
        "entrada",
        "saída",
        "solicitação",
        "equipamento",
    ]
    for termo in termos_tecnicos:
        if termo in query_lower and termo in line:
            score += 8
            details.append(f"  + Termo técnico '{termo}': +8")

    return score, details


# Testes
queries = [
    "como verifico historico de movimentação do estoque?",
    "histórico de movimentação",
    "ver movimentação do estoque",
    "como verificar movimentações",
]

print("=" * 80)
print("ANÁLISE DE SELEÇÃO DE TIMESTAMPS")
print("=" * 80)

for query in queries:
    print(f"\n🔍 QUERY: {query}")
    print("-" * 80)

    for ts in timestamps_data["Passo a passo - Módulo de Suprimentos"]:
        score, details = score_timestamp(query, ts)
        print(f"\n⏱️  Timestamp: {ts['start']} → {ts['end']}")
        print(f"📝 Linha: {ts['line'][:100]}...")
        print(f"🎯 Score: {score}")
        if details:
            print("Detalhamento:")
            for detail in details:
                print(detail)

    print("\n" + "=" * 80)
