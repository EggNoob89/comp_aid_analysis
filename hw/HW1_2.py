#Coding Problem 1.2

import numpy as np 
import pylab

A = 30; B = 40; m = -0.276
t = np.array([0.5,3,7,11,15])
tf = A + (B * np.exp(m*t)) #try not to mix math with numpy
t2 = np.array([85,48,35,33,31])

pylab.plot(t,tf,c='r',label='model')
pylab.plot(t,t2,'o',label='data') #to get only dots use 'o' alone
pylab.title('Temperature Curves')
pylab.xlabel('Time (min)')
pylab.ylabel('Temperature (C)')
pylab.legend(loc='upper right')
pylab.grid()