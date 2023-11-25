import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
def plot_integral(f, result, method_name):
    x = np.linspace(a, b, 100)
    y = f(x)
    plt.plot(x, y, label='Функція')
    plt.fill_between(x, y, alpha=0.2)
    plt.title(f'Графік функції та області під кривою ({method_name} метод)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()
    print(f"Значення інтегралу ({method_name} метод): {result}\n")
def f1(x):
    return 1 / (2 * np.sqrt(2 * x**2 + 1.3))
a, b = 0, 1
result_trapezoid_1 = integrate.trapz(f1(np.linspace(a, b, 20)), np.linspace(a, b, 20))
plot_integral(f1, result_trapezoid_1, 'Метод трапецій')
