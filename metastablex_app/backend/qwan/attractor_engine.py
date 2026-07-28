import numpy as np
from scipy import stats


class AttractorDetector:
    """
    Classifica o tipo de atrator com testes estatísticos, não
    limiares fixos:

    - fixed_point: teste F de razão de variâncias, calculado por
      dimensão espacial (nunca misturando variância espacial com
      temporal — um padrão espacialmente heterogêneo porém CONSTANTE
      NO TEMPO ainda é um ponto fixo). Para um sistema parado
      (posição constante no tempo + ruído iid), a variância TEMPORAL
      de cada coordenada deveria ser explicável inteiramente pela
      variância do ruído estimada por diferenciação (Var(diff) =
      2*Var(ruído) para ruído iid). H0: Var(nível) == Var(ruído); se
      não há evidência para rejeitar H0, é ponto fixo.

    - limit_cycle: PICO LOCAL de autocorrelação (de uma projeção
      escalar do estado — distância ao centro da janela) que excede
      a banda de significância padrão ±1.96/√N para alguma defasagem
      > 0. Exigir um pico local (sobe, desce, sobe de novo) — não
      apenas qualquer valor acima da banda — é o que distingue
      recorrência periódica genuína de mera correlação de curto
      alcance por suavidade (ex.: um passeio aleatório é suave e tem
      autocorrelação alta em lags pequenos sem ser periódico).

    - strange_attractor: nenhum dos testes acima se sustenta.
    """

    def __init__(self, max_history=50, alpha=0.05, confidence_z=1.96):
        self.max_history = max_history
        self.alpha = alpha
        self.confidence_z = confidence_z
        self.history = []

    def update(self, field):
        flat = np.asarray(field).flatten()
        self.history.append(flat)
        if len(self.history) > self.max_history:
            self.history.pop(0)

    def _is_fixed_point(self, data):

        # data: (n_time, n_dims). diffs ao longo do TEMPO, por dimensao
        diffs = data[1:] - data[:-1]

        # variancia TEMPORAL por dimensao (nao espacial): quanto cada
        # coordenada varia ao longo do tempo, ignorando o quanto as
        # coordenadas diferem ENTRE SI num mesmo instante
        temporal_var = np.mean(np.var(data, axis=0, ddof=1))
        noise_var = np.mean(np.var(diffs, axis=0, ddof=1)) / 2

        if noise_var <= 1e-300:
            return temporal_var <= 1e-300

        df1 = data.shape[0] - 1
        df2 = diffs.shape[0] - 1

        F = temporal_var / noise_var
        p_value = 1 - stats.f.cdf(F, df1, df2)

        # H0: Var(nível) == Var(ruído) — sem evidência contra H0,
        # não há dinâmica além do ruído
        return p_value > self.alpha

    def _is_periodic(self, data):

        n = len(data)

        scalar = np.linalg.norm(data - data.mean(axis=0), axis=1)
        scalar = scalar - scalar.mean()

        denom = np.sum(scalar ** 2)
        if denom == 0:
            return False

        band = self.confidence_z / np.sqrt(n)

        ac = np.array([
            np.sum(scalar[:-lag] * scalar[lag:]) / denom
            for lag in range(1, n // 2)
        ])

        for lag in range(1, len(ac) - 1):
            if ac[lag] > band and ac[lag] > ac[lag - 1] and ac[lag] >= ac[lag + 1]:
                return True

        return False

    def detect(self):

        if len(self.history) < 20:
            return "unknown"

        data = np.array(self.history)

        if self._is_fixed_point(data):
            return "fixed_point"

        if self._is_periodic(data):
            return "limit_cycle"

        return "strange_attractor"
