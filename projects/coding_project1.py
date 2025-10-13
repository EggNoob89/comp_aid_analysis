#%%CODING PROJECT
#Part 1-3

print("Bryan Bejoy")
print("11943562")

from scipy.optimize import brentq
import numpy as np 
import pylab as pl 

#funcion f where x = I
f = lambda x: (3/2)*x**2 + 2*x - np.exp(x**3)  
fd = lambda x: (3*x) + 2 - (3*x**2)*np.exp(x**3)
x = np.linspace(0, 1, 100); xl = 0; xu = 1
sol = brentq(fd, 1, 0)
print(f'the optimal current is at x = {sol:.4f} and y = {f(sol):.4f}')
#plot graph and point
pl.plot(x, f(x))
pl.xlabel("Current")
pl.ylabel("Efficiency")
pl.title("Optimal Current Graph")
pl.plot(sol, f(sol), 'r*', ms = 8)
pl.grid()

#%% Part 4
print("Bryan Bejoy")
print("11943562")

import numpy as np 
import pylab as pl


f = lambda x: (3/2)*x**2 + 2*x - np.exp(x**3)
fd = lambda x: (3*x) + 2 - (3*x**2)*np.exp(x**3)

x = np.linspace(0, 1, 100); xl = 0; xu = 1; n = 4

def false_position(f,xl,xu,n):
    xr = xu-f(xu)*(xl-xu)/(f(xl)-f(xu)) #first guess
    es = 0.5*10**(2-n) #initialize
    ea = 100
    i = 1
    print(f'brackets: [{xl:.4f}, {xu:.4f}], xr = {xr:.4f}, es = {es:.4f}, iteration: {i}')
    while ea > es:
        if f(xl)*f(xr) < 0: #if true, root is the first half of the bracket
            xu = xr
        else:
            xl=xr
        old = xr; #save old value
        xr = xu-f(xu)*(xl-xu)/(f(xl)-f(xu))
        ea = abs((xr-old)/xr)*100
        i += 1
        print(f'brackets: [{xl:.4f}, {xu:.4f}], xr = {xr:.4f}, ea = {ea:.4f}, es = {es:.4f}, iteration: {i}')
    return (xr,i)


sol,i = false_position(fd,xl,xu,n)

print(f'the optimal current is at x = {sol:.4f} and y = {f(sol):.4f} found in {i} iterations')

#plot graph and point
pl.plot(x, f(x))
pl.xlabel("Current")
pl.ylabel("Efficiency")
pl.title("Optimal Current Graph")
pl.plot(sol, f(sol), 'r*', ms = 8)
pl.grid()

#%% Part 5
print("Bryan Bejoy")
print("11943562")

import numpy as np 
import pylab as pl


f = lambda x: (3/2)*x**2 + 2*x - np.exp(x**3)
fd = lambda x: (3*x) + 2 - (3*x**2)*np.exp(x**3)

x = np.linspace(0, 1, 100); xl = 0; xu = 1; n = 4

def illinois(f,xl,xu,n):
    u = 1
    xr = xu- (f(xu)*(xl-xu)/(f(xl)-f(xu))) #first guess
    es = 0.5*10**(2-n) #initialize
    ea = 100
    i = 1
    print(f'brackets: [{xl:.4f}, {xu:.4f}], xr = {xr:.4f}, es = {es:.4f}, iteration: {i},')
    while ea > es:
        if f(xl)*f(xr) < 0: #if true, root is the first half of the bracket
            xu = xr
            u = 0
        else:
            xl=xr
            u = 1
        old = xr; #save old value
        if u == 1:
            xr = xu - ((1/2*(f(xu)*(xl-xu)))/(f(xl)-(1/2)*f(xu)))
        else:
            xr = xu - (f(xu)*(xl-xu)/((1/2*f(xl))-f(xu)))            
        ea = abs((xr-old)/xr)*100
        i += 1
        print(f'brackets: [{xl:.4f}, {xu:.4f}], xr = {xr:.4f}, ea = {ea:.4f}, es = {es:.4f}, iteration: {i}')
    return (xr,i)


sol,i = illinois(fd,xl,xu,n)

print(f'the optimal current is at x = {sol:.4f} and y = {f(sol):.4f} found in {i} iterations')

#plot graph and point
pl.plot(x, f(x))
pl.xlabel("Current")
pl.ylabel("Efficiency")
pl.title("Optimal Current Graph")
pl.plot(sol, f(sol), 'r*', ms = 8)
pl.grid()