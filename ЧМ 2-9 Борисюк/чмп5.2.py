import numpy as np
import matplotlib.pyplot as plt
import math
x_values = np.linspace(-2, 2, 400)
y_values = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x_values, y_values)
F1 = np.sin(X) + 2 * Y - 2
F2 = np.cos(Y - 1) + X - 0.7
plt.contour(X, Y, F1, levels=[0], colors='r', label='sin(x) + 2y - 2 = 0')
plt.contour(X, Y, F2, levels=[0], colors='b', label='cos(y - 1) + x - 0.7 = 0')
plt.title('Відокремлення коренів системи рівнянь')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()
