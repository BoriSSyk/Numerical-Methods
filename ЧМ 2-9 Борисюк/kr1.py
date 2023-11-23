def f(x):
    return 2*x**4 + 4*x**3 + x**2 + 3*x - 6
def chord_method(func, a, b, tolerance):
    if func(a) * func(b) > 0:
        raise ValueError("Значення функції на кінцях інтервалу повинні мати протилежні знаки.")
    while abs(func(b)) > tolerance:
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if func(c) == 0:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
    
    return (a * func(b) - b * func(a)) / (func(b) - func(a))
intervals = [(-3, -2), (-2, -1), (-1, 0), (0, 1), (1, 2), (2, 3)]
for interval in intervals:
    try:
        result = chord_method(f, interval[0], interval[1], 0.001)
        print(f"Корінь в інтервалі {interval}: {result:.4f}")
    except ValueError:
        print(f"Корінь не знайдено в інтервалі {interval}")
