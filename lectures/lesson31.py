#LESSON 31

import numpy as np

h = np.pi / 6 # step size
x = np.arange(0, np.pi + h, h)
y = x**2 * np.sin(x)
df = np.zeros(x.shape)
df[0] = (-3 * y[0] + 4 * y[1] - y[2]) / (2 * h) #first point
df[-1] = (3 * y[-1] - 4 * y[-2] + y[-3]) / (2 * h) #last point
#can also be achieved by
df[6]=(3*y[6]-4*y[5]+y[4])/(2*h) #last point
# intermediate points using centered difference:
for i in range(1, 6):
    df[i] = (y[i + 1] - y[i - 1]) / (2 * h)
# df will have all O(h^2) results
print(df)
#%%
import numpy as np
x=np.array([1,3,5,7,9,11]); y=np.array([2,7,3,-2,6,4])
h=x[1]-x[0] # x is equally spaced
df=np.gradient(y,h)
# end corrections by manual calculations using O(h^2) formulas:
df[0]=(-y[2]+4*y[1]-3*y[0])/(2*h) #first point
df[-1]=(3*y[-1]-4*y[-2]+y[-3])/(2*h) #last point
#%%
import numpy as np
h=np.pi/6 #step size
x=np.arange(0,np.pi+h,h); y=x**2*np.sin(x)
h=x[1]-x[0] # x is equally spaced
df=np.gradient(y,h)
# end corrections by manual calculations using O(h^2) formulas:
df[0]=(-y[2]+4*y[1]-3*y[0])/(2*h) #first point
df[-1]=(3*y[-1]-4*y[-2]+y[-3])/(2*h) #last point
print(df)