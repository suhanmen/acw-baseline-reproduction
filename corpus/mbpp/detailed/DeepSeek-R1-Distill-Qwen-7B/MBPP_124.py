import math

def angle_complex(x, y):
    # Validate inputs
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both x and y must be numbers.")

    # Handle special cases
    if x == 0 and y == 0:
        raise ValueError("The complex number 0 has no defined angle.")
    elif x == 0:
        if y > 0:
            return math.pi / 2
        else:
            return -math.pi / 2

    # Calculate the angle using atan2 which handles the signs correctly
    angle = math.atan2(y, x)

    return angle