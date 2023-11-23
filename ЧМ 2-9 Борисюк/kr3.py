import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
i = np.array([0, 1, 2, 3, 4])
x = np.array([0.1, 0.3, 0.6, 1.1, 1.8])
y = np.array([2.65, 2.75, 2.19, 1.76, 3.43])
cs = CubicSpline(x, y)
x_range = np.linspace(min(x), max(x), 100)
y_cs = cs(x_range)
plt.plot(x_range, y_cs, label="Cubic Spline")
plt.scatter(x, y, color='red', label="Given points")
plt.title("Cubic Spline Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
