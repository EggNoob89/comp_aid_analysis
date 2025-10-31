# Coding Project 2 (extra credit)

#(3) Apply Multivariable Newton Raphson
import numpy as np  
u1 = 0; u2 = 0; u3 = 0; #initial values
P = 5; es = 0.05; mxea = 100 
i = 0; maxiter = 30 #Newton Raphson divergence detection
while mxea>es and i<maxiter:
    i = i+1
    k1 = np.exp(u1)
    k2 = np.exp(u2-u1)
    k3 = np.exp(u3-u2)
    f = np.matrix([
        [k1*u1-k2*(u2-u1)],
        [k2*(u2-u1)-k3*(u3-u2)],
        [k3*(u3-u2)-P]]) #3x1

    J = np.matrix([
        [k1*(u1+1)+k2*(u2-u1+1), k2*(u1-u2-1), 0],
        [k2*(u1-u2-1), k2*(u2-u1+1)+k3*(u3-u2+1), k3*(u2-u3-1)],
        [0, k3*(u2-u3-1), k3*(u3-u2+1)]]) #3x3
    
    OLD = np.matrix([[u1],[u2],[u3]]) #save old values, must be columns!
    NEW = OLD - np.linalg.solve(J,f) #make new guess
    ea = abs((NEW-OLD)/NEW)*100 #compute relative errors
    mxea = np.max(ea)
    u1 = NEW[0,0];u2 = NEW[1,0];u3 = NEW[2,0]
if i == maxiter:
    print('no convergence')
else:
    print(f'converged in {i} iterations')
    print(f'u1={u1:.4f},\nu2={u2:.4f},\nu3={u3:.4f},')

#%%(4) 
import numpy as np
import pylab
  
u1 = 0; u2 = 0; u3 = 0; #initial values
P = 5; es = 1e-4; maxf = 100 
i = 0; maxiter = 30; list_maxf=[]; list_i=[] 
while maxf>es and i<maxiter:
    list_i.append(i); list_maxf.append(maxf)
    i=i+1
    k1 = np.exp(u1)
    k2 = np.exp(u2-u1)
    k3 = np.exp(u3-u2)
    f = np.matrix([
        [k1*u1-k2*(u2-u1)],
        [k2*(u2-u1)-k3*(u3-u2)],
        [k3*(u3-u2)-P]]) #3x1 - f

    J = np.matrix([
        [k1*(u1+1)+k2*(u2-u1+1), k2*(u1-u2-1), 0],
        [k2*(u1-u2-1), k2*(u2-u1+1)+k3*(u3-u2+1), k3*(u2-u3-1)],
        [0, k3*(u2-u3-1), k3*(u3-u2+1)]]) #3x3 - Jacobian Matrix
    
    OLD = np.matrix([[u1],[u2],[u3]]) #save old values, must be columns!
    NEW = OLD - np.linalg.solve(J,f) #make new guess
    maxf = np.max(np.abs(f))
    mxea = np.max(ea)
    u1 = NEW[0,0];u2 = NEW[1,0];u3 = NEW[2,0]
if i == maxiter:
    print('no convergence')
else:
    print(f'converged in {i} iterations')
    print(f'u1={u1:.4f},\nu2={u2:.4f},\nu3={u3:.4f},')

pylab.plot(list_i, list_maxf)
pylab.title('Residulas vs Iteration #')
pylab.xlabel('Iteration')
pylab.ylabel('Max Residuals')
pylab.grid()