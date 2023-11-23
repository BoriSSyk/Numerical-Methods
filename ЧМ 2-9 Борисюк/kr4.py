import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
def true_function(x):
    return np.cos(2*x) + 2*x
def model_linear(params, x):
    return params[0] * x + params[1]
def model_quadratic(params, x):
    return params[0] * x**2 + params[1] * x + params[2]
x = np.arange(0.1, 1.1, 0.1)
y_true = true_function(x)
noise = np.random.normal(0, 0.1, len(x))
y_noisy = y_true + noise
initial_params_linear = [0, 0]
initial_params_quadratic = [0, 0, 0]
result_linear = least_squares(model_linear, initial_params_linear, args=(x,), loss='soft_l1')
result_quadratic = least_squares(model_quadratic, initial_params_quadratic, args=(x,), loss='soft_l1')
y_approx_linear = model_linear(result_linear.x, x)
y_approx_quadratic = model_quadratic(result_quadratic.x, x)
plt.plot(x, y_true, label="True Function")
plt.scatter(x, y_noisy, color='red', label="Noisy Data")
plt.plot(x, y_approx_linear, label="Linear Approximation")
plt.plot(x, y_approx_quadratic, label="Quadratic Approximation")
plt.title("Least Squares Approximations")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
