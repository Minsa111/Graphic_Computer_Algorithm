import matplotlib.pyplot as plt

# Define region codes for the regions
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Function to compute region code for a point
def computeRegionCode(x, y, xmin, xmax, ymin, ymax):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT

    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP

    return code

# Function to clip a line using Cohen-Sutherland algorithm
def cohenSutherlandClip(x1, y1, x2, y2, xmin, xmax, ymin, ymax):
    code1 = computeRegionCode(x1, y1, xmin, xmax, ymin, ymax)
    code2 = computeRegionCode(x2, y2, xmin, xmax, ymin, ymax)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            # Both endpoints are inside the window
            accept = True
            break
        elif (code1 & code2) != 0:
            # Both endpoints are outside the same region
            break
        else:
            # Perform line clipping
            x = 0
            y = 0
            code_out = 0

            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeRegionCode(x1, y1, xmin, xmax, ymin, ymax)
            else:
                x2 = x
                y2 = y
                code2 = computeRegionCode(x2, y2, xmin, xmax, ymin, ymax)

    if accept:
        # Draw the clipped line
        print("Accepted line: ({}, {}) to ({}, {})".format(x1, y1, x2, y2))
        plt.plot([x1, x2], [y1, y2], 'r')
    else:
        # Reject the line
        print("Rejected line")

# Test the algorithm with sample values
cohenSutherlandClip(20, 10, 60, 50, 0, 50, 0, 40)

# Set the axis limits
plt.xlim(0, 70)
plt.ylim(0, 60)

# Display the plot
plt.show()
