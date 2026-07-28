import numpy as np
from metastablex.physics.lyapunov import lyapunov_exponent

def compute_metrics(series):

    ts = np.array(series)

    returns = np.diff(ts)

    variance = np.var(returns)

    lyap = lyapunov_exponent(returns)

    hist, _ = np.histogram(returns, bins=20, density=True)
    p = hist + 1e-12
    entropy = -np.sum(p * np.log(p))

    complexity = entropy

    stability = 1/(1+variance+abs(lyap))

    return complexity, stability
