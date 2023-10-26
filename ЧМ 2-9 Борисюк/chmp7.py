import numpy as np
import matplotlib.pyplot as plt
xi = [0.151, 0.505]
yi = [0.8607, 0.0]
x_interpolate = 0.15
def newton_interpolation(x, y, x_interpolate):
    n = len(x)
    coefficients = np.zeros(n)
    coefficients[0] = y[0]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            y[i] = (y[i] - y[i - 1]) / (x[i] - x[i - j])
        coefficients[j] = y[j]
    result = 0
    for j in range(n):
        term = coefficients[j]
        for i in range(j):
            term *= (x_interpolate - x[i])
        result += term
    return result
interpolated_value = newton_interpolation(xi, yi, x_interpolate)
print(f"Значення функції при x = {x_interpolate} дорівнює {interpolated_value}")
x_range = np.linspace(min(xi), max(xi), 100)
y_interpolated = [newton_interpolation(xi, yi, x) for x in x_range]
plt.plot(xi, yi, 'ro', label='Вхідні точки')
plt.plot(x_range, y_interpolated, label='Інтерполяційна функція')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
