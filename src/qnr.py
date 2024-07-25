import numpy as np
import matplotlib.pyplot as plt

# Parameters
analysis_frequencies = np.linspace(0, 100, 500)  # Analysis frequencies in MHz
quantum_noise_power_unsqueezed = -80  # Quantum noise power in dBm for unsqueezed state
squeezing_dB = 10  # Squeezing level in dB

# Calculate noise power
unsqueezed_noise = np.full_like(analysis_frequencies, quantum_noise_power_unsqueezed)
squeezed_noise = np.full_like(analysis_frequencies, quantum_noise_power_unsqueezed - squeezing_dB)

# Convert noise power to linear scale for calculations
unsqueezed_noise_linear = 10 ** (unsqueezed_noise / 10)
squeezed_noise_linear = 10 ** (squeezed_noise / 10)

# Convert back to dBm for plotting
unsqueezed_noise_dBm = 10 * np.log10(unsqueezed_noise_linear)
squeezed_noise_dBm = 10 * np.log10(squeezed_noise_linear)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(analysis_frequencies, unsqueezed_noise_dBm, label='Unsqueezed Noise')
plt.plot(analysis_frequencies, squeezed_noise_dBm, label='Squeezed Noise', linestyle='--')

# Adding plot details
plt.xlabel('Analysis Frequency (MHz)')
plt.ylabel('Noise Power (dBm)')
plt.title('Quantum Noise: Unsqueezed vs. Squeezed')
plt.legend()
plt.grid(True)

# Show plot
plt.show()
