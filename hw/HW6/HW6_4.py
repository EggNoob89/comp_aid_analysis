#HW6_4
import numpy as np
import pylab as pl 
from sklearn.linear_model import LinearRegression

x=np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
y=np.array([71.1, 69.1, 66.0, 69.1, 73.0, 79.0, 86.0, 93.0, 96.1, 93.9, 91.0, 82.9, 82.0])
xc=np.vstack(x) 
X = np.hstack((np.ones(xc.shape),
               np.cos((xc*np.pi)/12),
               np.sin((xc*np.pi)/12),
               np.cos((xc*np.pi)/6)))
model = LinearRegression(fit_intercept=False)
model.fit(X, y)
c1, c2, c3, c4 = model.coef_

f = lambda t: c1 + c2*np.cos((t*np.pi)/12) + c3*np.sin((t*np.pi)/12) + c4*np.cos((t*np.pi)/6)

pl.title(f'y = {c1:.2f} + {c2:.2f}cos(πt/12) + {c3:.2f}sin(πt/12) + {c4:.2f}cos(πt/6)')
pl.scatter(x,y, color='r', label='data') #discrete data
xx=np.linspace(np.min(x), np.max(x));
pl.plot(xx,f(xx), label='model')
pl.legend()
