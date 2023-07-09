import matplotlib.pyplot as plt

def translate_point(point, tx, ty):
    # Perform translation on the given point
    x = point[0] + tx
    y = point[1] + ty
    return x, y

# Define the original coordinates
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

# Translation amounts
tx = 2
ty = 3

# Perform translation on each coordinate point
translated_x = [translate_point((x[i], y[i]), tx, ty)[0] for i in range(len(x))]
translated_y = [translate_point((x[i], y[i]), tx, ty)[1] for i in range(len(y))]

# Plot the original coordinates
plt.scatter(x, y, color='blue', label='Original')

# Plot the translated coordinates
plt.scatter(translated_x, translated_y, color='red', label='Translated')

# Draw arrows to indicate the translation
for i in range(len(x)):
    plt.arrow(x[i], y[i], tx, ty, color='gray', linestyle='dashed', head_width=0.2)

# Set the axis limits
plt.xlim(min(x) - 1, max(translated_x) + 1)
plt.ylim(min(y) - 1, max(translated_y) + 1)

# Add labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Display the plot
plt.show()
