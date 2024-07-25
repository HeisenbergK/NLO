import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 10.0  # Propagation distance
N = 1024  # Number of points in time domain
Tmax = 5.0  # Maximum time
beta2 = -1.0  # Dispersion coefficient (negative for anomalous dispersion)
gamma = 1.0  # Nonlinearity coefficient

# Time and frequency grids
t = np.linspace(-Tmax, Tmax, N)
dt = t[1] - t[0]
omega = np.fft.fftfreq(N, dt) * 2 * np.pi

# Initial condition (soliton solution)
A0 = np.sqrt(np.abs(beta2) / gamma) * np.cosh(t)

# Split-step Fourier method
def split_step_fourier(A0, L, beta2, gamma, dt, dz):
    A = A0.copy()
    steps = int(L / dz)
    linear_operator = np.exp(1j * beta2 * omega**2 * dz / 2)
    for _ in range(steps):
        # Nonlinear step
        A = A * np.exp(1j * gamma * np.abs(A)**2 * dz)
        # Linear step
        A = np.fft.ifft(np.fft.fft(A) * linear_operator)
    return A

# Simulation parameters
dz = 0.01  # Propagation step size
A_final = split_step_fourier(A0, L, beta2, gamma, dt, dz)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(t, np.abs(A0)**2, label='Initial Pulse')
plt.plot(t, np.abs(A_final)**2, label='Final Pulse after Propagation')
plt.xlabel('Time')
plt.ylabel('Intensity')
plt.title('Optical Soliton Propagation')
plt.legend()
plt.grid(True)
plt.show()
