import numpy as np
import matplotlib.pyplot as plt

# Define parameters
z = np.linspace(0, 10, 500)  # Propagation distance in cm
w0cw = 0.003 # CW Beam waist at z=0
w0pw = 1 # PW Beam waist equivalent

# pw laser self-focusing (for illustration purposes, assuming Kerr effect)
n2 = 1e-6  # Nonlinear refractive index in cm^2/W
I0 = 1  # Peak intensity in W/cm^2
w_pw = w0pw / np.sqrt(1 + (z / (z**2 * n2 * I0)))

# CW laser diverging
zR = 10  # Rayleigh range in cm
w_cw = w0cw * np.sqrt(1 + (z / zR)**2)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(z, w_pw, label='PW Laser Beam Profile')
plt.plot(z, w_cw, label='CW Laser Beam Profile', linestyle='--')
# plt.axhline(y=w0cw, color='gray', linestyle=':', label='Initial Beam Waist (w0)')

# Adding plot details
plt.xlabel('Propagation Distance (z) [cm]')
plt.ylabel('Beam Waist (w) [μm]')
plt.title('Comparison of Self-Focusing PW Lasers and Diverging CW Lasers')
plt.legend()
plt.grid(True)
# plt.ylim(0, 2 * w0cw)

# Show plot
plt.show()
