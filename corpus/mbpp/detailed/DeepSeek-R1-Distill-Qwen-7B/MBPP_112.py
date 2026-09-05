def perimeter(radius, height):
    """Calculate the perimeter of a cylinder."""
    if not isinstance(radius, int) or not isinstance(height, int):
        raise TypeError("Both radius and height must be integers.")
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive numbers.")
    perimeter_value = 2 * (radius + height)
    return perimeter_value