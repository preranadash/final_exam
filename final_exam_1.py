import numpy as np
from scipy.integrate import quad

# Define the density function
def density_function(x):
    return 3 * x**2 / (4 * np.pi * (1 + x**2)**(5/2))

# Define the mass integral function
def mass_integral(r):
    result, _ = quad(lambda x: 4 * np.pi * x**2 * density_function(x), 0, r)
    return result

# Radius for which to calculate the enclosed mass
radius = 2.0

# Calculate the mass enclosed within the given radius
enclosed_mass, _ = quad(mass_integral, 0, radius)

print(f"Mass enclosed within a radius of {radius}: {enclosed_mass:.4f} kg")
