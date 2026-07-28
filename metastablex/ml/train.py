import torch
import torch.nn as nn
import torch.optim as optim

from metastablex.ml.features import metastable_features
from metastablex.ml.loss import metastable_loss
from metastablex.ml.dataset import TimeSeriesDataset
from metastablex.ml.model import MetastableXModel


class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(3, 16),
            nn.ReLU(),
            nn.Linear(16, 1)
        )

    def forward(self, x):
        return self.net(x).squeeze()


def train(series):

    x = torch.tensor(series, dtype=torch.float32)

    feats = metastable_features(x)

    model = SimpleModel()

    optimizer = optim.Adam(model.parameters(), lr=0.01)

    for epoch in range(50):

        optimizer.zero_grad()

        y_pred = model(feats)

        # 🔥 alvo = série original
        y_true = x

        loss, _ = metastable_loss(y_pred, y_true)

        loss.backward()
        optimizer.step()

    return model


def train_metastable_x_model(series, window=50, epochs=20, lr=1e-3):
    """
    Treina o MetastableXModel (encoder + GRU + cabeça de previsão e
    de regime), usando TimeSeriesDataset para gerar janelas
    deslizantes. É o modelo esperado por metastablex.ml.inference.predict
    (que espera (y_pred, regimes, z) = model(feats)) — sem esta
    função não havia nenhum caminho de treino que produzisse um
    modelo compatível com aquela assinatura.

    Cada janela é convertida em uma sequência de features
    (var, autocorr, entropia local) via metastable_features antes de
    entrar no modelo.
    """

    dataset = TimeSeriesDataset(series, window=window)

    model = MetastableXModel(input_dim=3)
    optimizer = optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        for x_window, y_next in dataset:

            feats = metastable_features(x_window).unsqueeze(0)  # (1, window, 3)

            y_pred, regimes, z = model(feats)

            loss, _ = metastable_loss(
                y_pred, y_next.unsqueeze(0), z=z, regimes=regimes
            )

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    return model
