import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 10.0  # Fiber length in km
dz = 0.01  # Propagation step size in km
z = np.arange(0, L + dz, dz)  # Propagation distance array
gamma = 1.3  # Nonlinear coefficient in W^-1 km^-1

# Initial intensities (in W)
I_s0 = 1.0  # Initial signal intensity
I_p0 = 5.0  # Initial pump intensity

# Initial phase
phi_s0 = 0.0  # Initial phase of the signal

# Initialize intensity and phase arrays
I_s = np.zeros_like(z)
I_p = np.zeros_like(z)
phi_s = np.zeros_like(z)

I_s[0] = I_s0
I_p[0] = I_p0
phi_s[0] = phi_s0

# Cross-phase modulation simulation
for i in range(1, len(z)):
    dphi_s = gamma * I_p[i-1] * dz  # Phase shift due to XPM
    phi_s[i] = phi_s[i-1] + dphi_s
    # Assume constant intensities for simplicity
    I_s[i] = I_s0
    I_p[i] = I_p0

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(z, phi_s, label='Signal Phase')
plt.xlabel('Propagation Distance (km)')
plt.ylabel('Phase (radians)')
plt.title('Cross-Phase Modulation in a Fiber')
plt.legend()
plt.grid(True)
plt.show()
