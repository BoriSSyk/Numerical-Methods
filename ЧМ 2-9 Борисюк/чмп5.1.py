from scipy.optimize import fsolve
import math
def equations(vars):
    x, y = vars
    eq1 = math.sin(x) + 2 * y - 2
    eq2 = math.cos(y - 1) + x - 0.7
    return [eq1, eq2]
initial_guess = [0.0, 0.0]
result = fsolve(equations, initial_guess, xtol=0.001)
print(f'Результат: x = {result[0]}, y = {result[1]}')
