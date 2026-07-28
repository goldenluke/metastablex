import numpy as np
from scipy.spatial.distance import pdist

def correlation_dimension(embedded):
    """
    Dimensão de correlação (Grassberger-Procaccia): ajusta a
    inclinação de log(C(r)) vs log(r) na região de escala.

    `r` é derivado da distribuição real de distâncias par-a-par
    (não de um intervalo absoluto fixo) — um intervalo fixo como
    [1e-3, 1] só funciona se os dados já estiverem nessa escala; para
    qualquer outra escala, C(r) fica zero nos r menores e log(0)
    quebra o ajuste. Bins com C(r) == 0 são descartados antes do
    ajuste linear.
    """

    if embedded is None or len(embedded) < 10:
        return None

    dists = pdist(embedded)
    dists = dists[dists > 0]

    if len(dists) < 2:
        return None

    r_vals = np.logspace(np.log10(dists.min()), np.log10(dists.max()), 20)

    C = np.array([np.sum(dists < r) / len(dists) for r in r_vals])

    mask = C > 0
    if mask.sum() < 2:
        return None

    log_r = np.log(r_vals[mask])
    log_C = np.log(C[mask])

    slope = np.polyfit(log_r, log_C, 1)[0]

    return slope
