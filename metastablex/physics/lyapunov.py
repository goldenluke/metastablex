import numpy as np


def lyapunov_exponent(ts):
    """
    Proxy de Lyapunov: λ ≈ log(Var(x)), conforme documentado no
    modelo QWAN. Não é o expoente de Lyapunov formal da teoria de
    sistemas dinâmicos (que exigiria reconstrução do espaço de fase
    e divergência de trajetórias vizinhas) — é uma aproximação de
    sensibilidade via variância da série.
    """
    ts = np.array(ts, dtype=float)

    var = np.var(ts)

    if var <= 0:
        return 0.0

    return float(np.log(var))
