import matplotlib.pyplot as plt

def liang_barsky(x_min, y_min, x_max, y_max, x1, y1, x2, y2):
    p = [-1, -1, -1, -1]
    q = [-1, -1, -1, -1]
    r = [-1, -1, -1, -1]
    u1 = 0.0
    u2 = 1.0

    dx = x2 - x1
    dy = y2 - y1

    p[0] = -dx
    p[1] = dx
    p[2] = -dy
    p[3] = dy

    q[0] = x1 - x_min
    q[1] = x_max - x1
    q[2] = y1 - y_min
    q[3] = y_max - y1

    for i in range(4):
        if p[i] == 0 and q[i] < 0:
            return None

        r[i] = q[i] / p[i]

        if p[i] < 0:
            u1 = max(u1, r[i])
        else:
            u2 = min(u2, r[i])

    if u1 > u2:
        return None

    x1_new = x1 + u1 * dx
    y1_new = y1 + u1 * dy
    x2_new = x1 + u2 * dx
    y2_new = y1 + u2 * dy

    return x1_new, y1_new, x2_new, y2_new


# Example usage
x_min = 0
y_min = 0
x_max = 5
y_max = 10

x1 = 2
y1 = 3
x2 = 8
y2 = 7

clipped_line = liang_barsky(x_min, y_min, x_max, y_max, x1, y1, x2, y2)

# Plotting the original line
plt.plot([x1, x2], [y1, y2], 'b', label='Original Line')

if clipped_line:
    x1_new, y1_new, x2_new, y2_new = clipped_line
    # Plotting the clipped line
    plt.plot([x1_new, x2_new], [y1_new, y2_new], 'r', label='Clipped Line')

plt.xlim(x_min-5, x_max+5)
plt.ylim(y_min-5, y_max+5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Liang-Barsky Line Clipping')
plt.legend()
plt.grid(True)
plt.show()
