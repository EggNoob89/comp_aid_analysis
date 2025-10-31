#HW5_2
import pylab as pl
import numpy as np
from scipy.interpolate import interp1d

x=np.array([-4,-2,0,1,2,3])
y=np.array([-10,3,8,25,52,36])
xc=np.vstack(x); yc=np.vstack(y)
Z=np.hstack((np.power(xc,5), np.power(xc,4), np.power(xc,3), np.power(xc,2), xc, np.ones(xc.shape)))
a=np.linalg.solve(Z,yc)
a5=a[0,0]; a4=a[1,0]; a3=a[2,0]; a2=a[3,0]; a1=a[4,0]; a0=a[5,0];
print(f'the interpolating polynomial is:\n{a5:.4f}x^5+ {a4:.4f}x^4+ {a3:.4f}x^3+ {a2:.4f}x^2+{a1:.4f}x+{a0:.4f}\n')

#plot the data points w a circular marker (b)
pl.scatter(x,y, label='data points')

#lambda function plot (c)
f=lambda x: a5*x**5+a4*x**4+a3*x**3+a2*x**2+a1*x+a0
xx=np.linspace(-4, 3); yy=f(xx); pl.plot(xx,yy,'r', label='interpolating polynomial')

#Plot the linear splines using interp1d in the same figure (d)
fl=interp1d(x, y, kind='linear')
yy=fl(xx); pl.plot(xx,yy, label='linear splines')

#Plot the cubic splines using interp1d in the same figure (e)
fc=interp1d(x, y, kind='cubic')
yy=fc(xx); pl.plot(xx,yy, label='cubic splines')

pl.legend()

#Interpolate at x=2.3 using the different methods of interpolation implemented in the subparts above
#and print your results with an informative statement using print. (f)
#interpolating polynomial
x = 2.3 
print(f'Interpolating Polynomial at x=2.3 : {f(x):.4f}')
print(f'Linear Splines at x=2.3 : {fl(x)}')
print(f'Cubic Splines at x=2.3 : {fc(x)}')