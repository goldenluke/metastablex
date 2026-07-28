from metastablex.rg.flow import rg_flow


class RegimeRG:
    """
    Operador de renormalização em espaço real: aplica repetidamente
    a transformação de coarse-graining R_b (fator de bloco `b`) e
    rastreia o fluxo das constantes de acoplamento efetivas (rho, g)
    até um ponto fixo ou até esgotar `max_iterations`.

    Ver metastablex.rg.flow.rg_flow para a transformação em si.
    """

    def __init__(self, b=2, max_iterations=10, tol=1e-3):
        self.b = b
        self.max_iterations = max_iterations
        self.tol = tol

    def flow(self, ts):
        return rg_flow(
            ts,
            b=self.b,
            max_iterations=self.max_iterations,
            tol=self.tol,
        )
