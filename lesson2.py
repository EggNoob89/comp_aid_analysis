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

