import numpy as np


def to_numpy(serie):
    """
    Converte listas, pandas Series/DataFrame columns ou tensores
    em um np.ndarray de floats.
    """
    return np.asarray(serie, dtype=float)


def clean_series(serie):
    """
    Remove NaN e valores infinitos de uma série temporal.
    """
    serie = to_numpy(serie)
    return serie[np.isfinite(serie)]


def remove_outliers(serie, n_std=3):
    """
    Remove pontos que estejam a mais de `n_std` desvios padrão da média.
    """
    serie = clean_series(serie)

    if len(serie) == 0:
        return serie

    mean = np.mean(serie)
    std = np.std(serie)

    if std == 0:
        return serie

    mask = np.abs(serie - mean) <= n_std * std
    return serie[mask]
