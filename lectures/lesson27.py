#lesson 27 
import numpy as np
from sklearn.linear_model import LinearRegression
x=np.array([1,2,3,4,5,6,7])
y=np.array([2.95, 4.72, 7.51, 12.15, 14.32, 13.14, 10.9])
xc=np.vstack(x) #or xc=np.array([x]).T
#construct X matrix
X=np.hstack((xc, np.sin(xc), np.ones(xc.shape)))
# or X = np.column_stack([x, np.sin(x),np.ones(x.shape)])
model = LinearRegression(fit_intercept=False)
model.fit(X, y)
A, B, C = model.coef_
f=lambda x: A*x+B*np.sin(x)+C
import pylab as pl #plotting
pl.scatter(x,y, color='r') #discrete data
xx=np.linspace(np.min(x), np.max(x));
pl.plot(xx,f(xx))
pl.legend(['data','model'])
r2 = model.score(X,y)
pl.text(7,12, 'r^2={0:.4f}'.format(r2))