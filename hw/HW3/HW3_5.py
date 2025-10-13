#HOMEWORK #3_5

import numpy as np

W = 1000

L = np.sqrt(10**2 + 5**2)

#T1 T2 T3
A = np.array([
    [2/np.sqrt(33), -7/np.sqrt(158), 0],
    [-2/np.sqrt(33), -3/np.sqrt(158), 5/L],
    [5/np.sqrt(33), 10/np.sqrt(158), 10/L]])

b = np.array([0, 0, W])
T = np.linalg.solve(A, b)
T1, T2, T3 = T

print(f"T1 = {T1:.4f} lb")
print(f"T2 = {T2:.4f} lb")
print(f"T3 = {T3:.4f} lb")