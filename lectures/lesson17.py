#LESSON 17 (10.6.25 - Monday)

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