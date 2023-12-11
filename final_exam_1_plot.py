import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the density function
def density_function(x):
    return 3 * x**2 / (4 * np.pi * (1 + x**2)**(5/2))

# Define the mass integral function
def mass_integral(r):
    result, _ = quad(lambda x: 4 * np.pi * x**2 * density_function(x), 0, r)
    return result

# Array of radii from 0 to 10 meters
radii = np.linspace(0, 10, 100)

# Calculate the mass enclosed for each radius
enclosed_mass_values = [mass_integral(r) for r in radii]

# Plotting the results
plt.plot(radii, enclosed_mass_values, label='Enclosed Mass')
plt.title('Enclosed Mass vs Distance from Center')
plt.xlabel('Distance from Center (m)')
plt.ylabel('Enclosed Mass (kg)')
plt.legend()
plt.grid(True)
plt.show()
