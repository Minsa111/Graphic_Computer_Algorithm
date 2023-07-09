import matplotlib.pyplot as plt

def plot_point(x, y, x_c, y_c):
    # Move the point to the elliptical path centered at (x_c, y_c)
    x += x_c
    y += y_c
    plt.plot(x, y, 'bo')

def midpoint_ellipse(r_x, r_y, x_c, y_c):
    # Step 1: Calculate initial parameter in region 1
    p1_0 = r_y**2 - r_x**2 * r_y + (r_x**2) / 4

    # Region 1
    x = 0
    y = r_y

    dx = 2 * r_y**2 * x
    dy = 2 * r_x**2 * y

    while dx < dy:
        # Plot the current point and its symmetry points
        plot_point(x, y, x_c, y_c)
        plot_point(-x, y, x_c, y_c)
        plot_point(-x, -y, x_c, y_c)
        plot_point(x, -y, x_c, y_c)

        if p1_0 < 0:
            x += 1
            dx += 2 * r_y**2
            p1_0 += dx + r_y**2
        else:
            x += 1
            y -= 1
            dx += 2 * r_y**2
            dy -= 2 * r_x**2
            p1_0 += dx - dy + r_y**2

    # Step 2: Calculate initial parameter in region 2
    p2_0 = r_y**2 * (x + 0.5)**2 + r_x**2 * (y - 1)**2 - r_x**2 * r_y**2

    # Region 2
    while y >= 0:
        # Plot the current point and its symmetry points
        plot_point(x, y, x_c, y_c)
        plot_point(-x, y, x_c, y_c)
        plot_point(-x, -y, x_c, y_c)
        plot_point(x, -y, x_c, y_c)

        if p2_0 > 0:
            y -= 1
            dy -= 2 * r_x**2
            p2_0 += r_x**2 - dy
        else:
            x += 1
            y -= 1
            dx += 2 * r_y**2
            dy -= 2 * r_x**2
            p2_0 += dx - dy + r_x**2

# Inserting the coords of center and the radius
r_x = 20  # Semi-major axis
r_y = 10  # Semi-minor axis
x_c = 0  # Center x-coordinate
y_c = 0  # Center y-coordinate

plt.figure(figsize=(6, 6))
plt.axis('equal')

midpoint_ellipse(r_x, r_y, x_c, y_c)
plt.grid(True)

plt.show()
