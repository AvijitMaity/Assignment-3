# This program shows how to solve the equation using newton raphson  method
from numpy import *
from scipy import optimize

def f(x):
    return (sin(cos(exp(x))))
def fprime(x):
    return(-exp(x)*cos(cos(exp(x)))*sin(exp(x))) # The derivatie of the function is calculated using mathematica

root = optimize.newton(f,-0.1,fprime) # Initial guess is -0.1
print("root=",root)