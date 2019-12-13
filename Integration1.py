# This program shows how to compute the integration using trapezoidal rule #

from numpy import trapz

import numpy as np

def f(x):
    return (np.exp(x))

x = np.arange(0,1,0.01)
y = f(x)
A= np.trapz(y,x)
print('The value of the integral is=', A)