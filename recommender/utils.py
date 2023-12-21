import numpy as np


def normalize_score(val: float):
    return (val - 3) ** 3


def l2(a, b):
    return np.sqrt(np.square(a - b).sum())
