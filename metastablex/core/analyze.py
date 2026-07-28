import numpy as np
from metastablex.physics.lyapunov import lyapunov_exponent

def analyze_timeseries(ts):

    ts = np.array(ts)

    returns = np.diff(ts)

    result = {}

    result["mean"] = np.mean(ts)
    result["std"] = np.std(ts)
    result["volatility"] = np.std(returns)
    result["lyapunov"] = lyapunov_exponent(returns)

    return result
