import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
Author: Peyton J. Hall (C).
A python program which represents the earth's average 
radius at ground level at 31°46'40"N Latitude 
(i.e. 20906306.39764 feet).
"""

# Sphere parameters
radius_feet = 20906306.39764
radius_millions_feet = radius_feet / 1e6  # Convert to millions of feet

# Generate points on the sphere
phi, theta = np.linspace(0, np.pi, 100), np.linspace(0, 2 * np.pi, 100)
phi, theta = np.meshgrid(phi, theta)
x = radius_millions_feet * np.sin(phi) * np.cos(theta)
y = radius_millions_feet * np.sin(phi) * np.sin(theta)
z = radius_millions_feet * np.cos(phi)

# Create the plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='brown', rstride=5, cstride=5, alpha=0.5)

# Set the axis labels and title
ax.set_xlabel('Distance (Millions of Feet)')
ax.set_ylabel('Distance (Millions of Feet)')
ax.set_zlabel('Distance (Millions of Feet)')
ax.set_title(r"Earth's Average Ground Level Radius at 31°46'40''N")

# Set tick positions and labels at every 10 millionth foot
tick_positions = np.arange(-30, 30 + 10, 10)  # From -30 to 30 (both inclusive), step 10
ax.set_xticks(tick_positions)
ax.set_yticks(tick_positions)
ax.set_zticks(tick_positions)

plt.show()
