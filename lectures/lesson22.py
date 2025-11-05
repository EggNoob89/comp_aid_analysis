#Lesson 22
#Interpolation w Pyhton
import pylab as pl
import numpy as np
x=np.array([1.2, 2, 3, 3.5, 4])
y=np.array([3, 24, 30, 42, 132])
xc=np.vstack(x); yc=np.vstack(y)
Z=np.hstack((np.power(xc,4), np.power(xc,3), np.power(xc,2), xc, np.ones(xc.shape)))
a=np.linalg.solve(Z,yc)
a4=a[0,0]; a3=a[1,0]; a2=a[2,0]; a1=a[3,0]; a0=a[4,0];
print('the interpolating polynomial is :\n{0:.4f}x^4+ {1:.4f}x^3+ {2:.4f}x^2+ {3:.4f}x+{4:.4f}'.format(a4,a3,a2,a1,a0))
# lambda function for interpolating polynomial
f=lambda x: a4*x**4+a3*x**3+a2*x**2+a1*x+a0
#Interpolation:
print('the interpolated value at x=2.5 is {:.4f}'.format(f(2.5)))
#Plotting
pl.scatter(x,y) #discrete data
xx=np.linspace(1.2, 4); yy=f(xx); pl.plot(xx,yy,'r')
pl.legend(['data', 'interpolating polynomial'])

#%% Interpolation w Python 
#use polyfit and polyval
import pylab as pl
import numpy as np
x=np.array([1.2, 2, 3, 3.5, 4])
y=np.array([3, 24, 30, 42, 132])
a=np.polyfit(x,y,4) #degree of polynomial is 4
#Plotting
pl.scatter(x,y, color='r') #discrete data
xx=np.linspace(np.min(x), np.max(x));
yy=np.polyval(a, xx)
pl.plot(xx,yy)
pl.legend(['data', 'interpolating polynomial'])
