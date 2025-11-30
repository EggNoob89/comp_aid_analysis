#Lesson 23

# Polynomial Interpolation in class practice

import pylab as pl
import numpy as np
x=np.array([1, 4, 7,10 , 14, 18])
y=np.array([4, 9, 10, 22, 36, 49])
xc=np.vstack(x); yc=np.vstack(y)
Z=np.hstack((np.power(xc,5), np.power(xc,4), np.power(xc,3), np.power(xc,2), xc,
np.ones(xc.shape)))
a=np.linalg.solve(Z,yc)
a5=a[0,0]; a4=a[1,0]; a3=a[2,0]; a2=a[3,0]; a1=a[4,0]; a0=a[5,0];
f=lambda x: a5*x**5+a4*x**4+a3*x**3+a2*x**2+a1*x+a0 # interpolating polynomial
pl.scatter(x,y) #discrete data
xx=np.linspace(np.min(x), np.max(x)); yy=f(xx); pl.plot(xx,yy,'r')
pl.legend(['data', 'interpolating polynomial'])

#%%

#Polynomial Interpolation w built-in functions in class practice

import pylab as pl
import numpy as np
x=np.array([1, 4, 7,10 , 14, 18])
y=np.array([4, 9, 10, 22, 36, 49])
a=np.polyfit(x,y,5) #degree of polynomial is 5
#Plotting
pl.scatter(x,y, color='r') #discrete data
xx=np.linspace(np.min(x), np.max(x)); yy=np.polyval(a, xx)
pl.plot(xx,yy)
pl.legend(['data', 'interpolating polynomial'])

#%% Piecewise Interpolation - Linear Splines

import pylab as pl
import numpy as np
from scipy.interpolate import interp1d

x=np.array([1.2, 2, 3, 3.5, 4])
y=np.array([3, 24, 30, 42, 132])
# linear spline piecewise function
fl=interp1d(x, y, kind='linear') 
#built in function interp1d

# interpolate
x_in=1.7
y_in=fl(x_in)
print(y_in)

#Plotting
pl.scatter(x,y, color='r') #discrete data
xx=np.linspace(1.2, 4); yy=fl(xx); pl.plot(xx,yy)
pl.legend(['data', 'linear spline'])

#%% Piecewise Interpolation - Cubic Splines
#Not a knot


import pylab as pl
import numpy as np
from scipy.interpolate import interp1d
x=np.array([1.2, 2, 3, 3.5, 4])
y=np.array([3, 24, 30, 42, 132])
# cubic spline piecewise function
fc=interp1d(x, y, kind='cubic')
#Plotting
pl.scatter(x,y, color='r') #discrete data
xx=np.linspace(1.2, 4); yy=fc(xx); pl.plot(xx,yy)
pl.legend(['data', 'cubic spline'])
