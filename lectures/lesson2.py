#LESSON 2 (8.27.25 - Wednesday)

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


#you can use variables in expressions 
x = 3; y = 2 #sets variables
-x ** y 
#we get -9 bc we do the ** first
#so 3^2 = 9 and then followed by a -

#to avoid this we can use () to set a different order
(- x) ** y #returns 9 since we do -3 first and then ^2!

#%%python has built in variables

#abs takes absolute value and also magnitude
abs(-9) #returns 9
abs(3+4j) #by the adding j on the 2nd # we get both # magnitude

#round converts a floating point number into the nearest integer
round(0.6) #returns 1
round(0.5) #returns 0
round(0.51) #returns 1!
round(5.88839, 3) #rounds to 3 decimal places!

#mas returns maximum number btw 2 numbers
max(10,4) #retunrns 10

#min returns minimum number btw 2 numbers
min(10,4) #returns 4

#if you are smart about it:
x = 14 ; y = 22
max(x,y)

#%% Math module
#show blank space on source checkbox

import math

x = 10; b=2
print(math.sqrt(x)) #square root
print(math.log(x)) # ln()
print(math.log10(x)) #log10(x)
print(math.log(x,b)) #logb(x) where b is a number
print(math.exp(x)) #e^x

print(math.sin(x)) #sin, cos, tan, asin, acos, atan, atan2
print(math.sinh(x)) #sinh, cosh, tanh, asinh, acosh

#%% Bungee jumper velocity
import math

g = 9.81; m = 68.1; cd = 0.25
t = 10;
v = math.sqrt(m*g/cd)*math.tanh(math.sqrt((cd*g)/m)*t)
#tanh is a built in function
print(f"the speed given g={g}; m={m}; cd={cd}; t={t} is {round(v,3)}")
#%%you could also implement a function for it and see it in the console

import math
def bungee(t):
    g = 9.81; m=68.1; cd=0.25
    v = math.sqrt(m*g/cd)*math.tanh(math.sqrt((cd*g)/m)*t)
    return v
bungee(10)
#%% lambda functions
#can take ANY number of input arguments but ONLY ONE function can be def
#the output is a function
f = lambda x: x**3+x-1
print(f(2))

c = lambda a,b: a*b
print(c(5,6))
#%% In class coding practice - see slides
import math

g = lambda x: (math.pi*(x**2))/4 #define function
def midpoint(f,x1,x2):
    xmid = (x1+x2)/2
    return(f(xmid))

g1 = midpoint(g,1.5,2.78)
print(g1)

#apply the midpoint function created to another function

def h(w):
    return np.sin(w)*np.cosh(w)-5
#you could do the same thing using lambda a lil faster!
fmid = midpoint(h,0,3)
print('function value at midpoint =' , fmid)

