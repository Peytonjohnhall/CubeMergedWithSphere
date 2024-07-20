import numpy as np
import matplotlib.pyplot as plt

"""
Author: Peyton J. Hall (C).
A python program which graphs the 2D size of
New Jerusalem according to its dimensions 
described of in Revelation 21:16.
"""

# Square parameters
x_min = -689.4886364
x_max = 689.4886364
y_min = -689.4886364
y_max = 689.4886364

# Define the vertices of the square
vertices_x = [x_min, x_max, x_max, x_min, x_min]
vertices_y = [y_min, y_min, y_max, y_max, y_min]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')

# Plot the square
ax.plot(vertices_x, vertices_y, color='gold', linewidth=2)

# Set the axis labels and title
ax.set_xlabel('Distance (Miles)')
ax.set_ylabel('Distance (Miles)')
ax.set_title('2D Representation of New Jerusalem')

plt.show()
