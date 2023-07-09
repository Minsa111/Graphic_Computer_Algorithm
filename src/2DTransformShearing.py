import numpy as np
import matplotlib.pyplot as plt

def shear_x(matrix, shear_factor):
    shear_matrix = np.array([[1, shear_factor], [0, 1]])
    return np.dot(matrix, shear_matrix)

def shear_y(matrix, shear_factor):
    shear_matrix = np.array([[1, 0], [shear_factor, 1]])
    return np.dot(matrix, shear_matrix)

# Original rectangle coordinates
rectangle = np.array([[0, 0], [0, 4], [6, 4], [6, 0], [0, 0]])

# Apply shear against x-axis
shear_factor_x = 0.5
sheared_x = shear_x(rectangle, shear_factor_x)

# Apply shear towards y-axis
shear_factor_y = -0.5
sheared_y = shear_y(rectangle, shear_factor_y)

# Plotting the transformations
plt.figure(figsize=(10, 5))

# Shear against x-axis
plt.subplot(1, 2, 1)
plt.plot(rectangle[:, 0], rectangle[:, 1], 'b-', label='Before Shearing')
plt.plot(sheared_x[:, 0], sheared_x[:, 1], 'r-', label='After Shearing (X-axis)')
plt.title('Shear Against X-axis')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Shear towards y-axis
plt.subplot(1, 2, 2)
plt.plot(rectangle[:, 0], rectangle[:, 1], 'b-', label='Before Shearing')
plt.plot(sheared_y[:, 0], sheared_y[:, 1], 'g-', label='After Shearing (Y-axis)')
plt.title('Shear Towards Y-axis')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

plt.tight_layout()
plt.show()
