import matplotlib.pyplot as plt
import numpy as np


def plot(**signals):
    """plot discrete signals

    Arguments:
        signals {dict} -- [contains the signals to be plotted {'name':signal,...,'name',signal}]
    """
    labels = []
    for name, signal in signals.items():
        # plt.figure()
        plt.plot(np.arange(signal.shape[0]), signal)
        labels.append(name)
        plt.xlabel(r'$n$'), plt.ylabel(f"Amplitude")
    plt.legend(labels)
    plt.show()
