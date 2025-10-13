#HOMEWORK #3_2

import numpy as np
import pylab as pl

#part A
f_a1 = lambda x: 10*x + 6
f_a2 = lambda x: (2/3)*x**3 - 5

# Find intersection points by solving f_a1 - f_a2 = 0
coeff = [2/3 * -1, 0, 10, 11]  # -2/3 x^3 + 10x + 11 = 0
roots = np.roots(coeff)

# y-values at intersection
y_roots = f_a1(roots)

# Plot
x = np.linspace(-5, 5, 200)
pl.plot(x, f_a1(x), label='f_a1(x) = 10x + 6', color = 'red')
pl.plot(x, f_a2(x), label='f_a2(x) = 2/3 x^3 - 5', color = 'purple')
pl.plot(roots, y_roots, 'sg', label='Intersection')
pl.title('Part A')
pl.grid()
pl.legend()
pl.show()

#part B

f_b1 = lambda x: 12 + 8*x
f_b2 = lambda x: (-4/5)*x + (27/5)

A = np.array([[8, -1],
              [4, 5]])
b = np.array([-12, 27])

sol = np.linalg.solve(A, b)
x_sol, y_sol = sol
print(f'Solution for Part B: x = {x_sol}, y = {y_sol}')

# Plot
x_vals = np.linspace(-5, 5, 200)
pl.plot(x_vals, f_b1(x_vals), label='f_b1(x) = 12 + 8x')
pl.plot(x_vals, f_b2(x_vals), label='f_b2(x) = -4/5 x + 27/5')
pl.plot(x_sol, y_sol, 'sg', label='Intersection')
pl.title('Part B')
pl.grid()
pl.legend()
pl.show()
