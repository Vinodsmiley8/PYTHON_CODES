# Solve a system of linear equations
import numpy as np

coefficients = np.array([[2, 1], [1, -3]])
constants = np.array([8, 1])

solution = np.linalg.solve(coefficients, constants)
print("Solution:", solution)