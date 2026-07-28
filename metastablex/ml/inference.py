import torch

from .features import metastable_features


def predict(model, x):
    feats = metastable_features(x)     # (seq_len, 3)
    feats = feats.unsqueeze(0)         # (batch=1, seq_len, 3)

    y_pred, regimes, z = model(feats)

    return {
        "prediction": y_pred.item(),
        "regime_probs": regimes.detach().numpy(),
        "instability": torch.var(z).item()
    }
