#HW2_3

import numpy as np
import pylab as pl 

Ta = 1200; w = 10; yo = 5; y = 15 #define variable
es = 0.05
#set equation equal to 0
f = lambda x: (Ta/w) * np.cosh((w/Ta)*x) + yo - (Ta/w) - y
xi2_1 = -55; xi_1 = -40; #root1 
xi2_2 = 30; xi_2 = 60; #root2
es = 0.05

def secant(f,xi2,xi,es):
    i = 1
    ea = 100
    while ea>es:
        x_new = xi - ((f(xi)*(xi2-xi))/(f(xi2)-f(xi)))
        ea = abs((x_new-xi)/x_new)*100
        print(f'iteration({i}): x(i-1):{xi2:.4f}; xi;{xi:.4f}; x(i+1):{x_new:.4f}; f(xi-1):{f(xi2):.4f}; f(xi):{f(xi):.4f}; ea:{ea:.4f}')
        xi2 = xi
        xi = x_new
        i += 1
    print(f'the root is at f({xi:.5}) = {f(xi):.5}')
    return (xi)

root1 = secant(f, xi2_1, xi_1, es)
root2 =  secant(f, xi2_2, xi_2, es)
x = np.linspace(xi2_1-10,xi_2+10)
pl.plot(x,f(x))
pl.xlabel("X-axis")
pl.ylabel("Y-axis")
pl.title("Secant Algorithm")
pl.plot(root1, f(root1), 'r*', ms = 8) #plot star with r* and set size w ms
pl.plot(root2, f(root2), 'r*', ms = 8) #plot star with r* and set size w ms
pl.grid() #show grid and x-axis