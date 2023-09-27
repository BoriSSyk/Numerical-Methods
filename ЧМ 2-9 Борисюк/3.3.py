import numpy as np
from scipy.misc import derivative


def f(x):
    return 6 * x**4 + 4 * x**3 + x**2 + x - 10


def komb(a, b, eps):
    ai = a
    bi = b
    while abs(ai - bi) > eps:
        ai_1 = ai - f(ai) * (bi - ai) / (f(bi) - f(ai))
        bi_1 = bi - f(bi) / derivative(f, bi, n=1)
        ai = ai_1
        bi = bi_1
    x = (ai_1 + bi_1) / 2
    return x


result = komb(-2, -0.5, 0.0001)
print('Solving the equation by the combined method x =', result)
