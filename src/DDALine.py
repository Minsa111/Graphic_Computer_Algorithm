import matplotlib.pyplot as plt
import math

def dda_algorithm(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    # Determine the "step"
    step = max(abs(dx), abs(dy))

    # Calculate increments
    x_increment = dx / step
    y_increment = dy / step

    # Initialize coordinates
    x = x0
    y = y0

    # Create lists to store the pixel positions
    x_pixels = [round(x)]
    y_pixels = [round(y)]

    # Calculate the tolerance value
    cap = 1e-6

    # Iterate until (x, y) reaches the end point
    while abs(x - x1) > cap or abs(y - y1) > cap:
        x += x_increment
        y += y_increment

        # Round the coordinates to determine the pixel position
        x_pixel = round(x)
        y_pixel = round(y)

        # Store the pixel positions
        x_pixels.append(x_pixel)
        y_pixels.append(y_pixel)

    # Plot the line
    plt.plot(x_pixels, y_pixels, marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('DDA Algorithm')
    plt.grid(True)
    plt.show()

# Example usage
dda_algorithm(1, 1, 8, 5)
