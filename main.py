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
WhiteNoise = np.fft.fft(whiteNoise)

randomWalk = np.zeros(n)
for idx, val in enumerate(randomWalk):
    randomWalk[idx] = whiteNoise[0] if idx == 0 else randomWalk[idx - 1] + whiteNoise[idx]
RandomWalk = np.fft.fft(randomWalk)

fig = plt.figure(figsize=(12, 6))
sz = np.array([2, 2])
plot_TD_FD(whiteNoise, WhiteNoise, fs=1, timeAx=fig.add_subplot(sz[0], sz[1], 1), freqAx=fig.add_subplot(sz[0], sz[1], 3), pltShw=0, title="White Noise")
plot_TD_FD(randomWalk, RandomWalk, fs=1, timeAx=fig.add_subplot(sz[0], sz[1], 2), freqAx=fig.add_subplot(sz[0], sz[1], 4), tLim=np.array([0, 50]), pltShw=1, title="Random Walk")
