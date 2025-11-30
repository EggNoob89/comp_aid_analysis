#HW8_2
import numpy as np; import pylab as pl

dydt = lambda t,y: y*np.sin(t)
y_exact=lambda t:2*np.exp(1-np.cos(t)); #analytical solution
h=0.5 #step size
t = np.arange(0,10+h,h) 
y = np.zeros(t.shape) 
y[0]=2
n=len(y)
def Euler(n,f):
    for i in range(n-1): 
        phi =f(t[i],y[i])
        y[i+1] = y[i] + phi*h 
    return y
tt=np.linspace(0,10) 
pl.plot(tt,y_exact(tt))
pl.plot(t,Euler(n,dydt),'o')
pl.title('Euler step size 0.5')