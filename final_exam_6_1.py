import numpy as np
from scipy.integrate import odeint

# Function representing the differential equation
def decay_equation(n, t, decay_constant):
    return -decay_constant * n

# Parameters
n0 = 40.0  # Initial number density in cm^-3
decay_constant = 2.5  # Decay constant in s^-1
time_points = np.linspace(0, 10, 100)  # Time points from 0 to 10 seconds

# Numerical solution using odeint
result = odeint(decay_equation, n0, time_points, args=(decay_constant,))

# Print the numerical solution
for t, n in zip(time_points, result):
    print(f"Time: {t:.2f} s, Number Density: {n[0]:.4f} cm^-3")
