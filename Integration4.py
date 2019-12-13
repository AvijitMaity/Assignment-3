# This program shows how to compute the integration using 5 th order gaussian quadrature  rule #

import numpy as np
from scipy import integrate
def f(x):
    return (np.exp(x))


A= integrate.fixed_quad(f,0,1,n=5)
print('The value of the integral is=', A)