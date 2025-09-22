#LESSON 3 (8.29.25 - Friday)

#%% In class coding practice 
#remember last lesson (Review)
import math

g = lambda x: (math.pi*(x**2))/4 #define function
def midpoint(f,x1,x2):
    xmid = (x1+x2)/2
    return(f(xmid))

g1 = midpoint(g,1.5,2.78)
print(g1)
#%%

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 10:04:54 2025

@author: justus-100
"""
"""
import math
import numpy as np
import pylab as pl

def bungee(t):
    g=9.81; m=68; cd=0.25
    v = np.sqrt(m*g/cd) * np.tanh(np.sqrt(cd*g/m) * t)
    return v

g=9.81; m=68; cd=0.25
bungee1 = lambda t: math.sqrt(m*g/cd)*math.tanh(math.sqrt(cd*g/m))*t

tm = np.linspace(0,20,100)
v = bungee(tm)
pl.plot(tm,v)
#pl.plot(tm,v,ls='--',c='b',marker='D')
#we can label/change axis & title"""

import math 
import numpy as np
import pylab as pl

g = lambda x : (np.pi * x ** 2) / 4
xx = np.linspace(0,10)
yy = g(xx)
pl.plot(xx,yy)