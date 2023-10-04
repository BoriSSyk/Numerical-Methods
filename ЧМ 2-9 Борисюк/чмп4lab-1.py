import numpy as np
A = np.array([[1, 2], [4, -1]])
B = np.array([[2, -3], [-4, 1]])
AB = np.dot(A, B)
BA = np.dot(B, A)
C = AB - BA
print("Матриця C:")
print(C)
