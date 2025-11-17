import json


def parse_time(t: str) -> int:
    """Converte tempo MM:SS ou HH:MM:SS para segundos."""
    partes = list(map(int, t.split(":")))
    if len(partes) == 2:
        minutos, segundos = partes
        horas = 0
    else:
        horas, minutos, segundos = partes
    return horas * 3600 + minutos * 60 + segundos


def calcular_trecho(inicio: str, fim: str, url: str) -> dict:
    """
    Retorna:
    - minutagem formatada
    - duração em segundos
    - url ajustada com tempo inicial
    """
    t_inicio = parse_time(inicio)
    t_fim = parse_time(fim)
    duracao = t_fim - t_inicio

    # Gera a URL ajustada
    if "watch?v=" in url:
        # formato normal
        url_ajustada = f"{url}&t={t_inicio}s"
    else:
        # formato youtu.be
        url_ajustada = f"{url}?t={t_inicio}s"

    return {
        "minutagem": f"{inicio} → {fim}",
        "duracao_segundos": duracao,
        "url": url_ajustada,
    }


if __name__ == "__main__":
    # Testes adicionais
    # EXEMPLO:
    resultado = calcular_trecho(
        "25:00", "26:01", "https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73"
    )

    print(json.dumps(resultado, indent=4, ensure_ascii=False))
