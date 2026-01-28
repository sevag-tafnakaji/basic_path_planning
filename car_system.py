
import numpy as np


def system(x: np.ndarray, u: np.ndarray):
    assert x.shape == (3, 1) and u.shape == (2, 1)
    np.array([u[0] * np.cos(x[2]), u[0] * np.sin(x[2]), u[1]])
