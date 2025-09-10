#LESSON 7 

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
while ea>=es:
    if f(xl)*f(xm)<0:
        xu = xm
    else:
        xl=xm
    old=xm
    