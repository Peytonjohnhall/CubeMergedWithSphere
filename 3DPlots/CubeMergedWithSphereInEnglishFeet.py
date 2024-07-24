import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d

"""
Author: Peyton J. Hall (C).
A python program which 3 dimensionally graphs New Jerusalem 
on Mount Zion, at 31°46'40"N Latitude, in proportion with 
the radius of the earth at that given line of latitude. 
The graph emphasizes the fact that it would not be feasible
to enter through the gates of New Jerusalem without staircases
connecting the perimeter of the cube's base with the earth.
"""

# Constants for the cube
side_length_furlongs = 12000  # length of one side in furlongs
furlong_to_feet = 606.75
side_length_feet = side_length_furlongs * furlong_to_feet  # length of one side in feet
side_length_millions_feet = side_length_feet / 1e6  # length of one side in millions of feet

# Center the cube on top of the sphere
cube_offset = side_length_millions_feet / 2

# Vertices of the cube
vertices = [
    (-cube_offset, -cube_offset, 0), (-cube_offset, cube_offset, 0), (cube_offset, cube_offset, 0), (cube_offset, -cube_offset, 0),
    (-cube_offset, -cube_offset, side_length_millions_feet), (-cube_offset, cube_offset, side_length_millions_feet), (cube_offset, cube_offset, side_length_millions_feet), (cube_offset, -cube_offset, side_length_millions_feet)
]

# Define the six faces of the cube
faces = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],
    [vertices[4], vertices[5], vertices[6], vertices[7]],
    [vertices[0], vertices[1], vertices[5], vertices[4]],
    [vertices[2], vertices[3], vertices[7], vertices[6]],
    [vertices[1], vertices[2], vertices[6], vertices[5]],
    [vertices[4], vertices[7], vertices[3], vertices[0]]
]

# Constants for the sphere
radius_feet = 20906306.39764
radius_millions_feet = radius_feet / 1e6  # Convert to millions of feet

# Generate points on the sphere
phi, theta = np.linspace(0, np.pi, 100), np.linspace(0, 2 * np.pi, 100)
phi, theta = np.meshgrid(phi, theta)
x_sphere = radius_millions_feet * np.sin(phi) * np.cos(theta)
y_sphere = radius_millions_feet * np.sin(phi) * np.sin(theta)
z_sphere = radius_millions_feet * np.cos(phi) - radius_millions_feet

# Create the plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")

# Plot the sphere
ax.plot_surface(x_sphere, y_sphere, z_sphere, color='brown', rstride=5, cstride=5, alpha=0.5)

# Add each face of the cube to the plot
ax.add_collection3d(art3d.Poly3DCollection(faces, facecolors="gold", linewidths=1, edgecolors="black", alpha=.25))

# Set the limits of the plot
ax.set_xlim([-25, 25])
ax.set_ylim([-25, 25])
ax.set_zlim([-45, 15])

# Set labels
ax.set_xlabel("Distance (Millions of Feet)")
ax.set_ylabel("Distance (Millions of Feet)")
ax.set_zlabel("Distance (Millions of Feet)")

# Set tick positions and labels
tick_positions_x = np.arange(-25, 26, 5)  # From -25 to 25 in steps of 5 million feet
tick_positions_y = np.arange(-25, 26, 5)  # From -25 to 25 in steps of 5 million feet
tick_positions_z = np.arange(-45, 16, 5)  # From -45 to 15 in steps of 5 million feet
ax.set_xticks(tick_positions_x)
ax.set_yticks(tick_positions_y)
ax.set_zticks(tick_positions_z)

# Set title
ax.set_title("3D Representation of New Jerusalem on Mount Zion")

# Show the plot
plt.show()
