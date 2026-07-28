import numpy as np
from scipy import stats


class RegimeAlert:
    """
    Classifica o regime pelo SINAL do expoente de Lyapunov — o
    critério da própria teoria de sistemas dinâmicos, não um limiar
    escolhido a dedo: λ<0 é contração (estável), λ>0 é expansão
    (caótico), λ=0 é o limite crítico exato.

    A banda em torno de zero ("crítico") não é um intervalo fixo
    (ex.: ±0.01): é definida por um teste t de uma amostra sobre o
    histórico recente de λ, testando H0: média(λ) == 0. "Crítico"
    significa que a estimativa não é estatisticamente distinguível
    de zero, dada sua própria variabilidade amostral — a banda se
    alarga quando as estimativas são ruidosas e se estreita quando
    são consistentes, em vez de usar uma largura fixa.
    """

    def __init__(self, window=20, confidence=0.95):
        self.window = window
        self.alpha = 1 - confidence
        self.prev_regime = None
        self.lyap_history = []

    def classify(self, lyap, shannon, perm):

        if lyap is None:
            return "warming"

        self.lyap_history.append(lyap)
        if len(self.lyap_history) > self.window:
            self.lyap_history.pop(0)

        if len(self.lyap_history) < 5:
            # poucas amostras: usa apenas o sinal do valor mais recente
            if lyap > 0:
                return "chaotic"
            if lyap < 0:
                return "stable"
            return "critical"

        sample = np.array(self.lyap_history)
        std = sample.std(ddof=1)

        if std == 0:
            if sample.mean() > 0:
                return "chaotic"
            if sample.mean() < 0:
                return "stable"
            return "critical"

        # H0: média(λ) == 0 — testa se há evidência estatística de
        # que o sistema está genuinamente contraindo ou expandindo
        t_stat, p_value = stats.ttest_1samp(sample, popmean=0.0)

        if p_value > self.alpha:
            return "critical"

        return "chaotic" if t_stat > 0 else "stable"

    def update(self, lyap, shannon, perm):

        regime = self.classify(lyap, shannon, perm)

        alert = None

        if self.prev_regime and regime != self.prev_regime:
            alert = {
                "from": self.prev_regime,
                "to": regime,
                "type": f"{self.prev_regime}_to_{regime}",
            }

        self.prev_regime = regime

        return regime, alert
