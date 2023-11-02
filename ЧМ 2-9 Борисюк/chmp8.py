import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
x = np.array([0.5, 0.7, 1, 1.4, 1.9])
y = np.array([2.14, 1.46, 1.15, 3.28, 1.83])
cs = CubicSpline(x, y)
x_new = np.linspace(0.5, 1.9, 100)
y_new = cs(x_new)
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Табличні точки')
plt.plot(x_new, y_new, '-', label='Апроксимуючий сплайн')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
