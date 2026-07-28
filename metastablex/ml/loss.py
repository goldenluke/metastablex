import torch.nn.functional as F

def metastable_loss(y_pred, y_true, z=None, regimes=None):

    # achatar para 1D antes de comparar, para nao depender de squeeze()
    # deixar as formas compativeis "por sorte" (gera aviso de
    # broadcasting do PyTorch e resultado incorreto quando nao ficam)
    y_pred = y_pred.reshape(-1)
    y_true = y_true.reshape(-1)

    # 🔥 alinhar tamanhos
    min_len = min(len(y_pred), len(y_true))

    y_pred = y_pred[:min_len]
    y_true = y_true[:min_len]

    loss = F.mse_loss(y_pred, y_true)

    return loss, {"mse": loss.item()}
