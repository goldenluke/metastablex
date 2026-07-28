import torch
import torch.nn as nn


class NeuralODE(nn.Module):
    """
    Aprende o campo vetorial dx/dt = f(x) de uma série temporal
    e integra a trajetória resultante por Euler explícito.
    """

    def __init__(self, hidden=32):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(1, hidden),
            nn.Tanh(),
            nn.Linear(hidden, hidden),
            nn.Tanh(),
            nn.Linear(hidden, 1),
        )

    def dxdt(self, x):
        return self.net(x.unsqueeze(-1)).squeeze(-1)

    def forward(self, x0, steps=100, dt=0.01):

        x = x0
        trajectory = [x]

        for _ in range(steps):
            x = x + dt * self.dxdt(x)
            trajectory.append(x)

        return torch.stack(trajectory)


def simulate_neural_ode(x0, steps=100, dt=0.01, hidden=32):
    """
    Instancia um NeuralODE (não treinado) e integra a partir de x0.
    Útil para gerar/inspecionar trajetórias antes do treinamento.
    """

    model = NeuralODE(hidden=hidden)

    with torch.no_grad():
        x0 = torch.as_tensor(x0, dtype=torch.float32)
        trajectory = model(x0, steps=steps, dt=dt)

    return trajectory.numpy()
