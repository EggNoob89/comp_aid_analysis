#LESSON 21 (10.15.25 - Wednesday)

#(3) Apply the multivariate Newton-Raphson code to solve the above problem.
import numpy as np
u1=0; u2=0 #initial values
P=2; es=0.5; mxea=100 # max of ea1, ea2, ea3, ...
i=0; maxiter=30 # need this as Newton Raphson may diverge
while mxea>es and i< maxiter:
    i=i+1 #increment counter
    f=np.matrix([[u1*np.exp(u1)-(u2-u1)*np.exp(u2-u1)],[(u2-u1)*np.exp(u2-u1)-P]]) # f
    J=np.matrix([[(u1+1)*np.exp(u1)+(u2-u1+1)*np.exp(u2-u1), -(u2-u1+1)*np.exp(u2-u1)],
                 [-(u2-u1+1)*np.exp(u2-u1), (u2-u1+1)*np.exp(u2-u1)]]) #Jacobian matrix (square matrix)
    OLD=np.matrix([[u1],[u2]]) #save old values, must be column
    NEW=OLD-np.linalg.solve(J,f) # make new guess
    ea=abs((NEW-OLD)/NEW)*100 # compute relative errors
    mxea=np.max(ea) # extract largest error
    u1=NEW[0,0]; u2=NEW[1,0];
if i == maxiter:
    print('no convergence')
else:
    print('u1={0:.4f},\nu2={1:.4f}'.format(u1,u2))

#%%  Modify the continuing condition and use residuals > 10−4 instead 

import numpy as np
u1=0; u2=0 #initial values
P=2; es=1e-4; maxf=100
i=0; maxiter=30; list_maxf=[]; list_i=[]
while maxf>es and i< maxiter:
    list_i.append(i); list_maxf.append(maxf)
    i=i+1 #increment counter
    f=np.matrix([[u1*np.exp(u1)-(u2-u1)*np.exp(u2-u1)],[(u2-u1)*np.exp(u2-u1)-P]]) # f
    J=np.matrix([[(u1+1)*np.exp(u1)+(u2-u1+1)*np.exp(u2-u1), -(u2-u1+1)*np.exp(u2-u1)], [-(u2-u1+1)*np.exp(u2-u1),(u2-u1+1)*np.exp(u2-u1)]]) #Jacobian matrix (square matrix)
    OLD=np.matrix([[u1],[u2]]) #save old values, must be column
    NEW=OLD-np.linalg.solve(J,f) # make new guess
    maxf=np.max(np.abs(f)) # extract largest f
    u1=NEW[0,0]; u2=NEW[1,0];
if i == maxiter:
    print('no convergence')
else:
    print('u1={0:.4f},\nu2={1:.4f}'.format(u1,u2))

import pylab
pylab.plot(list_i, list_maxf)
pylab.title('Residuals vs Iteration #')
pylab.xlabel('Iteration')
pylab.ylabel('Max Residuals')
pylab.grid()
