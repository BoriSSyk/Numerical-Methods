import numpy as np
import math
from scipy.misc import derivative


def f(x):
    return 6*x**4 + 4*x**3 + x**2 + x - 10


solut = np.roots([6, 4, 1, 1, -10])
a = 1.0
b = 2.0
print("Аналітичне відокремлення коренів:", solut)
