import numpy as np
import matplotlib.pyplot as plt

from random import seed
from random import random

# whiteNoise = np.random.rand(20) - 0.5
# n = whiteNoise.shape
# print(whiteNoise[3,15])
# a = np.array([5, 2, 3, 7])
# print(a[0])
# print(whiteNoise[3:])
# import math
# print(math.ceil(5.5))
# # print(np.linspace(0,20-1,20))
# print(np.array([1, 2, 3, 4]./5))

    # Let y = Ap, where A = [[... x^2 x 1]] and p = [[c_2], [c_1], [c_0]]
    # So for y=mx+b, A = [[x 1]] and p = [[m], [b]]

# x = np.array([0, 1, 2, 3, 4, 5, 6])
# y = np.array([-1, 0.2, 0.9, 2.1, 4, 6, 10])
# A = np.vstack([x, np.ones(len(x))]).T
# print(A)
#
# m, c = np.linalg.lstsq(A, y, rcond=None)[0]
#
# import matplotlib.pyplot as plt
# _ = plt.plot(x, y, 'o', label='Original data', markersize=10)
# _ = plt.plot(x, m*x + c, 'r', label='Fitted line')
# _ = plt.legend()
# plt.show()

# n = 1000
# x = np.linspace(0, n, n, False)
# wn_td = np.random.rand(n) - 0.5  # White Noise, Time Domain
# y = np.cumsum(wn_td)  # Random Walk, Time Domain
# plt.plot(x, y)
# for order in [2, 4, 8, 16]:
#     poly = np.polynomial.Polynomial.fit(x, y, order).linspace(n, [min(x), max(x)])
#     plt.plot(poly[0], poly[1])
#
# plt.show()

A = [5., 3, 7.2]
print(A)
B = np.int(A)
print(B)
