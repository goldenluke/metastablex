import torch


def _gram_schmidt(vecs):
    """
    Ortonormaliza uma lista de vetores (Gram-Schmidt clássico).
    Vetores degenerados (norma zero após projeção) são substituídos
    por uma direção aleatória ortogonal às anteriores.
    """
    ortho = []

    for v in vecs:
        for u in ortho:
            v = v - torch.dot(v, u) * u

        norm = torch.norm(v)

        if norm.item() == 0:
            v = torch.randn_like(v)
            for u in ortho:
                v = v - torch.dot(v, u) * u
            norm = torch.norm(v)

        ortho.append(v / norm)

    return ortho


class LyapunovSpectrum:
    """
    Espectro de Lyapunov via algoritmo de Benettin et al. (1980):
    evolui `dim` vetores tangentes junto com a trajetória de
    referência e reortonormaliza (Gram-Schmidt) a cada passo.

    A reortonormalização é essencial — sem ela, todos os vetores
    tangentes convergem exponencialmente para a mesma direção (a de
    maior expansão), e o "espectro" retornado seria apenas `dim`
    cópias do maior expoente, não um espectro de verdade.

    Precisão numérica: os expoentes menores (mais contrativos) só
    convergem de forma confiável em float64. Em float32, ruído de
    arredondamento em direções que crescem mais rápido "vaza" para as
    direções contrativas e passa a dominá-las após poucas iterações
    (o vazamento cresce a uma taxa ~exp(λ_maior - λ_menor) por passo,
    independente de `eps`) — isso é uma limitação numérica conhecida
    do método de Benettin, não um bug de implementação. Para séries
    de expoentes muito espalhados, prefira `field` e `evolve_fn` em
    torch.float64.
    """

    def __init__(self, dim=3, eps=1e-6):
        self.dim = dim
        self.eps = eps
        self.initialized = False

    def init(self, field):
        self.ref = field.clone()

        vecs = []
        for _ in range(self.dim):
            v = torch.randn_like(field)
            vecs.append(v / torch.norm(v))

        vecs = _gram_schmidt(vecs)
        self.vecs = [v * self.eps for v in vecs]

        self.sums = [0.0] * self.dim
        self.steps = 0
        self.initialized = True

    def step(self, evolve_fn):

        if not self.initialized:
            return None

        ref_old = self.ref
        ref_new = evolve_fn(ref_old)

        # cada vetor tangente evolui a partir do MESMO estado de
        # referência anterior (não do já avançado), para medir a
        # divergência de exatamente um passo do mapa
        raw_vecs = [evolve_fn(ref_old + v) - ref_new for v in self.vecs]

        ortho = []
        norms = []

        for w in raw_vecs:
            for u in ortho:
                w = w - torch.dot(w, u) * u

            norm = torch.norm(w)
            norms.append(norm)
            ortho.append(w / norm if norm.item() > 0 else w)

        new_vecs = []

        for i, (norm, u) in enumerate(zip(norms, ortho)):
            if norm.item() == 0:
                new_vecs.append(self.vecs[i])
                continue

            self.sums[i] += torch.log(norm / self.eps).item()
            new_vecs.append(u * self.eps)

        self.ref = ref_new
        self.vecs = new_vecs
        self.steps += 1

        return [s / self.steps for s in self.sums]
