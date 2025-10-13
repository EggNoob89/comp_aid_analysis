#HW2_2

import numpy as np
import pylab as pl

f = lambda x: (2*x*np.cos(2*x)) - ((x - 2)**2)
#xl = lower bound 
#xu = upper bound
es = 0.05;
xl1 = 2; xu1 = 3 #root1 
xl2 = 3; xu2 = 4 #root2


#got xl and xu by plotting graph
#f(xl) and f(xu) should be diff signs
def bisect (f,xl,xu,es):
    ea = 100 #ea could be any number
    xm_old = (xl+xu)/2 #first guess
    print(f'first guess: {xm_old}')
    i = 1 #set iteration
    while ea>es:
        if f(xl)*f(xm_old) > 0:
            xl = xm_old
        else:
            xu = xm_old
        xm_new = (xl + xu)/2 
        ea = abs(((xm_new - xm_old)/(xm_new))*100)
        print(f"iteration({i}) - new bracket: [{xl:.4f} ,{xu:.4f}]; new midpoint: {xm_new:.4f}; f({xm_new:.4f}): {f(xm_new):.4f}; ea: {ea:.4f}")
        i+=1
        xm_old = xm_new
    print(f"the root of the function is: f({xm_old:.3}) = {f(xm_old):.4f}; bracket: [{xl:.4f}, {xu:.4f}]")
    return(xm_old)

root1 = bisect(f,xl1,xu1,es)
root2 = bisect(f,xl2,xu2,es)
x = np.linspace(xl1-1,xu2+1)
pl.plot(x,f(x))
pl.xlabel("X-axis")
pl.ylabel("Y-axis")
pl.title("Bisection Algorithm")
pl.plot(root1, f(root1), 'r*', ms = 8) #plot star with r* and set size w ms
pl.plot(root2, f(root2), 'r*', ms = 8) #plot star with r* and set size w ms
pl.grid() #show grid and x-axis