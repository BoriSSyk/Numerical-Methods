import numpy as np
import matplotlib.pyplot as plt
xi = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
yi = np.array([np.log(x + 1) - np.sin(x) for x in xi])
linear_coefficients = np.polyfit(xi, yi, 1)
linear_approximation = np.poly1d(linear_coefficients)
quadratic_coefficients = np.polyfit(xi, yi, 2)
quadratic_approximation = np.poly1d(quadratic_coefficients)
plt.scatter(xi, yi, label='Точки')
x_linear = np.linspace(0, 1, 100)
y_linear = linear_approximation(x_linear)
plt.plot(x_linear, y_linear, label='Лінійна апроксимація', color='red')
x_quadratic = np.linspace(0, 1, 100)
y_quadratic = quadratic_approximation(x_quadratic)
plt.plot(x_quadratic, y_quadratic, label='Квадратична апроксимація', color='green')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Апроксимація методом найменших квадратів')
plt.legend()
plt.show()
