import numpy as np
from metastablex.tensor.multiscale import coarse_grain


def effective_couplings(x):
    """
    Ajusta um processo AR(1) efetivo x_t = rho * x_{t-1} + ruído a
    uma série e retorna suas constantes de acoplamento:

    - rho: acoplamento de correlação de curto alcance (análogo à
      constante de acoplamento J de um modelo de spin — mede quanto
      um ponto "sente" seu vizinho)
    - g: energia de acoplamento residual (variância do ruído não
      explicado pelo acoplamento linear — análoga à temperatura
      efetiva do sistema renormalizado)
    """
    x = np.asarray(x, dtype=float)
    x = x - np.mean(x)

    if len(x) < 3 or np.std(x) == 0:
        return 0.0, 0.0

    x_prev, x_curr = x[:-1], x[1:]

    denom = np.sum(x_prev ** 2)
    rho = float(np.sum(x_prev * x_curr) / denom) if denom > 0 else 0.0

    residual = x_curr - rho * x_prev
    g = float(np.var(residual))

    return rho, g


def rg_transform(x, b=2):
    """
    A transformação de renormalização R_b propriamente dita: um
    passo de coarse-graining (bloco-agregação) por fator b. Aplicá-la
    repetidamente compõe o fluxo R_b ∘ R_b ∘ ... ∘ R_b.
    """
    return coarse_grain(x, b)


def rg_flow(ts, b=2, max_iterations=10, tol=1e-3):
    """
    Fluxo do grupo de renormalização em espaço real: itera a
    transformação de coarse-graining R_b sobre a série, extraindo em
    cada escala as constantes de acoplamento efetivas (rho, g).

    Ao contrário de apenas medir estatísticas em escalas
    pré-escolhidas da série original, cada iteração aqui é aplicada
    sobre o resultado da iteração anterior — é isso que faz da
    operação um fluxo (uma composição de transformações), e não uma
    tabela de métricas por escala.

    Para quando (rho, g) convergem dentro de `tol` (ponto fixo do
    fluxo) ou quando a série renormalizada fica curta demais para
    nova iteração.

    Retorna a trajetória do fluxo: lista de dicts com scale, rho, g
    e, no último ponto, fixed_point=True se convergiu.
    """
    x = np.asarray(ts, dtype=float)

    rho, g = effective_couplings(x)
    trajectory = [{"scale": 1, "rho": rho, "g": g}]

    scale = 1

    for _ in range(max_iterations):

        if len(x) < 2 * b:
            break

        x = rg_transform(x, b)
        scale *= b

        rho_new, g_new = effective_couplings(x)
        trajectory.append({"scale": scale, "rho": rho_new, "g": g_new})

        if abs(rho_new - rho) < tol and abs(g_new - g) < tol:
            trajectory[-1]["fixed_point"] = True
            break

        rho, g = rho_new, g_new

    return trajectory
