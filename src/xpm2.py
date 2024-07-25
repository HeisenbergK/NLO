import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# Parameters
fiber_length = 1.0  # Fiber length in meters
dz = 0.001  # Propagation step size in meters
z = np.arange(0, fiber_length + dz, dz)  # Propagation distance array
gamma = 1.3  # Nonlinear coefficient in W^-1 m^-1
beta2_probe = 0.02  # Group velocity dispersion for probe in ps^2/m
beta2_pump = 0.02  # Group velocity dispersion for pump in ps^2/m

# Time domain parameters
Tmax = 50  # Maximum time in ps
N = 2048  # Number of points
T = np.linspace(-Tmax, Tmax, N)
dt = T[1] - T[0]

# Initial probe and pump pulses
def initial_pulse(T, width, power, delay):
    return np.sqrt(power) * np.exp(-((T - delay)**2) / (2 * width**2))

probe_width = 1.0  # Pulse width in ps
probe_power = 1.0  # Probe power in W
pump_width = 1.0  # Pulse width in ps
pump_power = 5.0  # Pump power in W

# FFT frequencies
omega = np.fft.fftfreq(N, dt) * 2 * np.pi

# Split-step Fourier method for XPM
def split_step_fourier_xpm(probe_pulse, pump_pulse, z, dz, beta2_probe, gamma):
    probe_spectrum = np.fft.fft(probe_pulse)
    pump_intensity = np.abs(pump_pulse)**2
    for _ in range(len(z)):
        # Linear step for probe
        probe_spectrum *= np.exp(-0.5j * beta2_probe * omega**2 * dz)
        # Nonlinear step
        probe_pulse = np.fft.ifft(probe_spectrum)
        probe_pulse *= np.exp(1j * gamma * pump_intensity * dz)
        probe_spectrum = np.fft.fft(probe_pulse)
    return probe_pulse

# Delays for simulation
delays = np.linspace(-10, 10, 100)  # Delays in ps
frequency_shifts = []

for i in tqdm(range(len(delays))):
    delay = delays[i]
    probe_pulse = initial_pulse(T, probe_width, probe_power, 0)
    pump_pulse = initial_pulse(T, pump_width, pump_power, delay)
    
    probe_pulse_out = split_step_fourier_xpm(probe_pulse, pump_pulse, z, dz, beta2_probe, gamma)
    probe_spectrum_out = np.fft.fftshift(np.fft.fft(probe_pulse_out))
    
    # Calculate the induced frequency shift
    frequencies = np.fft.fftshift(omega) / (2 * np.pi)
    spectrum_intensity = np.abs(probe_spectrum_out)**2
    mean_frequency = np.sum(frequencies * spectrum_intensity) / np.sum(spectrum_intensity)
    
    frequency_shifts.append(mean_frequency)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(delays, frequency_shifts, marker='o')
plt.xlabel('Delay between Pump and Probe Pulses (ps)')
plt.ylabel('Induced Frequency Shift (THz)')
plt.title('Induced Frequency Shift of 532 nm Probe Pulse due to XPM with 1064 nm Pump Pulse')
plt.grid(True)
plt.show()
