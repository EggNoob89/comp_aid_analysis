#LESSON 1

#Went over syllabus

#%% Assignment of Values to Variables

a = 4
A = 6
#notice that variable names are a and A are BOTH different
#also the default type for both is integers

#multiple assignments on one line

y = 3.45 ; z = 1/3

#notice that the numeric type is a float w decimal fraction or point

#%% Predefined Variables

import numpy 

numpy.pi #floating number stored to 16 sig figs!
# ctrl + enter to run the cell
numpy.e 

import numpy as np #np is used as a shortcut
np.e

#%% NumPy Array

#an array is a single data type indexed by integer subscripts
#np.array is more efficient than a list
#np.array can also use built-in functions
import numpy as np
x = np.array([12.2, 10.9, 13.6, 8.4, 11.1])
x #array is printed into the console

#%% Subscripts

import numpy as np 
x = np.array([12.2, 10.9, 13.6, 8.4, 11.1])
print(x[0]) #subscript starts from 0 as usual 
print(x[1])
print(x[0:2]) #notice that it does not include the upper limit!
x[3:5]
#use print if you want to also run the previous values!