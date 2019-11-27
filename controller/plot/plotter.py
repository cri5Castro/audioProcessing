import matplotlib.pyplot as plt
import numpy as np
def plot(**signals):
    labels=[]
    for name,signal in signals.items():
        #plt.figure()
        plt.plot(np.arange(signal.shape[0]),signal)
        labels.append(name)
        plt.xlabel(r'$n$'), plt.ylabel(f"Amplitude")
    plt.legend(labels)
    plt.show()