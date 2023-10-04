import numpy as np
N = 4
M = 5
A = np.random.rand(N, M)
row_means = np.mean(A, axis=1)
min_row_mean = np.min(row_means)
print("Матриця A:")
print(A)
print("\nСередні значення для кожного рядка:")
print(row_means)
print("\nНайнижче середнє значення серед усіх рядків:", min_row_mean)
