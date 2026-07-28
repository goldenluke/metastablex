import torch

# =========================
# ENTROPIA
# =========================
def entropy(x):
    if x.dim() == 1:
        x_norm = (x - x.min()) / (x.max() - x.min() + 1e-8)
        p = x_norm / (x_norm.sum() + 1e-8)
        return -torch.sum(p * torch.log(p + 1e-8))

    elif x.dim() == 2:
        x_norm = (x - x.min(dim=1, keepdim=True)[0]) / (
            x.max(dim=1, keepdim=True)[0] - x.min(dim=1, keepdim=True)[0] + 1e-8
        )
        p = x_norm / (x_norm.sum(dim=1, keepdim=True) + 1e-8)
        return -torch.mean(torch.sum(p * torch.log(p + 1e-8), dim=1))


# =========================
# COERÊNCIA (simples)
# =========================
def coherence(x):
    # suporta batch (B, T)
    if x.dim() == 1:
        if len(x) < 2:
            return torch.tensor(0.0, requires_grad=True)
        return torch.mean(x[1:] * x[:-1])

    elif x.dim() == 2:
        return torch.mean(x[:, 1:] * x[:, :-1])

# =========================
# ENERGIA LIVRE (Ginzburg-Landau / Allen-Cahn)
# =========================
def energy_free(x):
    """
    Energia livre de Ginzburg-Landau discreta, com fronteira periódica:

        E[x] = Σ_i [ 1/2 (x_{i+1} - x_i)^2 - 1/2 x_i^2 + 1/4 x_i^4 ]

    termo de difusão espacial + poço duplo biestável. O gradiente
    funcional desta energia é exatamente o lado direito da PDE
    documentada do modelo QWAN:

        dx/dt = -dE/dx = ∇²x + x - x³

    (ver compute_gradients em qwan/gradients.py, que usa
    autograd para obter -dE/dx a partir desta energia).
    """
    x_next = torch.roll(x, shifts=-1, dims=-1)
    gradient_term = 0.5 * (x_next - x) ** 2
    potential_term = -0.5 * x ** 2 + 0.25 * x ** 4

    density = gradient_term + potential_term

    if x.dim() == 1:
        return torch.sum(density)
    elif x.dim() == 2:
        return torch.mean(torch.sum(density, dim=1))


# =========================
# FUNCIONAL Φ
# =========================
def structural_energy(x, alpha=1.0, beta=1.0):
    H = entropy(x)
    I = coherence(x)
    E = energy_free(x)

    return E - alpha * H - beta * I
