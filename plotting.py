import numpy as np
import matplotlib.pyplot as plt


def plot_TD_FD(data, Data, fs=1, timeAx=0, freqAx=0, tLim=np.array([0, 0]), fLim=np.array([0, 0]), pltShw=1, title=""):
    n = len(data)
    # f = np.linspace(0,fs/2 - 1,n/2)
    if (timeAx == 0 or freqAx == 0):
        fig = plt.figure(figsize=(6, 6))
        timeAx = fig.add_subplot(211)
        freqAx = fig.add_subplot(212)

    if (tLim - np.array([0, 0])).all(): tLim = np.array([0, 1000])
    if (fLim - np.array([0, 0])).all(): fLim = np.array([100, n])

    timeAx.set_title(title + ' TD')
    freqAx.set_title(title + ' FD')
    timeAx.plot(data, color='black')
    timeAx.set_xlim(tLim)
    timeAx.set_ylim(min(data), max(data))

    freqAx.plot(abs(Data), color='blue')
    freqAx.set_xscale('log')
    freqAx.set_yscale('log')
    freqAx.set_xlim(fLim)
    freqAx.set_ylim(min(abs(Data)), max(abs(Data)))

    # axlim = 3
    # ax1.set_xlim(-axlim, axlim)
    # ax1.set_ylim(-axlim, axlim)

    if pltShw == 1: plt.show()

    return (timeAx, freqAx)
