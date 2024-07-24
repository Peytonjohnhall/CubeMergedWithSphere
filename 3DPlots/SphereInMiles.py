import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
Author: Peyton J. Hall (C).
A python program which represents the earth's average 
radius at ground level at 31°46'40"N Latitude 
(i.e. 3959.527726825758 miles).
"""

# Sphere parameters
center_x = 0
center_y = 0
center_z = 0
radius = 3959.527726825758

# Generate points on the sphere
phi, theta = np.linspace(0, np.pi, 100), np.linspace(0, 2 * np.pi, 100)
phi, theta = np.meshgrid(phi, theta)
x = center_x + radius * np.sin(phi) * np.cos(theta)
y = center_y + radius * np.sin(phi) * np.sin(theta)
z = center_z + radius * np.cos(phi)

# Create the plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='brown', rstride=5, cstride=5, alpha=0.5)

# Set the axis labels and title
ax.set_xlabel('Distance (Miles)')
ax.set_ylabel('Distance (Miles)')
ax.set_zlabel('Distance (Miles)')
ax.set_title(r"Earth's Average Ground Level Radius at 31°46'40''N")

plt.show()
