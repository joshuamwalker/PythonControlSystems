# import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
# from random import seed
# from random import random
from plotting import plot_TD_FD

# seed(1)
# generate some random numbers
n = 100000  # Number of elements
fs = 1

whiteNoise = np.random.rand(n) - 0.5

randomWalk = np.zeros(n)
for idx, val in enumerate(randomWalk):
    randomWalk[idx] = whiteNoise[0] if idx == 0 else randomWalk[idx - 1] + whiteNoise[idx]

gaussNoise = np.random.randn(n)

gaussWalk = np.zeros(n)
for idx, val in enumerate(gaussWalk):
    gaussWalk[idx] = gaussNoise[0] if idx == 0 else gaussWalk[idx - 1] + gaussNoise[idx]

fig = plt.figure(figsize=(12, 6))
sz = np.array([2, 4])
whiteNoiseAx = plot_TD_FD(whiteNoise, fs=1, timeAx=fig.add_subplot(sz[0], sz[1], 1), freqAx=fig.add_subplot(sz[0], sz[1], 5), tLim=np.array([0, 100]), title="White Noise")
randomWalkAx = plot_TD_FD(randomWalk, fs=1, timeAx=fig.add_subplot(sz[0], sz[1], 2), freqAx=fig.add_subplot(sz[0], sz[1], 6), tLim=np.array([0, n]), title="Random Walk")
gaussNoiseAx = plot_TD_FD(gaussNoise, fs=1, timeAx=fig.add_subplot(sz[0], sz[1], 3), freqAx=fig.add_subplot(sz[0], sz[1], 7), tLim=np.array([0, 100]), title="Gaussian Noise")
gaussWalkAx = plot_TD_FD(gaussWalk, fs=1, timeAx=fig.add_subplot(sz[0], sz[1], 4), freqAx=fig.add_subplot(sz[0], sz[1], 8), tLim=np.array([0, n]), title="Gaussian Walk")

plt.show()
