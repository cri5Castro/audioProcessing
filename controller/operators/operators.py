import math
import numpy as np
from scipy import signal
   
def interpolate(sig, factor:int):
    print(factor)
    return signal.resample(sig,sig.size*factor)

def decimate(sig,factor:int):
    return signal.resample(sig,math.ceil(sig.shape[0]/factor))

def shift(sig,factor:int):
    if factor == 0: 
        return sig
    if np.abs(factor) > sig.size:
        res = np.zeros_like(sig)
    elif factor < 0:
        zeros = np.zeros((abs(factor),1))
        res = np.concatenate((zeros,sig[:factor]))
    else:
        zeros = np.zeros((factor,1))
        res = np.concatenate((sig[factor:],zeros))
    return res

def reflect(sig):
    return sig[::-1]

def mamplitude(sig,factor):
    return sig*factor