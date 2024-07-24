import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.ticker import FuncFormatter

"""
Author: Peyton J. Hall (C)
A Python program to represent the geometric structure of the perfect cube
of New Jerusalem. That is, according to what is described in Revelation 21:16.
Revelation 21:16 KJV "And the city lieth foursquare, and the length is 
as large as the breadth: and he measured the city with the reed, twelve 
thousand furlongs. The length and the breadth and the height of it are equal."
"""

# Constants
furlong_to_feet = 606.75
side_length_furlongs = 12000  # length of one side in furlongs
side_length_feet = side_length_furlongs * furlong_to_feet  # length of one side in feet
side_length_millions_feet = side_length_feet / 1e6  # length of one side in millions of feet

# Vertices of the cube
vertices = [
    (0, 0, 0), (0, side_length_millions_feet, 0), (side_length_millions_feet, side_length_millions_feet, 0), (side_length_millions_feet, 0, 0),
    (0, 0, side_length_millions_feet), (0, side_length_millions_feet, side_length_millions_feet), (side_length_millions_feet, side_length_millions_feet, side_length_millions_feet), (side_length_millions_feet, 0, side_length_millions_feet)
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

# Plotting the cube
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Add each face to the plot
ax.add_collection3d(Poly3DCollection(faces, facecolors="gold", linewidths=1, edgecolors="black", alpha=.25))

# Set the limits of the plot
ax.set_xlim([0, side_length_millions_feet])
ax.set_ylim([0, side_length_millions_feet])
ax.set_zlim([0, side_length_millions_feet])

# Set labels
ax.set_xlabel("Length (Millions of Feet)")
ax.set_ylabel("Breadth (Millions of Feet)")
ax.set_zlabel("Height (Millions of Feet)")

# Set tick positions and labels
ax.set_xticks(range(0, int(side_length_millions_feet) + 1))
ax.set_yticks(range(0, int(side_length_millions_feet) + 1))
ax.set_zticks(range(0, int(side_length_millions_feet) + 1))

# Set title
ax.set_title("Geometric Structure of New Jerusalem")

# Show the plot
plt.show()
