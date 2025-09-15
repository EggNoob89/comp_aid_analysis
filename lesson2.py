#LESSON 2

#%% Subscripts
#review from previous lesson!!

import numpy as np 
x = np.array([12.2, 10.9, 13.6, 8.4, 11.1])
print(x[0]) #subscript starts from 0 as usual 
print(x[1])
print(x[0:2]) #notice that it does not include the upper limit!
x[3:5]
#use print if you want to also run the previous values!
#you could also run this code using the console!!
#%% IPython Console Features

#in the console you can press the up arrow to go back 
#if you dont know a command simply type help(x) where x is the command or var
#e.g help(int)

#%% Different types of functions

#arange function
#np.arange(x1,x2,dx)
#creates an array that starts with x1 in steps of dx up to but not including x2
import numpy as np
x = np.arange(0,1,0.1)
#to also include x2 we can say array to x2 + dx
x1 = np.arange(0,1.1,0.1)

#linspace function
#n equally-spaced points from x1 to x2
import numpy as np 
d = np.linspace(1,100,8) #100 or x2 is included!

#mathematical operators

"""
+ = addition
- = substraction 
* = multiplication
/ = division (floating point)
// = divion (integer)
% = remainder of a division
** = exponentiation
"""

#order of operations 
#expressions are evaluated from left to right and within parentheses
# ** is the highest order
# -(unary)
# *,/,//,%
# +,- lowest
#%%Mathematical Operations - Part 2

import numpy as np 
#computes area of a circle of a diameter 0.5
#Area of a circle = pi r^2
#so pi(0.5/2)^2 since 0.5 is the radius
x = np.pi * 0.5**2 / 4
#0.5 is result1 cause of ** having a higher priority 
#np.pi * result1 is result2 since left to right
#result2/4 is the final result

#we could also divide prior and get the same result
y = np.pi * 0.25**2

#if you want to be fancy you could even use parentheses
z = np.pi * (0.5/2)**2
#%%
"""import math
g=9.81; m=68.1; cd=0.25
t=10

def bungee(t):
    g=9.81; m=68.1; cd=0.25
    v = math.sqrt(m*g/cd)*math.tanh(math.sqrt(cd*g/m)*t)
    return v

g=9.81; m=68.1; cd=0.25
bungee1 = lambda t: math.sqrt(m*g/cd)*math.tanh(math.sqrt(cd*g/m)*t)
print(bungee(10))
print(bungee1(10))"""


import numpy as np 

g = lambda x: (np.pi * x**2)/4

import numpy as np

def midpoint(f, x1, x2):
    xmid = (x1+x2)/2
    return f(xmid)

print(midpoint(g, 1.5, 2.78))
#takes midpoint value between 1.5 and 2.78 and then plugs into the earlier function g!

