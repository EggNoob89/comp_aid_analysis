#LESSON 29
import numpy as np; import pylab as pl
from scipy.optimize import least_squares
x = np.array([1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6]) # E
y = np.array([20, 45, 70, 150, 230, 350, 500]) # sigma
def fun_e(params, x, y):
    return (params[0]/params[1]*np.exp(params[1]*x)) - y # Return residual
param_0 = np.array([1, 1]) # Initial parameter guess
sol = least_squares(fun_e, param_0, args=(x,y))
print(sol.x)
pl.scatter(x,y, color='r') #discrete data
xx=np.linspace(np.min(x), np.max(x));
pl.plot(xx,sol.x[0]/sol.x[1]*np.exp(sol.x[1]*xx))
pl.legend(['data','model']) 

#%%
import numpy as np; import pylab as pl; from scipy.optimize import least_squares
x = np.array([1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6]) # E
y = np.array([20, 45, 70, 150, 230, 350, 500]) # sigma
def error(k, x, y):
    return (k[0]/k[1]*np.exp(k[1]*x)-k[2]/k[3]*np.exp(2*k[3]*x))-y
k0 = np.array([1, 1, 1, 1]) # Initial parameter guess
sol = least_squares(error, k0, args=(x,y), bounds=([0,0,0,0], [np.inf,np.inf, np.inf, np.inf]))
print(sol.x); print(sol.cost)
pl.scatter(x,y, color='r') #discrete data
xx=np.linspace(np.min(x), np.max(x));
pl.plot(xx,sol.x[0]/sol.x[1]*np.exp(sol.x[1]*xx)-sol.x[2]/sol.x[3]*np.exp(2*sol.x[3]*xx))
pl.legend(['data','model'])