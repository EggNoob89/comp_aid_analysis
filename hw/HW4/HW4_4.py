#HW_4_4

import numpy as np

c1=1; c2=1; c3=1 #initial values
# initialize
es=0.005; maxiter=30 # need this as Newton Raphson may diverge
def newton_raphson(x1,x2,x3,es,maxiter):
    i = 0
    mxea = 100
    while mxea>es and i< maxiter:
        i += 1 #increment counter

        # Define functions inside the loop (must update every iteration!)
        f1 = x1**3 - 10*x1 + x2 - x3 + 3
        f2 = x2**3 + 10*x2 - 2*x1 - 2*x3 - 5
        f3 = x1 + x2 - 10*x3 + 2*np.sin(x3) + 5

        J = np.matrix([
            [3*x1**2 - 10, 1, -1],
            [-2, 3*x2**2 + 10, -2],
            [1, 1, -10 + 2*np.cos(x3)]
        ])

        f = np.matrix([[f1], [f2], [f3]])
        
        OLD = np.matrix([[x1],[x2],[x3]]) #save old values, must be column
        
        NEW = OLD-np.linalg.solve(J,f) # make new guess, Cramer’s rule for handwork only!
        
        ea=abs((NEW-OLD)/NEW)*100 # compute relative errors
        
        mxea=np.max(ea) # extract largest error
        
        x1, x2, x3 = NEW[0,0], NEW[1,0], NEW[2,0]; #update values
    if i == maxiter:
        print('no convergence')
    else:
        print(f'x = {x1:.4f}, y={x2:.4f}, z={x3:.4f}; converges in {i} iterations')

newton_raphson(c1,c2,c3,es,maxiter)
