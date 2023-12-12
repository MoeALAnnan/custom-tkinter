import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()
x_data = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x_data, np.sin(x_data))

# Define the update function for the animation
def update(frame):
    line.set_ydata(np.sin(x_data + frame / 10))
    return line,


# Create the animation
ani = FuncAnimation(fig, update, frames=range(200), blit=True, interval=20)

# Show the animation
plt.show()

