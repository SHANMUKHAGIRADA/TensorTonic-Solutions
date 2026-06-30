import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    X = np.array(X, dtype=float)

    if X.ndim == 1:
        xmin = np.min(X)
        xmax = np.max(X)
        return (X - xmin) / (xmax - xmin + eps)

    elif X.ndim == 2:
        xmin = np.min(X, axis=axis, keepdims=True)
        xmax = np.max(X, axis=axis, keepdims=True)
        return (X - xmin) / (xmax - xmin + eps)
        