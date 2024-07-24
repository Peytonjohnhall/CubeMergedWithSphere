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
side_length_miles = 1378.9772728  # length of one side in miles

# Vertices of the cube
vertices = [
    (0, 0, 0), (0, side_length_miles, 0), (side_length_miles, side_length_miles, 0), (side_length_miles, 0, 0),
    (0, 0, side_length_miles), (0, side_length_miles, side_length_miles), (side_length_miles, side_length_miles, side_length_miles), (side_length_miles, 0, side_length_miles)
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
ax = fig.add_subplot(111, projection='3d')

# Add each face to the plot
ax.add_collection3d(Poly3DCollection(faces, facecolors='gold', linewidths=1, edgecolors='black', alpha=.25))

# Set the limits of the plot
ax.set_xlim([0, side_length_miles])
ax.set_ylim([0, side_length_miles])
ax.set_zlim([0, side_length_miles])

# Set labels
ax.set_xlabel('Length (miles)')
ax.set_ylabel('Breadth (miles)')
ax.set_zlabel('Height (miles)')

# Set tick positions and labels
ax.set_xticks(range(0, int(side_length_miles) + 1, 200))
ax.set_yticks(range(0, int(side_length_miles) + 1, 200))
ax.set_zticks(range(0, int(side_length_miles) + 1, 200))

# Set title
ax.set_title('Geometric Structure of New Jerusalem')

# Show the plot
plt.show()
