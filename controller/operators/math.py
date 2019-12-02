import math
import numpy as np
from scipy import signal


def interpolate(sig, factor: int):
    """[interpolates a discrete signal by  factor]

    Arguments:
        sig {np.array} -- [discrete signal]
        factor {int} -- [factor of interpolation]

    Returns:
        [np.array] -- [interpolated signal]
    """
    return signal.resample(sig, sig.size*factor)


def decimate(sig, factor: int):
    """[downsample a signal by a factor]

    Arguments:
        sig {np.array} -- [discrete signal]
        factor {int} -- [downsampling factor]

    Returns:
        [np.array] -- [downsampled signal]
    """
    return signal.resample(sig, math.ceil(sig.shape[0]/factor))


def shift(sig, factor: int):
    """[shift a signal in time]

    Arguments:
        sig {np.array} -- [discrete signal]
        factor {int} -- [shift factor]

    Returns:
        [np.array] -- [shifted signal in time]
    """
    if factor == 0:
        return sig
    if np.abs(factor) > sig.size:
        res = np.zeros_like(sig)
    elif factor < 0:
        zeros = np.zeros((abs(factor), 1))
        res = np.concatenate((zeros, sig))
    else:
        zeros = np.zeros((factor, 1))
        res = np.concatenate((sig[factor:], zeros))
    return res


def reflect(sig):
    """[reflects a signal in time]

    Arguments:
        sig {np.array} -- [discrete signal]

    Returns:
        [np.array] -- [signal reflected in time]
    """
    return sig[::-1]


def mamplitude(sig, factor):
    """modifies the amplitude of a signal

    Arguments:
        sig {np.array} -- [discrete signal]
        factor {float} -- [amplitude amount]

    Returns:
        [np.array] -- [modulated signal]
    """
    return sig*factor
