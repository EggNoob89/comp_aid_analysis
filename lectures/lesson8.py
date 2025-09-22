#LESSON 8

#%% Bisection Method: PYTHON Code

import numpy as np
import pylab as pl 

f = lambda x: 10*np.cos(x)-x
x = np.linspace(5.5,8.5,100)
y = f(x)
pl.plot(x,y)
pl.grid()
xl=7;xu=8
xm=(xl+xu/2)
n = 3; es = 0.5*10**(2-n)
ea = 100 
while ea>=es:
    if f(xl)*f(xm)<0:
        xu = xm
    else:
        xl=xm
    old=xm
    xm=(xl+xu)/2
    ea=abs((xm-old)/xm)*100
print('the root of interval [{0:.4f}, {1:.4f}] correct of {2:g} sig figs is {3:.2f}'. format(xl, xu, n, xm))


#%% In-class Practice

import numpy as np
import pylab as pl 

f = lambda x: x**3-x**2-5
x = np.linspace(5.5,8.5,100)
y = f(x)
pl.plot(x,y)
pl.grid()
xl=7;xu=8
xm=(xl+xu/2)
n = 3; es = 0.5*10**(2-n)
ea = 100 
while ea>=es:
    if f(xl)*f(xm)<0:
        xu = xm
    else:
        xl=xm
    old=xm
    xm=(xl+xu)/2
    ea=abs((xm-old)/xm)*100
print('the root of interval [{0:.4f}, {1:.4f}] correct of {2:g} sig figs is {3:.2f}'. format(xl, xu, n, xm))