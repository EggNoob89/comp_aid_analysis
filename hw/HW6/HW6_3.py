#HW6_3

#Plot the data points as well as the regression curves 
#Straight line and cubic curve
import numpy as np 

x=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y=np.array([26.7,20.2,16.8,15.3,15.1,9.3,5.1,2.8,-1.1,-8.4])
al=np.polyfit(x,y,1) #y=a1*x+a0
aq=np.polyfit(x,y,3) #y=a3*x^3+a2*x^2+a1*x+a0

#Plotting
import pylab as pl
pl.scatter(x,y, color='r', label='data') #discrete data
xx=np.linspace(np.min(x), np.max(x));
yyl=np.polyval(al, xx); yyc=np.polyval(aq,xx)
pl.plot(xx,yyl,'b',label='linear'); pl.plot(xx,yyc,'g',label='cubic')
pl.legend()
pl.title('Polynomial Regression')

#Using the function r2_score compute the coefficient of determination, r^2 for both regression models
#and place it on the plot using the text command.
from sklearn.metrics import r2_score
r2_1=r2_score(y,np.polyval(al,x))
r2_2=r2_score(y,np.polyval(aq,x))
pl.text(6.5,9, 'r^2(linear)={0:.4f}\nr^2(cubic)={1:.4f}\n'.format(r2_1,r2_2))

y1 = np.polyval(al, 7.2)
y2 = np.polyval(aq, 7.2)
if r2_1 > r2_2:
    print('Linear Regression is a better fit')
    print(f'the value of y when x = 7.2 is {y1:.4f}')
else:
    print('Cubic Regression is a better fit')
    print(f'Value of y when x = 7.2 is {y2:.4f}')