import sympy as sp
x = sp.symbols('x')
f = 6*x**4 + 4*x**3 + x**2 + x - 10


def secant_method(f, a, b, epsilon):
    x0 = a
    x1 = b
    while abs(x1 - x0) > epsilon:
        x2 = x1 - (f.subs(x, x1) * (x1 - x0)) / (f.subs(x, x1) - f.subs(x, x0))
        x0 = x1
        x1 = x2
    return x1


a = 1.0
b = 2.0
epsilon = 0.0001

root_secant = secant_method(f, a, b, epsilon)
print("Метод хорд: x =", root_secant)
