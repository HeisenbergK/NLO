import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
c = 3e8  # Speed of light in m/s
n = 1.5  # Refractive index of the crystal
L = 10.0  # Length of the crystal in mm
z = np.linspace(-L/2, 3*L/2, 500)  # Propagation distance in mm
k1 = 2 * np.pi / 1.0  # Wave number for the fundamental wave (arbitrary units)
k2 = 2 * k1  # Wave number for the second harmonic (arbitrary units)
E1_0 = 1.0  # Initial electric field amplitude of the fundamental wave
deff = 5  # Effective nonlinear coefficient in arbitrary units
omega = 2 * np.pi  # Angular frequency of the fundamental wave

# Time parameters
t_max = 2 * np.pi / omega  # Time period of the wave
num_frames = 100  # Number of frames in the animation
times = np.linspace(0, t_max, num_frames)

# Initialize electric fields
E1 = np.zeros((len(z), num_frames))
E2 = np.zeros((len(z), num_frames))

# Calculate electric fields
for i, t in enumerate(times):
    for j, zj in enumerate(z):
        E1[j, i] = E1_0 * np.cos(k1 * zj - omega * t)
        if zj >= 0 and zj <= L:
            # E2[j, i] = E1_0*(zj/L)* np.cos(k2 * zj - omega * t)
            E2[j, i] = E1_0*np.tanh(3*zj/L)* np.cos(k2 * zj - omega * t)
            E1[j, i] = E1_0*(1-(0.75*(zj/L)))* np.cos(k1 * zj - omega * t)
        elif zj < 0:
            E2[j, i] = 0
            E1[j, i] = E1_0 * np.cos(k1 * zj - omega * t)
        elif zj > L:
            E2[j, i] = E1_0*np.tanh(3)* np.cos(k2 * zj - omega * t)
            E1[j, i] = E1_0*0.25* np.cos(k1 * zj - omega * t)

# Set up the figure and axis
fig, ax = plt.subplots()
line1, = ax.plot([], [], 'b-', label='Fundamental Wave')
line2, = ax.plot([], [], 'r-', label='Second Harmonic Wave')
crystal_location = ax.axvspan(0, L, color='gray', alpha=0.2, label='Crystal Location')
ax.set_xlim(-L/2, 3*L/2)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('Propagation Distance (mm)')
ax.set_ylabel('Electric Field Amplitude')
ax.set_title('Second Harmonic Generation in a $\chi^{(2)}$ Crystal')
ax.legend()
ax.grid(True)

# Initialization function for the animation
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

# Animation function
def animate(i):
    line1.set_data(z, E1[:, i])
    line2.set_data(z, E2[:, i])
    return line1, line2

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init, blit=True, interval=50)

# Display the animation
plt.show()
