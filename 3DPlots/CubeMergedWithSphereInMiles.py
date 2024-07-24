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
side_length_miles = 1378.9772728  # length of one side in miles

# Center the cube on top of the sphere
cube_offset = side_length_miles / 2

# Vertices of the cube
vertices = [
    (-cube_offset, -cube_offset, 0), (-cube_offset, cube_offset, 0), (cube_offset, cube_offset, 0), (cube_offset, -cube_offset, 0),
    (-cube_offset, -cube_offset, side_length_miles), (-cube_offset, cube_offset, side_length_miles), (cube_offset, cube_offset, side_length_miles), (cube_offset, -cube_offset, side_length_miles)
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
radius_miles = 3959.527726825758  # radius in miles

# Generate points on the sphere
phi, theta = np.linspace(0, np.pi, 100), np.linspace(0, 2 * np.pi, 100)
phi, theta = np.meshgrid(phi, theta)
x_sphere = radius_miles * np.sin(phi) * np.cos(theta)
y_sphere = radius_miles * np.sin(phi) * np.sin(theta)
z_sphere = radius_miles * np.cos(phi) - radius_miles

# Create the plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")

# Plot the sphere
ax.plot_surface(x_sphere, y_sphere, z_sphere, color='brown', rstride=5, cstride=5, alpha=0.5)

# Add each face of the cube to the plot
ax.add_collection3d(art3d.Poly3DCollection(faces, facecolors="gold", linewidths=1, edgecolors="black", alpha=.25))

# Set the limits of the plot
ax.set_xlim([-4500, 4500])
ax.set_ylim([-4500, 4500])
ax.set_zlim([-9000, 2000])

# Set labels
ax.set_xlabel("Distance (Miles)")
ax.set_ylabel("Distance (Miles)")
ax.set_zlabel("Distance (Miles)")

# Set tick positions and labels, removing specific ticks
tick_positions_x = [x for x in np.arange(-4500, 4501, 500) if x not in [-4500, -3500, -2500, -1500, -500, 500, 1500, 2500, 3500, 4500]]
tick_positions_y = [y for y in np.arange(-4500, 4501, 500) if y not in [-4500, -3500, -2500, -1500, -500, 500, 1500, 2500, 3500, 4500]]
tick_positions_z = np.arange(-9000, 2001, 1000)  # From -9000 to 2000 in steps of 1000 miles
ax.set_xticks(tick_positions_x)
ax.set_yticks(tick_positions_y)
ax.set_zticks(tick_positions_z)

# Set title
ax.set_title("3D Representation of New Jerusalem on Mount Zion")

# Show the plot
plt.show()
