import numpy as np
import matplotlib.pyplot as plt

"""
Author: Peyton J. Hall (C).
A python program which represents the earth's average 
radius at ground level at 31°46'40"N Latitude 
(i.e. 20906306.39764 feet).
"""

# Circle parameters
center_x = 0
center_y = -20906306.39764 
radius = 20906306.39764

# Generate points on the circle
theta = np.linspace(0, 2*np.pi, 100)
x = center_x + radius * np.cos(theta)
y = center_y + radius * np.sin(theta)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')
ax.plot(x/1000000, y/1000000, color='brown', linewidth=2)

# Set the axis labels and title
ax.set_xlabel('Distance (Millions of Feet)')
ax.set_ylabel('Distance (Millions of Feet)')
ax.set_title(r"Earth's Average Ground Level Radius at 31°46'40''N")

plt.show()
