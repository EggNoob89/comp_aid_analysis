#Lesson 24

import pylab as pl; import numpy as np
from scipy.interpolate import interp1d
x=np.array([1.2, 2, 3, 3.5, 4, 4.5])
y=np.array([50, 40, 42, 80, 30, 0])
a=np.polyfit(x,y, 5)
fc=interp1d(x, y, kind='cubic')
fl= interp1d(x, y, kind='linear')
pl.scatter(x,y, color='r') #discrete data
xx=np.linspace(1.2, 4.5);
pl.plot(xx, np.polyval(a, xx)); pl.plot(xx, fc(xx)); pl.plot(xx, fl(xx))
pl.legend(['data', 'polynomial', 'cubic', 'linear'])
#%%
import numpy as np
from scipy.interpolate import interp1d
import pylab as pl
u1=1.32; u2=1.89; u3=4.67
x=[1,2,3]; u=[u1,u2,u3]
pl.scatter(x,u,c='r')
fl=interp1d(x, u, kind='linear')
xx=np.linspace(1, 3);
pl.plot(xx, fl(xx))
pl.legend(['data', 'linear FE'])