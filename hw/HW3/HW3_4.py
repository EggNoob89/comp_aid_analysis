#HOMEWORK #3_4

import numpy as np

v1 = 100; v2 = 50; R1 = 5; R2 = 100; R3 = 200; R4 = 150; R5 = 250

A = np.array([
    [R1, 0, 0, R4, 0],
    [0, R2, 0, -R4, R5],
    [0, 0, R3, 0, -R5],
    [1, -1, 0, -1, 0], #i1 - i2 -i4
    [0, 1, -1, 0, -1] #i2 - i3 - i5
])

b = np.array([v1, 0, -v2, 0, 0])

#Currents = I
I = np.linalg.solve(A, b)

I1, I2, I3, I4, I5 = I
print(f"I1 = {I1:.4f} A")
print(f"I2 = {I2:.4f} A")
print(f"I3 = {I3:.4f} A")
print(f"I4 = {I4:.4f} A")
print(f"I5 = {I5:.4f} A")