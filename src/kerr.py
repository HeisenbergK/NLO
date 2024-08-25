import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# Constants
c = 3e8  # speed of light in vacuum (m/s)
wavelength = 800e-9  # wavelength of the laser (m)
tau = 1e-18  # pulse duration (1 attosecond)
E0 = 1e10  # peak electric field (V/m)
n2 = 1e-20  # Kerr coefficient (m^2/W)
z0 = 1e-3  # initial beam waist (m)
L = 1e-3  # propagation distance (m)
dz = 1e-6  # step size for z (m)

# Temporal grid
t = np.linspace(-10*tau, 10*tau, 1000)
dt = t[1] - t[0]

# Gaussian pulse
pulse = E0 * np.exp(-t**2 / (2 * tau**2)) * np.cos(2 * np.pi * c / wavelength * t)

# Spatial grid
x = np.linspace(-10*z0, 10*z0, 1000)
dx = x[1] - x[0]
X, T = np.meshgrid(x, t)

# Initial beam profile
beam_profile = np.exp(-X**2 / (2 * z0**2))

# Intensity of the pulse
I = pulse[:, np.newaxis]**2 * beam_profile

# Propagation loop
loop = np.arange(0, L, dz)
for i in tqdm(range(len(loop))):
    # Set z position
    z = loop[i]

    # Nonlinear phase shift due to Kerr effect
    phase_shift = n2 * I * dz
    
    # Apply the phase shift
    pulse = pulse * np.exp(1j * phase_shift.mean(axis=1))
    
    # Update intensity
    I = pulse[:, np.newaxis]**2 * beam_profile

# Plot the temporal profile of the pulse
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(t, np.abs(pulse)**2)
plt.title('Temporal Profile of the Pulse')
plt.xlabel('Time (s)')
plt.ylabel('Intensity (W/m^2)')

# Plot the spatial profile showing self-focusing
plt.subplot(1, 2, 2)
plt.imshow(np.abs(pulse[:, np.newaxis] * beam_profile.T)**2, extent=[x.min(), x.max(), t.min(), t.max()], aspect='auto', cmap='hot')
plt.title('Spatial Profile Showing Self-Focusing')
plt.xlabel('Position (m)')
plt.ylabel('Time (s)')
plt.colorbar(label='Intensity (W/m^2)')

plt.tight_layout()
# plt.show()
plt.savefig('images/kerr_profiles.svg')
