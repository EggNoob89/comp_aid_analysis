#HW4_3

import numpy as np
x = np.zeros([3,1]); old = np.zeros([3,1]) # initial values of unknowns (all zeros)
es=0.05; mxea=100 # max of ea1, ea2, ea3, ...
while mxea>es:
    for i in range(3):
        old[i] = x[i] # store old x values
    x[0] = (3800 + 3*x[1] + x[2])/15
    x[1] = (1200 + 3*x[0] + 6*x[2])/18 # most updated values of x1, x2, x3 are used
    x[2] = (2350 + 4* x[0] + x[1])/12
    ea=abs((x-old)/x)*100 # x and old are vectors, so ea is a vector
    mxea=np.max(ea) # max of vector ea
print('x1={0:.3f},\nx2={1:.3f},\nx3={2:.3f},\n'.format(x[0,0], x[1,0], x[2,0]))