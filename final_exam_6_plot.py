import numpy as np
import matplotlib.pyplot as plt

# Function representing the differential equation
def decay_equation(n, decay_constant):
    return -decay_constant * n

# Fourth-order Runge-Kutta method for numerical integration
def runge_kutta_method(n0, decay_constant, dt, num_steps):
    time_values = np.zeros(num_steps + 1)
    number_density_values = np.zeros(num_steps + 1)

    # Initial conditions
    time_values[0] = 0
    number_density_values[0] = n0

    # Numerical integration using Runge-Kutta method
    for i in range(num_steps):
        t = time_values[i]
        k1 = dt * decay_equation(number_density_values[i], decay_constant)
        k2 = dt * decay_equation(number_density_values[i] + 0.5 * k1, decay_constant)
        k3 = dt * decay_equation(number_density_values[i] + 0.5 * k2, decay_constant)
        k4 = dt * decay_equation(number_density_values[i] + k3, decay_constant)

        time_values[i + 1] = t + dt
        number_density_values[i + 1] = (
            number_density_values[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        )

    return time_values, number_density_values

# Parameters
n0 = 40.0  # Initial number density in cm^-3
decay_constant = 2.5  # Decay constant in s^-1
dt = 0.1  # Time step in seconds
num_steps = 100  # Number of steps

# Numerical solution using Runge-Kutta method
time_values, number_density_values = runge_kutta_method(n0, decay_constant, dt, num_steps)

# Plotting the results
plt.plot(time_values, number_density_values, label='Numerical Solution')
plt.title('Decay of Particles')
plt.xlabel('Time (s)')
plt.ylabel('Number Density (cm$^{-3}$)')
plt.axhline(y=0, color='black', linestyle='--', label='Equilibrium (n=0)')
plt.legend()
plt.grid(True)
plt.show()
