import numpy as np
import matplotlib.pyplot as plt
from plotting import plot_TD_FD, poly_fit_plot
import math


def polyfit_exploration():
    # Found that integrating a polyfit on white noise
    # produces a very similar result to performing the polyfit
    # on the integrated white noise (random walk)

    n = 100000  # Number of elements
    nf = int(n/2+1)  # Number of elements in FD
    fs = 1
    t = np.linspace(0, n/fs, n, False)  # Do not include endpoint
    f = np.linspace(0, fs/2, nf, True)  # Include endpoint. Number of elements is n/2 + 1

    # Compute Time Domain WN, RW, and their polyfits
    wn_td = np.random.rand(n) - 0.5  # White Noise, Time Domain
    rw_td = np.cumsum(wn_td)  # Random Walk, Time Domain
    wd_td_pf_td = poly_fit_plot(t, wn_td, 20, n)[1][1]
    rw_td_pf_td = poly_fit_plot(t, rw_td, 20, n)[1][1]

    # Take DFT of each (real) signal
    wn_fd = abs(np.fft.rfft(wn_td))
    rw_fd = abs(np.fft.rfft(rw_td))
    wd_td_pf_fd = abs(np.fft.rfft(wd_td_pf_td))
    rw_td_pf_fd = abs(np.fft.rfft(rw_td_pf_td))

    # Perform polyfit on Frequency Domain signals
    wd_fd_pf_fd = poly_fit_plot(f, wn_fd, 20, nf)[1][1]
    rw_fd_pf_fd = poly_fit_plot(f, rw_fd, 20, nf)[1][1]
    f_ls = np.rint(10**np.linspace(0, math.log10(n/2), int(n/10), False)).astype(int)  # Generate sampling indices for logarithmic sampling
    wd_fd_ls_pf_fd = poly_fit_plot(f[[f_ls]], wn_fd[[f_ls]], 20, nf)[1]
    rw_fd_ls_pf_fd = poly_fit_plot(f[[f_ls]], rw_fd[[f_ls]], 20, nf)[1]
    # wd_fd_ls_pf_fd = np.polynomial.Polynomial.fit(x, y, order).linspace(n, [0, max(t)])
    # rw_fd_ls_pf_fd =

    # Take IDFT of each polyfit frequency data
    # data = np.fft.irfft(Data)

    fig = plt.figure(figsize=(12, 6))
    wn_td_ax = fig.add_subplot(221, title='White Noise, TD')
    rw_td_ax = fig.add_subplot(222, title='Random Walk, TD')
    wn_fd_ax = fig.add_subplot(223, title='White Noise, FD', xscale='log', yscale='log')
    rw_fd_ax = fig.add_subplot(224, title='Random Walk, FD', xscale='log', yscale='log')

    wn_td_ax.plot(t, wn_td, color='black')
    rw_td_ax.plot(t, rw_td, color='black')
    wn_fd_ax.plot(f, wn_fd, color='black')
    rw_fd_ax.plot(f, rw_fd, color='black')

    wn_td_ax.plot(t, wd_td_pf_td, color='blue')  # Blue indicates polyfit perfomed in TD
    rw_td_ax.plot(t, rw_td_pf_td, color='blue')

    wn_fd_ax.plot(f, wd_td_pf_fd, color='blue')
    rw_fd_ax.plot(f, rw_td_pf_fd, color='blue')
    # wn_fd_ax.plot(f, wd_fd_pf_fd, color='magenta', linestyle='dashed')  # Magenta indicates polyfit perfomed in FD
    # rw_fd_ax.plot(f, rw_fd_pf_fd, color='magenta', linestyle='dashed')
    # wn_fd_ax.plot(wd_fd_ls_pf_fd[0], wd_fd_ls_pf_fd[1], color='magenta')
    # rw_fd_ax.plot(rw_fd_ls_pf_fd[0], rw_fd_ls_pf_fd[1], color='magenta')


    # noise_1f = np.mean(np.divide(abs(Data[1:]), f[1:]))/f[1:]
    # freqAx.plot(f[1:], noise_1f, color='red')

    # whiteNoise_polyfit,  whiteNoise_polypts = poly_fit_plot(t, whiteNoise, 20, n, axes=whiteNoiseAx[0], color='magenta')
    # whiteNoise_polyfit_integrated = np.cumsum(whiteNoise_polypts[1])
    # randomWalkAx[0].plot(t, whiteNoise_polyfit_integrated, color='magenta')


    # randomWalkAx = plot_TD_FD(randomWalk, fs=1, timeAx=randomWalkAx[0], freqAx=randomWalkAx[1], title="Random Walk")

    plt.show()

    return()


polyfit_exploration()
