#HW5_3
import pylab as pl
import numpy as np
from scipy.interpolate import interp1d

x=np.array([0,30,60,150,240])
y=np.array([800,457,269,79,46])

#plot data as discrete points
pl.scatter(x,y, label='data points')


# interpolating polynomial, using polyfit and polyval (a)
a=np.polyfit(x,y,4) 
#degree of polynomial is 4 (n-1) 
xx=np.linspace(np.min(x), np.max(x));
yy=np.polyval(a, xx)
pl.plot(xx,yy,'c-', label='interpolating polynomial')

# piecewise cubic interpolation - not-a-knot (b)

fc=interp1d(x, y, kind='cubic')
yy=fc(xx) 
pl.plot(xx,yy,'m-',label='cubic spline')

pl.xlabel('Time (sec)')
pl.ylabel('Temp (C)')
pl.title('Ball Bearing Cooling Process')
pl.legend()
pl.show()

#Looking at the plot, choose the method you believe to be the best and smoothest fit to predict the
#temperature after 3 minutes of cooling.
t = 180 #3 minutes in seconds
poly_valt = np.polyval(a, t)
print(f'polynomial (t=180): {poly_valt:.4f} ')
print(f'cubic (t=180): {fc(t):.4f}') 
print('Looking at the graph the cubic spline seems to be smoother')
print(f'Hence the right value of the temperature would be: {fc(t):.4f}') 