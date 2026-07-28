import numpy as np


class RegimeDetector:
    """
    Compara (Phi, I) à distância do ponto fixo teórico do campo QWAN
    (Phi*=1, I*=0 — os mínimos do poço duplo bistável: campo
    totalmente ordenado, sem flutuação). A distância máxima
    teoricamente possível é derivada dos próprios limites do campo
    (Phi∈[0,1] e I∈[0,1] para um campo bistável em ±1), não de um
    limiar arbitrário escolhido a dedo: max_dev = sqrt(Phi*²+I_max²).

    Os cortes estável/crítico/caótico são os terços dessa distância
    MÁXIMA TEÓRICA — não de um histórico empírico nem de constantes
    arbitrárias como "I<0.3".
    """

    def __init__(self, window=30, phi_star=1.0, i_max=1.0):
        self.window = window
        self.phi_star = phi_star
        self.max_dev = np.sqrt(phi_star ** 2 + i_max ** 2)
        self.history = []

    def detect(self, Phi, I):

        self.history.append([Phi, I])
        if len(self.history) > self.window:
            self.history.pop(0)

        if len(self.history) < 10:
            return "warming"

        data = np.array(self.history)
        phi_vals, I_vals = data[:, 0], data[:, 1]

        deviation = np.sqrt((phi_vals - self.phi_star) ** 2 + I_vals ** 2)
        frac = deviation.mean() / self.max_dev

        if frac < 1 / 3:
            return "stable"

        if frac > 2 / 3:
            return "chaotic"

        return "critical"
