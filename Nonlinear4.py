# This program shows how to solve the equation using secant  method #
from numpy import *
from scipy import optimize

def f(x):
    return (sin(cos(exp(x))))
root = optimize.newton(f, -0.1) # Initial guess is -0.1
print("root=",root)