#HW7_4
import numpy as np
from scipy.integrate import simpson

h = 0.25
t = np.arange(0, 15 + h, h)

# vectorized velocity function
def v(t):
    return np.where(t <= 5, 4*t, 20 + (5 - t)**2)

vel = v(t)

# Simpson's rule 
s_sim = simpson(vel, x=t)
W_sim = 200 * s_sim

# trapezoidal rule 
s_trap = np.trapz(vel, t)
W_trap = 200 * s_trap

print(f"Displacement - Simpson: {s_sim:.4f}")
print(f"Displacement - trapezoid: {s_trap:.4f}")
print(f"Work - Simpson: {W_sim:.4f}")
print(f"Work - trapezoid: {W_trap:.4f}")
