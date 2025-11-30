#CODING PROJECT 3

#%% Part a - Quadratic Polynomial Regression

import numpy as np
import pylab as pl

E = np.array([1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6]) # Strain
sigma = np.array([20, 45, 70, 150, 230, 350, 500]) # Stress

aq=np.polyfit(E,sigma,2)
aq2= aq[0]; aq1= aq[1]; aq0= aq[2]

#quality of fit (R^2)
from sklearn.metrics import r2_score
r2 = r2_score(sigma,np.polyval(aq,E))

#Plotting

pl.scatter(E,sigma, color='r', label='data points') #discrete data
xx = np.linspace(np.min(E), np.max(E)); yyq = np.polyval(aq, xx)
pl.plot(xx,yyq, label='quadratic regression')
pl.title('Soft Tissue Mechanical Testing')
pl.xlabel('Strain')
pl.ylabel('Stress')
pl.text(1.45,80,'r^2={:.4f}'.format(r2))
pl.legend()

#%% Part b 

import numpy as np
import pylab as pl
from sklearn.metrics import r2_score

E = np.array([1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6])
sigma = np.array([20, 45, 70, 150, 230, 350, 500])

# Linearization
X = E
Y = np.log(sigma)

# Linear regression Y = a + bX
b, a = np.polyfit(X, Y, 1)

k2 = b
k1 = np.exp(a)  

print(f"k1 = {k1:.4f}")
print(f"k2 = {k2:.4f}")

# Linear model for transformed data
f = lambda X: a + b*X

# Original nonlinear model fit
sigma_fit = k1 * np.exp(k2 * E)

# R^2 for nonlinear model
R2 = r2_score(sigma, sigma_fit)

fig, (ax1, ax2) = pl.subplots(2, 1, figsize=(8, 6))

# Plot 1: Linearized Data
ax1.scatter(X, Y, label='Transformed Data')
ax1.plot(X, f(X), label='Linear Fit')
ax1.set_title('Linearized Plot')
ax1.set_xlabel('E')
ax1.set_ylabel('ln(sigma)')
ax1.legend()
ax1.grid(True)

# Plot 2: Original Nonlinear Model
ax2.scatter(E, sigma, label='Original Data')
ax2.plot(E, sigma_fit, label='Nonlinear Fit: k1*exp(k2*E)')
ax2.set_title('Nonlinear Fit on Original Data')
ax2.set_xlabel('Strain')
ax2.set_ylabel('Stress')
ax2.text(1.45, 80, f'R^2 = {R2:.4f}')
ax2.text(1.25, 450, f'sigma(E) = {k1:.3f} * exp({k2:.3f} * E)')
ax2.legend()
ax2.grid(True)

pl.tight_layout()

#%% Part c 

import numpy as np
import pylab as pl
from scipy.optimize import least_squares

# Data
E = np.array([1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6])
sigma = np.array([20, 45, 70, 150, 230, 350, 500])

# Model residuals for least squares
def fun_e(params, x, y):
    k1, k2, k3, k4 = params
    return (k1/k2*np.exp(k2*x) - k3/k4*np.exp(2*k4*x)) - y

# Initial guesses (all 81 combinations)
vals = [1, 5, 10]
initial_guesses = [
    [k1_0, k2_0, k3_0, k4_0]
    for k1_0 in vals
    for k2_0 in vals
    for k3_0 in vals
    for k4_0 in vals
]

# Run least squares for all guesses
params_all = []
sse_all = []

for p0 in initial_guesses:
    sol = least_squares(fun_e, p0, args=(E, sigma), bounds=(0, np.inf)) #Pass args 
    params_all.append(sol.x)
    sse_all.append(np.sum(sol.fun**2))

# Pick best parameters
best_idx = np.argmin(sse_all)
k1, k2, k3, k4 = params_all[best_idx]

# Predicted sigma and R^2
sigma_pred = k1/k2*np.exp(k2*E) - k3/k4*np.exp(2*k4*E)
SS_res = np.sum((sigma - sigma_pred)**2)
SS_tot = np.sum((sigma - np.mean(sigma))**2)
R2 = 1 - SS_res/SS_tot

# Plot
pl.figure(figsize=(8,6))
pl.scatter(E, sigma, color='r', label='data')
xx = np.linspace(np.min(E), np.max(E), 300)
pl.plot(xx, k1/k2*np.exp(k2*xx) - k3/k4*np.exp(2*k4*xx), label='model', linewidth=2)
pl.text(1.02, 400, f"k1={k1:.3f}\nk2={k2:.3f}\nk3={k3:.3f}\nk4={k4:.3f}")
pl.text(1.02, 320, f"R^2={R2:.4f}")
pl.xlabel("E")
pl.ylabel("sigma")
pl.title("Nonlinear Regression (Part c)")
pl.grid()
pl.legend()
pl.show()

print("Best-fit parameters:", k1, k2, k3, k4)
print("R^2 =", R2)