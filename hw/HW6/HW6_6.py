#HW6_6

import numpy as np
import pylab as pl
from sklearn.metrics import r2_score

x = np.array([0.5, 1.25, 1.5, 2.25, 3.0, 3.2, 3.5])
y = np.array([1.2, 7.5, 11.25, 25.0, 45.0, 50.0, 65.0])

# Linear
al = np.polyfit(x, y, 1)  # y = a1*x + a0
lin = np.polyval(al, x)
r2_lin = r2_score(y, lin)

# Parabolic
aq = np.polyfit(x, y, 2)  # y = a2*x^2 + a1*x + a0
quad = np.polyval(aq, x)
r2_quad = r2_score(y, quad)

# Power
log_x = np.log(x)
log_y = np.log(y)
coeff_power = np.polyfit(log_x, log_y, 1)  # log(y) = b*log(x) + log(a)
a_power = np.exp(coeff_power[1])
b_power = coeff_power[0]
power_model = lambda t: a_power * t**b_power

#Exponential
ln_y = np.log(y)
coeff_exp = np.polyfit(x, ln_y, 1)  # ln(y) = b*x + ln(a)
a_exp = np.exp(coeff_exp[1])
b_exp = coeff_exp[0]
exp_model = lambda t: a_exp * np.exp(b_exp * t)

r2_power = r2_score(y, power_model(x))
r2_exp = r2_score(y, exp_model(x))

print(f"Linear R^2: {r2_lin:.4f}")
print(f"Parabolic R^2: {r2_quad:.4f}")
print(f"Power R^2: {r2_power:.4f}")
print(f"Exponential R^2: {r2_exp:.4f}")

print('since the Parabolic equation has the highest r^2, we will graph it')

# Best-fit model (Parabolic)
best_model = lambda t: np.polyval(aq, t)

# Predict Power at 4A
A_val = 4.0
P_pred = best_model(A_val)
print(f"\nPredicted Power at {A_val} A: {P_pred:.2f} W")

# Plot data and best-fit curve

I_plot = np.linspace(0, 4, 200)  # range for plotting

pl.figure(figsize=(8,6))
pl.scatter(x, y, color='red', label='Data Points', s=60)
pl.plot(I_plot, best_model(I_plot), color='blue', label=f'Parabolic Fit (R^2={r2_quad:.4f})', linewidth=2)
pl.scatter([A_val], [P_pred], color='green', s=100, label=f'Prediction at 4A: {P_pred:.2f} W')
pl.xlabel('Current (A)')
pl.ylabel('Power (W)')
pl.title('Joule Effect: Power vs. Current (Best-fit Parabolic)')
pl.legend()
pl.grid(True)
pl.show()