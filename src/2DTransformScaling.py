import matplotlib.pyplot as plt

def scale_points(points, scale_x, scale_y):
    new_points = []
    for x, y in points:
        new_x = x * scale_x
        new_y = y * scale_y
        new_points.append((new_x, new_y))
    return new_points

def plot_scaling(points, scale_x, scale_y):
    # Before scaling
    plt.subplot(121)
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.plot(x, y, 'ro')
    plt.title('Before Scaling')
    plt.xlim(min(x) - 1, max(x) + 1)
    plt.ylim(min(y) - 1, max(y) + 1)
    plt.grid(True)

    # After scaling
    scaled_points = scale_points(points, scale_x, scale_y)
    x_scaled = [p[0] for p in scaled_points]
    y_scaled = [p[1] for p in scaled_points]
    plt.subplot(122)
    plt.plot(x_scaled, y_scaled, 'bo')
    plt.title('After Scaling')
    plt.xlim(min(x_scaled) - 1, max(x_scaled) + 1)
    plt.ylim(min(y_scaled) - 1, max(y_scaled) + 1)
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Example usage
points = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
scale_x = 2
scale_y = 4

plot_scaling(points, scale_x, scale_y)
