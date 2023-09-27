import numpy as np
import math
from scipy.optimize import newton


def f(x):
    return 6*x**4 + 4*x**3 + x**2 + x - 10


def df(x):
    return 24*x**3 + 12*x**2 + 2*x + 1


initial_guess = 1.0
root_newton = newton(f, initial_guess, fprime=df)
print("Метод Ньютона: x =", root_newton)
