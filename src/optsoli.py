import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft, fftshift

# Constants and Parameters
L = 1.0  # Length of the medium (in arbitrary units)
N = 1024  # Number of grid points
dz = 0.01  # Propagation step size
nz = int(L / dz)  # Number of steps in propagation
beta2 = -1.0  # Group velocity dispersion (GVD) parameter
gamma = 1.0  # Nonlinearity parameter

# Remap ticks
def remap(useless, tick):
    return round(100*(useless-0.99),1)

# Time/Frequency domain
Tmax = 10
T = np.linspace(-Tmax, Tmax, N)  # Time grid
dt = T[1] - T[0]  # Time step
omega = 2 * np.pi * np.fft.fftfreq(N, d=dt)  # Frequency grid

# Initial condition: fundamental soliton
A0 = 1/np.cosh(T)

# Precompute phase shifts for efficiency
D = np.exp(-0.5j * beta2 * omega**2 * dz)  # Dispersion phase shift
N_phase = lambda A: np.exp(1j * gamma * np.abs(A)**2 * dz)  # Nonlinear phase shift

# Initialize field
A = A0.copy()

# Store results for visualization
A_z = np.zeros((nz, N), dtype=complex)
A_z[0, :] = A

# Propagation loop using SSFM
for i in range(1, nz):
    A = ifft(D * fft(A))  # Linear step (dispersion)
    A = N_phase(A)  # Nonlinear step
    A_z[i, :] = A

# Plot results
plt.figure(figsize=(10, 6))

# # Intensity plot
# plt.subplot(2, 1, 1)
plt.imshow(np.abs(A_z)**2, extent=[-Tmax, Tmax, 0, L], aspect='auto', cmap='inferno')
plt.ylim([0.99, 1])
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(remap))
plt.colorbar(label='Intensity |A|^2')
plt.xlabel('Time')
plt.ylabel('Propagation Distance')
plt.title('Optical Soliton Propagation in Nonlinear Medium')

# # Final pulse shape
# plt.subplot(2, 1, 2)
# plt.plot(T, np.abs(A_z[0, :])**2, label='Input Pulse')
# plt.plot(T, np.abs(A_z[5, :])**2, label='Output Pulse')
# plt.xlabel('Time')
# plt.ylabel('Intensity |A|^2')
# plt.legend()

plt.tight_layout()
# plt.show()
plt.savefig('images/soliton_propagation.svg')
