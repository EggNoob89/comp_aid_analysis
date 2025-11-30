#HW8_3
import numpy as np; import pylab as pl
g = 9.81; R = 4; r = 0.02; h=6
dydt = lambda t,y: y*np.sin(t) 
y_exact=lambda t:2*np.exp(1-np.cos(t)); 
h=0.5 
t = np.arange(0,10+h,h) 
y = np.zeros(t.shape) 
y[0]=2 
n=len(y)
for i in range(n-1):
    phi=dydt(t[i],y[i])
    tmid = t[i]+h/2
    ymid = y[i] + phi*h/2; 
    phi_half = dydt(tmid,ymid) 
    y[i+1] = y[i] + phi_half*h
pl.figure() 
tt=np.linspace(0,10)
pl.plot(tt,y_exact(tt)); pl.plot(t,y,'o')
pl.title('midpoint method step size 0.5')
