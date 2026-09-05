import math

def volume_cylinder(r, h):
    # Check if inputs are valid numbers (int or float)
    if not isinstance(r, (int, float)) or not isinstance(h, (int, float)):
        raise ValueError("Inputs must be numbers")

    # Check if radius and height are non-negative
    if r < 0 or h < 0:
        raise ValueError("Radius and height must be non-negative")

    # Calculate the volume of the cylinder
    volume = math.pi * (r ** 2) * h

    return volume