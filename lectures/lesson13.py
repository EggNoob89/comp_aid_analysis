import numpy as np
A = np.matrix('-3 2; 5 1')
b = np.matrix('-9; 2')
x = np.linalg.inv(A)*b #solution

#%% 
import numpy as np
A = np.matrix('-3 2; 5 1')
b = np.matrix('-9; 2')
x = np.linalg.solve(A,b) #uses more efficient algorithm, Gaussian elimination
