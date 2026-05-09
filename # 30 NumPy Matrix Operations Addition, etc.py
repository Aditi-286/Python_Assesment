# 30 NumPy Matrix Operations Addition, Subtraction, Multiplication, Inverse

import numpy as np

# Create two matrices
A = np.array([[4, 7],
              [2, 6]])

B = np.array([[1, 3],
              [5, 2]])

print("Matrix A:\n", A)
print("\nMatrix B:\n", B)

# Addition
print("\nAddition:\n", A + B)

# Subtraction
print("\nSubtraction:\n", A - B)

# Multiplication (Matrix Product)
print("\nMatrix Multiplication:\n", np.dot(A, B))

# Inverse of matrices (only if determinant is not zero)
print("\nInverse of A:\n", np.linalg.inv(A))
print("\nInverse of B:\n", np.linalg.inv(B))