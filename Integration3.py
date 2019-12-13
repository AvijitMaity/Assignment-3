# This program shows how to compute the integration using romberg method #

import numpy as np
from scipy import integrate
def f(x):
    return (np.exp(x))


A= integrate.romberg(f,0,1)
print('The value of the integral is=', A)