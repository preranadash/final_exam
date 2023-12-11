import numpy as np
from scipy.interpolate import interp1d

# Given data
theta_data = np.array([0.1, 0.621053, 1.142105, 1.663158, 2.184211, 2.705263, 3.226316, 3.747368, 4.268421, 4.789474, 5.310526, 5.831579, 6.352632, 6.873684, 7.394737, 7.915789, 8.436842, 8.957895, 9.478947, 10.0])
d_data = np.array([1.000000e+04, 4.174599e+01, 6.712458e+00, 2.173700e+00, 9.596581e-01, 5.050931e-01, 2.977689e-01, 1.900294e-01, 1.285873e-01, 9.101996e-02, 6.677091e-02, 5.042449e-02, 3.900668e-02, 3.079153e-02, 2.473044e-02, 2.016124e-02, 1.665176e-02, 1.391176e-02, 1.174139e-02, 1.000000e-02])

# Function for interpolation
def interpolate_d(theta_value):
    # Create an interpolation function
    interp_function = interp1d(theta_data, d_data, kind='linear', fill_value='extrapolate')

    # Interpolate the value at the given theta
    interpolated_d = interp_function(theta_value)

    return interpolated_d

# Test the function with an arbitrary value of theta
theta_value = 3.0
result_d = interpolate_d(theta_value)
print(f"For theta = {theta_value}, interpolated d = {result_d:.6f}")
