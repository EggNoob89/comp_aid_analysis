#Exam 2 Review 
import numpy as np

x = np.zeros([3,1])
old = np.zeros([3,1])
es = 0.5
mxea = 100

while mxea > es:
    old = x.copy()
    x[0] = (36 + 2*x[1] - 3*x[2]) / 8
    x[1] = (74 - 2*x[0] - 6*x[2]) / 2
    x[2] = (4 - 2*x[0] - 8*x[1]) / 4
    
    ea = abs((x - old) / x) * 100
    mxea = np.max(ea)

print('x1={0}, \nx2={1}, \nx3={2}'.format(x[0,0], x[1,0], x[2,0]))

#%%
import numpy as np

x = np.zeros((3,1))
old = np.zeros((3,1))
es = 0.5
mxea = 100

while mxea > es:
    old = x.copy()
    # updated ordering: row2 and row3 swapped from original image
    x[0] = (36 + 2*x[1] - 3*x[2]) / 8      # x1
    x[1] = (4  - 2*x[0] + 4*x[2]) / 8      # x2 (from swapped equation)
    x[2] = (74 - 2*x[0] - 2*x[1]) / 6      # x3
    ea = np.abs((x - old) / x) * 100
    mxea = np.max(ea)
    print(f'mxea: {mxea:.4f}')

print('x1={0},\nx2={1},\nx3={2}'.format(x[0,0], x[1,0], x[2,0]))

#%% Lecture 12  Root Finding Review & Matrix Math
#- No code

#%%Lecure 12 - 13
import numpy as np
A = np.matrix('-3 2; 5 1')
b = np.matrix('-9;2')
x = np.linalg.solve(A,b)
print(x)

#%%Lecture 14

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

#%% Lecture 17
#Gauss Seidel : Code
import numpy as np
#given constants
k1=k2=k3=10 #N/m
m1=2; m2=3; m3=2.5 #kg
g=9.81 #m/s^2
# initial values of unknowns (all zeros)
x = np.zeros([3,1]); old = np.zeros([3,1])
# initialize while loop
es=0.5; mxea=100 # max of ea1, ea2, ea3, ...
while mxea>es:
    for i in range(3):
        old[i] = x[i] # store old x values
        x[0] = (m1*g+k2* x[1])/(k1+k2)
        x[1] = (m2*g+k2* x[0]+k3*x[2])/(k2+k3) # most updated values of x1, x2, x3 are used
        x[2] = (m3*g+k3* x[1])/k3
        ea=abs((x-old)/x)*100 # x and old are vectors, so ea is a vector
        mxea=np.max(ea) # max of vector ea
print('x1={0:.3f},\nx2={1:.3f},\nx3={2:.3f},\n'.format(x[0,0], x[1,0], x[2,0]))

#%% Lecture 18

import numpy as np
#given constants
k1=k2=k3=10 #N/m
m1=2; m2=3; m3=2.5 #kg
g=9.81 #m/s^2
# initial values of unknowns (all zeros)
x = np.zeros([3,1]); old = np.zeros([3,1])
# initialize while loop
es=0.5; mxea=100 # max of ea1, ea2, ea3, ...
while mxea>es:
    for i in range(3):
        old[i] = x[i] # store old x values
    x[0] = (m1*g+k2* x[1])/(k1+k2)
    x[1] = (m2*g+k2* x[0]+k3*x[2])/(k2+k3) # most updated values of x1, x2, x3 are used
    x[2] = (m3*g+k3* x[1])/k3
    ea=abs((x-old)/x)*100 # x and old are vectors, so ea is a vector
    mxea=np.max(ea) # max of vector ea
print('x1={0:.3f},\nx2={1:.3f},\nx3={2:.3f},\n'.format(x[0,0], x[1,0], x[2,0]))

#%%Lecture 19

import numpy as np
x1=1.5; x2=3.5 #initial values
# initialize
es=0.5; mxea=100 # max of ea1, ea2, ea3, ...
i=0; maxiter=30 # need this as Newton Raphson may diverge
while mxea>es and i< maxiter:
    i=i+1 #increment counter
    f=np.matrix([[x1**2+x1*x2-10],[x2+3*x1*x2**2-57]]) # vector function, f is a column
    J=np.matrix([[2*x1+x2, x1],[3*x2**2,1+6*x1*x2]]) #Jacobian matrix (square matrix)
    OLD=np.matrix([[x1],[x2]]) #save old values, must be column
    NEW=OLD-np.linalg.solve(J,f) # make new guess, Cramer’s rule for handwork only!
    ea=abs((NEW-OLD)/NEW)*100 # compute relative errors
    mxea=np.max(ea) # extract largest error
x1=NEW[0,0]; x2=NEW[1,0];
if i == maxiter:
    print('no convergence')
else:
    print('x1={0:.4f},\nx2={1:.4f}'.format(x1,x2))