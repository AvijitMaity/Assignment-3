# This program shows how to solve the equation using bisection method

from numpy import *
from scipy import optimize

def f(x):
    return (sin(cos(exp(x))))
root = optimize.bisect(f, -1,1)
print("root=",root)