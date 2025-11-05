#lesson 25
import numpy as np 

x=np.array([10, 20, 30, 40, 50, 60])
y=np.array([25, 70, 360, 550, 610, 740])
al=np.polyfit(x,y,1) #y=a1*x+a0
al1=al[0]; al0=al[1]
aq=np.polyfit(x,y,2) #y=a2*x^2+a1*x+a0
aq2 = aq[0]; aq1 = aq[1]; aq0 = aq[2]
#Plotting
import pylab as pl
pl.scatter(x,y, color='r') #discrete data
xx=np.linspace(np.min(x), np.max(x));
yyl=np.polyval(al, xx); yyq=np.polyval(aq,xx)
pl.plot(xx,yyl,'b'); pl.plot(xx,yyq,'g')
pl.legend(['data', 'linear', 'quadratic'])
pl.title('polynomial regression')