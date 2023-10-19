import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
x_values = np.array([-2, -1, 1, 2])
y_values = np.array([-26, -5, 1, 10])
x_interpolate = np.array([-0.5, 0.5, 1.5, 2.5])
poly = lagrange(x_values, y_values)
y_interpolate = poly(x_interpolate)
plt.plot(x_values, y_values, 'o', label="Дані точки")
plt.plot(x_interpolate, y_interpolate, label="Інтерполяція")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Інтерполяція функції за допомогою багаточлену Лагранжа')
plt.grid()
plt.show()
for x, y in zip(x_interpolate, y_interpolate):
    print(f'f({x}) = {y:.3f}')
