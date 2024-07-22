import numpy as np
import matplotlib.pyplot as plt

"""
Author: Peyton J. Hall (C).
A python program which represents the earth's average 
radius at ground level at 31°46'40"N Latitude 
(i.e. 3959.527726825758 miles).
"""

# Circle parameters
center_x = 0
center_y = -3959.527726825758
radius = 3959.527726825758

# Generate points on the circle
theta = np.linspace(0, 2*np.pi, 100)
x = center_x + radius * np.cos(theta)
y = center_y + radius * np.sin(theta)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')
ax.plot(x, y, color='brown', linewidth=2)

# Set the axis labels and title
ax.set_xlabel('Distance (Miles)')
ax.set_ylabel('Distance (Miles)')
ax.set_title(r"Earth's Average Ground Level Radius at 31°46'40''N")

plt.show()
