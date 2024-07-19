import numpy as np
import matplotlib.pyplot as plt

"""
Author: Peyton J. Hall (C).
A python program which 2 dimensionally graphs New Jerusalem 
on Mount Zion, at 31°46'40"N Latitude, in proportion with 
the radius of the earth at that given line of latitude. 
The graph emphasizes the fact that it would not be feasible
to enter through the gates of New Jerusalem without staircases
connecting the perimeter of the cube's base with the earth.
"""

def plot_square(ax, color='gold'):
    """
    Plots a square representing the 2D size of New Jerusalem.
    
    Parameters:
    ax (matplotlib.axes.Axes): The axes to plot on.
    color (str): The color of the square's outline.
    """
    # Square parameters
    x_min = -3640500
    x_max = 3640500
    y_min = 0
    y_max = 7281000

    # Define the vertices of the square
    vertices_x = [x_min, x_max, x_max, x_min, x_min]
    vertices_y = [y_min, y_min, y_max, y_max, y_min]

    # Scale the vertices to millions of feet
    vertices_x = [x / 1e6 for x in vertices_x]
    vertices_y = [y / 1e6 for y in vertices_y]

    # Plot the square
    ax.plot(vertices_x, vertices_y, color=color, linewidth=2)

def plot_circle(ax, color='brown'):
    """
    Plots a circle representing the Earth's average 
    ground level radius at 31°46'40"N Latitude.
    
    Parameters:
    ax (matplotlib.axes.Axes): The axes to plot on.
    color (str): The color of the circle's outline.
    """
    # Circle parameters
    center_x = 0
    center_y = -20906306.39764 
    radius = 20906306.39764

    # Generate points on the circle
    theta = np.linspace(0, 2*np.pi, 100)
    x_circle = center_x + radius * np.cos(theta)
    y_circle = center_y + radius * np.sin(theta)

    # Scale the circle points to millions of feet
    x_circle = [x / 1e6 for x in x_circle]
    y_circle = [y / 1e6 for y in y_circle]

    # Plot the circle
    ax.plot(x_circle, y_circle, color=color, linewidth=2)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')

# Plot the circle and the square
plot_circle(ax, color='brown')
plot_square(ax, color='gold')

# Set the axis limits for both x and y to be centered around 0
ax.set_xlim(-22, 22)
ax.set_ylim(-45, 10)

# Set the axis labels and title
ax.set_xlabel('Distance (Millions of Feet)')
ax.set_ylabel('Distance (Millions of Feet)')
ax.set_title(r"2D Representation of New Jerusalem on Mount Zion")

# Display the plot
plt.show()
