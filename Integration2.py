# This program shows how to compute the integration using simpsons rule #

import numpy as np
from scipy import integrate
def f(x):
    return (np.exp(x))

x = np.arange(0,1,0.0001)
y = f(x)
A= integrate.simps(y,x)
print('The value of the integral is=', A)