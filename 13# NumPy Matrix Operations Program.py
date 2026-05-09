# NumPy Matrix Operations Program

import numpy as np

# Create 5x5 matrix with random integers
matrix = np.random.randint(1, 100, (5, 5))

print("Original Matrix:\n")
print(matrix)

# Row-wise sum
row_sum = np.sum(matrix, axis=1)
print("\nRow-wise Sum:")
print(row_sum)

# Column-wise sum
column_sum = np.sum(matrix, axis=0)
print("\nColumn-wise Sum:")
print(column_sum)

# Transpose of matrix
transpose_matrix = matrix.T
print("\nTranspose of Matrix:")
print(transpose_matrix)

# Determinant of matrix
determinant = np.linalg.det(matrix)
print("\nDeterminant of Matrix:")
print(determinant)