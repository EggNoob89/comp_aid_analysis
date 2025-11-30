#HW7_6

import numpy as np
import pylab as pl

# Data
t = np.array([10, 20, 30, 40, 50, 60])
c = np.array([3.52, 2.48, 1.75, 1.23, 0.87, 0.61])

# Derivative
dc = -np.gradient(c, t)  # minus bc dc/dt is negative

# Linear regression ln(-dc/dt) = ln(k) + n ln(c)
x = np.log(c)
y = np.log(dc)
p = np.polyfit(x, y, 1)
n = p[0]
k = np.exp(p[1])

print(f"n = {n:.4f}")
print(f"k = {k:.4f}")

# Solve dc/dt = -k c^n numerically
t_fit = np.linspace(t[0], t[-1], 300)
c_fit = np.zeros_like(t_fit)
c_fit[0] = c[0]

dt_fit = t_fit[1] - t_fit[0]
for i in range(1, len(t_fit)):
    c_fit[i] = c_fit[i-1] - k * c_fit[i-1]**n * dt_fit

# Plot
pl.plot(t, c, "ko", label="Data")
pl.plot(t_fit, c_fit, label="Model")
pl.xlabel("Time")
pl.ylabel("Concentration")
pl.title("Chemical Reaction Model")
pl.grid(True)
pl.legend()
pl.show()
