import sympy as sp
x = sp.symbols('x')
f = 6*x**4 + 4*x**3 + x**2 + x - 10


def bisection_method(f, a, b, epsilon):
    while (b - a) / 2 > epsilon:
        midpoint = (a + b) / 2
        if f.subs(x, midpoint) == 0:
            return midpoint
        elif f.subs(x, a) * f.subs(x, midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2


a = 1.0
b = 2.0
epsilon = 0.0001
root_bisection = bisection_method(f, a, b, epsilon)
print("Метод половинного ділення: x =", root_bisection)
