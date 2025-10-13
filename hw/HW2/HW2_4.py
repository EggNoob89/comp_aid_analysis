#HW2_4

#(a)
import numpy as np
#we dont rlly need to define the equation w lambda
#just used as a reference
g = lambda x: x**4 + 65*x**3 + 86*x + 128
#create a one dimensional array of poly coefficeint
coefficients = [1, 65, 0, 86, 128]
#x^4=1 ;x^3=65; x^3=0; x^2=0; x=86; x^0=128
#since there is no x^2 term its coefficient is 0
results = np.roots(coefficients)
print(f'roots of the function g are: \n {results} \n')

#(b)
from scipy.optimize import brentq
import numpy as np 
import pylab as pl

f = lambda x: x**3-5*x+10
g = lambda x: (4*np.sin(3*x))+6

root = brentq(f,-3,2)
print(f"the root for f is f({root:.4f}) = {f(root):.4f}")

pl.title('built-in functions')
pl.xlabel('X-axis')
pl.ylabel('Y-axis')
x = np.linspace(-3,3)
pl.plot(x,f(x),label='f(x) = x^3-5x+10')
pl.plot(x,g(x),label='g(x) = 4sin(3x)+6')
#use brentq to find the point in which they intersect
#create new function f2 = f-g
f2=lambda x: f(x)-g(x)
point1 = brentq(f2,-4,-2)
point2 = brentq(f2,0,0.5)
point3 =brentq(f2,0.5,2)
print(f'point 1: ({point1:.4f}, {f(point1):.4f})')
print(f'point 2: ({point2:.4f}, {f(point2):.4f})')
print(f'point 3: ({point3:.4f}, {f(point3):.4f})')
pl.plot(point1, f(point1), 'r*', ms = 10) 
pl.plot(point2, f(point2), 'r*', ms = 10) 
pl.plot(point3, f(point3), 'r*', ms = 10) 

pl.legend()
