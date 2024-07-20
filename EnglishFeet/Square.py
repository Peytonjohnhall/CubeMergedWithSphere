import numpy as np
import matplotlib.pyplot as plt

"""
Author: Peyton J. Hall (C).
A python program which graphs the 2D size of
New Jerusalem according to its dimensions 
described of in Revelation 21:16.
"""

# Square parameters
x_min = -3640500
x_max = 3640500
y_min = -3640500
y_max = 3640500

# Define the vertices of the square
vertices_x = [x_min, x_max, x_max, x_min, x_min]
vertices_y = [y_min, y_min, y_max, y_max, y_min]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')

# Plot the square
ax.plot(np.array(vertices_x)/1000000, np.array(vertices_y)/1000000, color='gold', linewidth=2)

# Set the axis labels and title
ax.set_xlabel('Distance (Millions of Feet)')
ax.set_ylabel('Distance (Millions of Feet)')
ax.set_title('2D Representation of New Jerusalem')

plt.show()
