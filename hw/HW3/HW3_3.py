#HOMEWORK #3_3

import numpy as np

# System 1
s1 = np.array([
    [ 4, -5, -3,  5],
    [-4,  0,  4, -4],
    [ 0, -4, -2,  2],
    [ 3, -2, -4,  0]])
s1c = np.array([22, -28, 4, 3])

# System 2
s2 = np.array([
    [ 3, -2, -4,  0],
    [ 4,  2, -3,  5],
    [ 0, -4, -2,  2],
    [-4,  0,  4, -4]])
s2c = np.array([3, 22, 4, -28])

def determinant(x):
    return(np.linalg.det(x))

#if the determinant of either systems of equations is 0 it IS NOT SOLVABLE
if determinant(s1) == 0:
    print('system 1 is not solvable')
elif determinant(s2) == 0:
    print('system2 is not solvable')
else: 
    print('both equations are solvable')
    
    
    