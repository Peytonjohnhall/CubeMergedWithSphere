import numpy as np
import matplotlib.pyplot as plt

"""
Author: Peyton J. Hall (C).
A python program which 2 dimensionally graphs New Jerusalem 
on Mount Zion, at 31°46'40"N Latitude, in proportion with 
the radius of the earth at that given line of latitude. 
The graph emphasizes the fact that staircases, angled at 45°,
would provide accessibility in and out of New Jerusalem's gates.
"""

def plot_square(ax, color='gold'):
    """
    Plots a square representing the 2D size of New Jerusalem.
    
    Parameters:
    ax (matplotlib.axes.Axes): The axes to plot on.
    color (str): The color of the square's outline.
    """
    # Square parameters in miles
    x_min = -689.4886364
    x_max = 689.4886364
    y_min = 0
    y_max = 1378.9772728

    # Define the vertices of the square
    vertices_x = [x_min, x_max, x_max, x_min, x_min]
    vertices_y = [y_min, y_min, y_max, y_max, y_min]

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
    # Circle parameters in miles
    center_x = 0
    center_y = -3959.527726825758
    radius = 3959.527726825758

    # Generate points on the circle
    theta = np.linspace(0, 2*np.pi, 100)
    x_circle = center_x + radius * np.cos(theta)
    y_circle = center_y + radius * np.sin(theta)

    # Plot the circle
    ax.plot(x_circle, y_circle, color=color, linewidth=2)

def plot_staircases(ax, color='tan'):
    """
    Plots the staircases angled at 45°.
    
    Parameters:
    ax (matplotlib.axes.Axes): The axes to plot on.
    color (str): The color of the staircases.
    """
    # Staircase equations and domains
    x1 = np.linspace(-763.87, -689.4886364, 100)
    y1 = x1 + 689.4886364

    x2 = np.linspace(689.4886364, 763.87, 100)
    y2 = -(x2 - 689.4886364)

    # Plot the staircases
    ax.plot(x1, y1, color=color, linewidth=2)
    ax.plot(x2, y2, color=color, linewidth=2)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')

# Plot the circle, square, and staircases
plot_circle(ax, color='brown')
plot_square(ax, color='gold')
plot_staircases(ax, color='tan')

# Set the axis limits for both x and y to be centered around 0
ax.set_xlim(-4500, 4500)
ax.set_ylim(-9000, 2000)

# Set the axis labels and title
ax.set_xlabel('Distance (Miles)')
ax.set_ylabel('Distance (Miles)')
ax.set_title(r"2D Representation of New Jerusalem on Mount Zion" + "\n" + 
             "With Staircases Angled 45° Connecting the Earth to the Gates")

# Display the plot
plt.show()
