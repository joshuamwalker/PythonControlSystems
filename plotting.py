import numpy as np
import matplotlib.pyplot as plt
import math


def plot_TD_FD(data, Data=np.array(0), fs=1000, timeAx=0, freqAx=0, tLim=np.array([0, 0]), fLim=np.array([0, 0]), title=""):
    # Returns 2 axes, time and frequency domain graphs
    # TD and FD axes has limits specified by optional tLim and fLim vectors
    # Optional title can be set for plots
    n = len(data)
    Data = np.fft.fft(data)
    Data = Data[0:math.ceil(n/2)]
    Data = abs(Data)
    # DataSmooth = np.convolve(Data, np.divide(np.ones(20), 20), 'same')  # Smooth frequency domain
    # f = np.linspace(0,fs/2 - 1,n/2)
    if (timeAx == 0 or freqAx == 0):
        fig = plt.figure(figsize=(6, 6))
        timeAx = fig.add_subplot(211)
        freqAx = fig.add_subplot(212)

    t = np.arange(0, n/fs, 1/fs)
    f = np.arange(0, fs/2, fs/n)

    if not any(tLim):
        tLim = np.array([0, 1000])
    if not any(fLim):
        fLim = np.array([f[10], max(f)])

    timeAx.set_title(title + ' TD')
    freqAx.set_title(title + ' FD')
    timeAx.plot(t, data, color='black')
    timeAx.set_xlim(tLim)
    timeAx.set_ylim(min(data), max(data))

    freqAx.plot(f, Data, color='blue')
    # freqAx.plot(f, DataSmooth, color='green')
    noise_1f = np.mean(np.divide(abs(Data[1:]), f[1:]))/f[1:]
    freqAx.plot(f[1:], noise_1f, color='red')

    freqAx.set_xscale('log')
    freqAx.set_yscale('log')
    # freqAx.set_xlim(fLim)
    freqAx.set_ylim(min(abs(Data)), max(abs(Data)))

    # axlim = 3
    # ax1.set_xlim(-axlim, axlim)
    # ax1.set_ylim(-axlim, axlim)

    return (timeAx, freqAx)


def poly_fit_plot(x, y, order, pts, axes=None, color='magenta'):
    # Perform a polynomial fitting of the specified order
    # Return the polynomial and the x, y points of the function
    # Use poly.coef to return the coefficients from the np.polynomial object
    # https://numpy.org/doc/stable/reference/routines.polynomials.package.html#module-numpy.polynomial
    # FUTURE: Add some way to slect the polynomial type (Polynomial/Chebyshev/Legendre/etc.)
    poly = np.polynomial.Polynomial.fit(x, y, order)
    polypts = poly.linspace(pts, [min(x), max(x)])

    if axes is not None:
        axes.plot(polypts[0], polypts[1], color=color)

    return(poly, polypts)
