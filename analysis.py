import numpy as np


def leastSquares(x, y, order=2):
    # Let y = Ap, where A = [[... x^2 x 1]] and p = [[c_2], [c_1], [c_0]]
    # So for y=mx+b, A = [[x 1]] and p = [[m], [b]]

    np.linalg.lstsq(x, y)
    coeffs = np.array()

    return coeffs
