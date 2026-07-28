import numpy as np


def instability_index(serie):
    """
    Calcula um índice composto de instabilidade estrutural,
    comparando a primeira e a segunda metade da série.

    Combina:
    - tendência de variância (var_trend)
    - tendência de autocorrelação lag-1 (ac_trend)

    Retorna:
    -------
    dict com var_trend, ac_trend e score (média dos dois,
    quanto maior, mais instável o sistema).
    """

    serie = np.array(serie, dtype=float)
    serie = serie[~np.isnan(serie)]

    if len(serie) < 4:
        return {"var_trend": 0.0, "ac_trend": 0.0, "score": 0.0}

    mid = len(serie) // 2
    first, second = serie[:mid], serie[mid:]

    def autocorr(x):
        if len(x) < 2:
            return 0.0
        return np.corrcoef(x[:-1], x[1:])[0, 1]

    var_trend = np.var(second) - np.var(first)
    ac_trend = autocorr(second) - autocorr(first)

    score = (var_trend + ac_trend) / 2

    return {
        "var_trend": float(var_trend),
        "ac_trend": float(ac_trend),
        "score": float(score),
    }


def is_unstable(serie, var_threshold=0.1, ac_threshold=0.05):
    """
    Classifica a série como instável se a variância ou a
    autocorrelação estiverem crescendo além dos limiares.
    """

    metrics = instability_index(serie)

    return (
        metrics["var_trend"] > var_threshold
        or metrics["ac_trend"] > ac_threshold
    )
