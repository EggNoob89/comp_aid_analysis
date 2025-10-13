#LESSON 14 (9.29.25 - Monday)

import numpy as np
A=np.matrix('1 2 1; 5 3 4; 8 10 1') # 3x3 matrix
np.linalg.det(A)
#roundoff error is present in the output 

#%% Solve the Matrix Equation using PYTHON

k1=10; k2=10; k3=10 #(N/m) #given constants
m1=2; m2=3; m3=2.5 #(kg)
g=9.81 #(m/s^2)
import numpy as np
A = np.matrix([[-(k1+k2), k2, 0],[k2, -(k2+k3), k3],[0, k3, -k3]])
b=-g*np.matrix([[m1],[m2],[m3]])
print(np.linalg.det(A))
x=np.linalg.solve(A,b)
x1=x[0,0]; x2=x[1,0]; x3=x[2,0]; #solutions
print(-k1*x1+k2*(x2-x1)+m1*g) #verify results in original equations (before rearrangement)
print(-k2*(x2-x1)+k3*(x3-x2)+m2*g) #expect to see zeros (or small numbers)
print(-k3*(x3-x2)+m3*g)
#lot of roundoff errors but its not as significant as it seems
