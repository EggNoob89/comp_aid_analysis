#HW6_5
import numpy as np
import pylab as pl 
from sklearn.metrics import r2_score

c = np.array([0.5, 0.8, 1.5, 2.5, 4.0])
k = np.array([1.1, 2.5, 5.3, 7.6, 8.9])

# Linearization
x = 1 / (c ** 2)
y = 1 / k
a = np.polyfit(x,y,1)
a1 = a[0]
a0 = a[1]

kmax = 1/a0
cs = a1*kmax
f = lambda x: a1*x + a0
g = lambda x: (kmax*c**2)/(cs+c**2)

r2_1 = r2_score(y, f(x))
r2_2 = r2_score(k, g(c))

pl.figure(1)
pl.scatter(x, y, color='r', label='Linearized Data Points')
pl.plot(x, f(x), label='Linear model')
pl.title('Linearized Plot')
pl.text(2.5, .4,'r^2(linear)={0:.4f}'.format(r2_1))
pl.legend() 
pl.grid(True)

pl.figure(2)
pl.scatter(c, k, color='r', label='Original Data Points')
pl.plot(c, g(c), label='Growth model')
pl.title('Unlinearized Plot')
pl.text(2.5,4, 'r^2(growth)={0:.4f}'.format(r2_1))
pl.legend()
pl.grid(True)
