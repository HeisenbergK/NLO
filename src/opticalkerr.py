import numpy as np
import matplotlib.pyplot as plt

# Define parameters
z = np.linspace(0, 10, 1000)  # Propagation distance in cm
w0 = 100  # Beam waist at z=0 in µm
n0 = 1.5  # Linear refractive index
n2 = 1e-16  # Nonlinear refractive index in cm^2/W
I0 = 1e10  # Peak intensity in W/cm^2

# Calculate intensity profile
def intensity_profile(z, w0, I0):
    zR = np.pi * (w0**2) / 1e4  # Rayleigh range in cm (1e4 to convert µm² to cm²)
    wz = w0 * np.sqrt(1 + (z / zR)**2)  # Beam radius at z
    Iz = I0 * (w0 / wz)**2  # Intensity at z
    return wz, Iz

# Calculate refractive index change due to Kerr effect
def refractive_index_change(Iz, n0, n2):
    return n0 + n2 * Iz

# Compute intensity profile and refractive index change
wz, Iz = intensity_profile(z, w0, I0)
nz = refractive_index_change(Iz, n0, n2)

# Plotting
plt.figure(figsize=(12, 8))

# Beam radius
plt.subplot(2, 1, 1)
plt.plot(z, wz, label='Beam Radius (wz)', color='blue')
plt.axhline(y=w0, color='gray', linestyle=':', label='Initial Beam Waist (w0)')
plt.xlabel('Propagation Distance (z) [cm]')
plt.ylabel('Beam Radius (wz) [µm]')
plt.title('Beam Profile and Refractive Index Change due to Optical Kerr Effect')
plt.legend()
plt.grid(True)

# Refractive index change
plt.subplot(2, 1, 2)
plt.plot(z, nz, label='Refractive Index (nz)', color='red')
plt.axhline(y=n0, color='gray', linestyle=':', label='Linear Refractive Index (n0)')
plt.xlabel('Propagation Distance (z) [cm]')
plt.ylabel('Refractive Index (nz)')
plt.legend()
plt.grid(True)

# Show plot
plt.tight_layout()
# plt.show()
plt.savefig('images/kerr_index.svg')
