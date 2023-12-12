import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define tank dimensions
central_tank_radius = 4
wing_tank_radius = 2
pipe_length = 5

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-central_tank_radius-1, central_tank_radius+1)
ax.set_ylim(-central_tank_radius-1, central_tank_radius+1)

# Define the central tank
central_circle = plt.Circle((0, 0), central_tank_radius, fill=False, color='blue')
ax.add_patch(central_circle)

# Define the wing tank
wing_circle = plt.Circle((pipe_length, 0), wing_tank_radius, fill=False, color='blue')
ax.add_patch(wing_circle)

# Define the pipe
pipe = plt.Line2D([0, pipe_length], [0, 0], color='blue')
ax.add_line(pipe)

# Define the jet pump
pump = plt.Circle((0, 0), 0.1, fill=False, color='red')
ax.add_patch(pump)

# Define the update function
def update(frame):
    pump.set_center((frame/100, 0))
    return pump,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(200), interval=50, blit=True)

# Show the animation
plt.axis('equal')
plt.show()
