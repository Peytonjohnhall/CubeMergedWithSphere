import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

"""
Author: Peyton J. Hall (C)
A Python program to represent the geometric structure of the perfect cube
of New Jerusalem. That is, according to what is described in Revelation 21:16.
Revelation 21:16 KJV "And the city lieth foursquare, and the length is 
as large as the breadth: and he measured the city with the reed, twelve 
thousand furlongs. The length and the breadth and the height of it are equal."
"""

# Constants
side_length = 12000  # length of one side in furlongs

# Vertices of the cube
vertices = [
    (0, 0, 0), (0, side_length, 0), (side_length, side_length, 0), (side_length, 0, 0),
    (0, 0, side_length), (0, side_length, side_length), (side_length, side_length, side_length), (side_length, 0, side_length)
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
ax.set_xlim([0, side_length])
ax.set_ylim([0, side_length])
ax.set_zlim([0, side_length])

# Set labels
ax.set_xlabel("Length (Furlongs)")
ax.set_ylabel("Breadth (Furlongs)")
ax.set_zlabel("Height (Furlongs)")

# Set title
ax.set_title("Geometric Structure of New Jerusalem")

# Show the plot
plt.show()
