import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
xi = np.array([-2, -1, 0, 3, -1.5, -0.5, 1, 2])
fi = np.array([-4, 3, 2, 11, None, None, None, None])
xi = xi[fi != None]
fi = fi[fi != None]
def lagrange_interpolation(x, xi, fi):
    result = 0
    for i in range(len(xi)):
        term = fi[i]
        for j in range(len(xi)):
            if j != i:
                term *= (x - xi[j]) / (xi[i] - xi[j])
        result += term
    return result
x_values = np.array([-1.5, -0.5, 1])
approximated_values = lagrange_interpolation(x_values, xi, fi)
print("Approximated values at given points:")
for x, approx_value in zip(x_values, approximated_values):
    print(f"f({x}) ≈ {approx_value:.3f}")
x_range = np.linspace(min(xi), max(xi), 100)
y_interpolated = lagrange_interpolation(x_range, xi, fi)
plt.plot(x_range, y_interpolated, label="Interpolation")
plt.scatter(xi, fi, color='red', label="Given points")
plt.title("Lagrange Interpolation")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
