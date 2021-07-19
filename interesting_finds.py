import numpy as np
import matplotlib.pyplot as plt
from plotting import plot_TD_FD, poly_fit_plot


def polyfit_whitenoise_vs_randomwalk():
    # Found that integrating a polyfit on white noise
    # produces a very similar result to performing the polyfit
    # on the integrated white noise (random walk)
    n = 100000  # Number of elements
    fs = 1
    t = np.linspace(0, n/fs, n, False)  # Do not include endpoint

    whiteNoise = np.random.rand(n) - 0.5

    randomWalk = np.zeros(n)
    for idx, val in enumerate(randomWalk):
        randomWalk[idx] = whiteNoise[0] if idx == 0 else randomWalk[idx - 1] + whiteNoise[idx]

    gaussNoise = np.random.randn(n)

    gaussWalk = np.zeros(n)
    for idx, val in enumerate(gaussWalk):
        gaussWalk[idx] = gaussNoise[0] if idx == 0 else gaussWalk[idx - 1] + gaussNoise[idx]

    fig = plt.figure(figsize=(12, 6))
    sz = np.array([2, 2])
    whiteNoiseAx = plot_TD_FD(whiteNoise, fs=1, timeAx=fig.add_subplot(sz[0], sz[1], 1), freqAx=fig.add_subplot(sz[0], sz[1], 3), tLim=np.array([0, n]), title="White Noise")
    randomWalkAx = plot_TD_FD(randomWalk, fs=1, timeAx=fig.add_subplot(sz[0], sz[1], 2), freqAx=fig.add_subplot(sz[0], sz[1], 4), tLim=np.array([0, n]), title="Random Walk")

    whiteNoise_polyfit,  whiteNoise_polypts = poly_fit_plot(t, whiteNoise, 20, n, axes=whiteNoiseAx[0], color='magenta')
    whiteNoise_polyfit_integrated = np.zeros(n)
    for idx, val in enumerate(whiteNoise_polypts[0]):
        whiteNoise_polyfit_integrated[idx] = whiteNoise_polypts[1][0] if idx == 0 else whiteNoise_polyfit_integrated[idx - 1] + whiteNoise_polypts[1][idx]
    randomWalkAx[0].plot(t, whiteNoise_polyfit_integrated, color='magenta')

    poly,  polypts = poly_fit_plot(t, randomWalk, 20, n, axes=randomWalkAx[0], color='blue')

    whiteNoiseAx = plot_TD_FD(whiteNoise_polypts[1], fs=1, timeAx=whiteNoiseAx[0], freqAx=whiteNoiseAx[1], title="White Noise", tColor='magenta', fColor='magenta')
    # randomWalkAx = plot_TD_FD(randomWalk, fs=1, timeAx=randomWalkAx[0], freqAx=randomWalkAx[1], title="Random Walk")

    plt.show()

    return()


polyfit_whitenoise_vs_randomwalk()
