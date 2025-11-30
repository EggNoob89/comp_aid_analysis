#lesson 26 implement r^2
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10])
y=np.array([12,15,16,18,19,20,22,31,38,42])
# lets try out a quadratic model
aq=np.polyfit(x,y,2) #y=a2*x^2+a1*x+a0
fq = lambda x: np.polyval(aq,x)
#quality of fit
from sklearn.metrics import r2_score
r2=r2_score(y,fq(x))
import pylab as pl
pl.scatter(x,y, color='r') #discrete data
xx=np.linspace(np.min(x), np.max(x));
pl.plot(xx,fq(xx)) # or pl.plot(xx, np.polyval(aq, xx))
pl.text(7,15, 'r^2={:.4f}'.format(r2))
#%% In-Class Practice
import numpy as np
x=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y=np.array([8, 1, 9, 13, 45, 50, 120, 115, 210, 300])
a1=np.polyfit(x,y,1); a3=np.polyfit(x,y,3); a8=np.polyfit(x,y,8)
from sklearn.metrics import r2_score
r21=r2_score(y, np.polyval(a1, x)) #quality of fit
r23=r2_score(y, np.polyval(a3, x))
r28=r2_score(y, np.polyval(a8, x))
import pylab as pl
pl.scatter(x,y, color='r') #discrete data
xx=np.linspace(0.7, 10.3)
pl.plot(xx, np.polyval(a1, xx)); pl.plot(xx, np.polyval(a3, xx)); pl.plot(xx, np.polyval(a8,
xx))
pl.legend(['data', 'linear', 'cubic', '8th degree'])
pl.text(8,0, 'r^2={0:.4f}\nr^2={1:.4f}\nr^2={2:.4f}'.format(r21,r23,r28))