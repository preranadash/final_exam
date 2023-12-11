import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Given data
theta_data = np.array([0.1, 0.621053, 1.142105, 1.663158, 2.184211, 2.705263, 3.226316, 3.747368, 4.268421, 4.789474, 5.310526, 5.831579, 6.352632, 6.873684, 7.394737, 7.915789, 8.436842, 8.957895, 9.478947, 10.0])
d_data = np.array([1.000000e+04, 4.174599e+01, 6.712458e+00, 2.173700e+00, 9.596581e-01, 5.050931e-01, 2.977689e-01, 1.900294e-01, 1.285873e-01, 9.101996e-02, 6.677091e-02, 5.042449e-02, 3.900668e-02, 3.079153e-02, 2.473044e-02, 2.016124e-02, 1.665176e-02, 1.391176e-02, 1.174139e-02, 1.000000e-02])

# Function for interpolation using cubic spline
def interpolate_d_cubic_spline(theta_value):
    interp_function = interp1d(theta_data, d_data, kind='cubic', fill_value='extrapolate')
    return interp_function(theta_value)

# Generate points for the interpolated curve
theta_interp = np.linspace(0.1, 10, 100)
d_interp_cubic_spline = interpolate_d_cubic_spline(theta_interp)

# Plotting the results
plt.scatter(theta_data, d_data, label='Theoretical Data', marker='o')
plt.plot(theta_interp, d_interp_cubic_spline, label='Cubic Spline Interpolation', linestyle='--')
plt.title('Cubic Spline Interpolation of Theoretical Data')
plt.xlabel('Theta')
plt.ylabel('D')
plt.legend()
plt.grid(True)
plt.show()
