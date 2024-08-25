import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light in m/s
central_wavelength = 800e-9  # Central wavelength of the lasers in meters (800 nm)
central_frequency = c / central_wavelength  # Central frequency

# Define the time duration for an attosecond pulse and CW laser
duration_attosecond = 100e-18  # 100 attoseconds in seconds
duration_CW = 1e-3  # 1 millisecond (effectively infinite for CW)

# Define frequency range
frequencies = np.linspace(central_frequency - 5e15, central_frequency + 5e15, 1000)

# Calculate the spectral width (Fourier transform relationship)
spectrum_attosecond = np.exp(-0.5 * ((frequencies - central_frequency) * duration_attosecond) ** 2)
spectrum_CW = np.exp(-0.5 * ((frequencies - central_frequency) * duration_CW) ** 2)

# Normalize spectra
spectrum_attosecond /= np.max(spectrum_attosecond)
spectrum_CW /= np.max(spectrum_CW)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(frequencies * 1e-15, spectrum_attosecond, label='Attosecond Pulse', color='blue')
# plt.plot(frequencies * 1e-15, spectrum_CW, label='CW Laser', color='red')
plt.title('Spectral Broadening: Attosecond Pulse')
plt.xlabel('Frequency Difference (PHz)')
plt.ylabel('Normalized Intensity')
# plt.legend()
plt.grid(True)
# plt.show()
plt.savefig('images/attosecond_spectrum.svg')
