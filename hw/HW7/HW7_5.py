#HW7_5

import numpy as np
from scipy.integrate import quad

L=0.2 #meters
theta0=30 #degrees

theta0_rad=theta0*np.pi/180 #convert to radians

k = np.sin(theta0_rad); g=9.81

#compute the integral term
f = lambda x: 1 / np.sqrt(1-(k)**2*(np.sin(x))**2)  

I,e = quad(f,0,np.pi/2)
#compute T
T = 4*np.sqrt(L/g)*I

print('The pendulum period is {:.4f} sec'.format(T))
