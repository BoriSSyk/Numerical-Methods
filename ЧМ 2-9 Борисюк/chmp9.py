import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols
def f(x):
    return np.log(x + 1) - np.sin(x)
def f_prime(x):
    return 1 / (x + 1) - np.cos(x)
def f_double_prime(x):
    return -1 / (x + 1)**2 + np.sin(x)
def f_triple_prime(x):
    return 2 / (x + 1)**3 + np.cos(x)
x0 = 0
f_x0 = f(x0)
f1_x0 = f_prime(x0)
f2_x0 = f_double_prime(x0)
f3_x0 = f_triple_prime(x0)
x = symbols('x')
T = f_x0 + f1_x0*(x-x0) + (f2_x0/2)*(x-x0)**2 + (f3_x0/6)*(x-x0)**3
print("f(0) =", f_x0)
print("T(x) =", T)
x_vals = np.linspace(-2, 2, 1000)
f_vals = np.array([f(xi) for xi in x_vals])
T_vals = np.array([T.subs(x, xi).evalf() for xi in x_vals])
plt.figure(figsize=(10, 6))
plt.plot(x_vals, f_vals, label="f(x) curve", color='blue')
plt.plot(x_vals, T_vals, label="T(x)", linestyle='--', color='red')
plt.scatter(x0, f_x0, color='red', label='Точка розкладу')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Графік функції та наближення многочленом Тейлора")
plt.tight_layout()
plt.grid()
plt.show()
