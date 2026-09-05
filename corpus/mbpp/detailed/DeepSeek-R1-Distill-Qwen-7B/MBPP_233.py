import math

def lateralsuface_cylinder(r, h):
    """
    Calculate the lateral surface area of a cylinder.

    Args:
        r (float): The radius of the cylinder.
        h (float): The height of the cylinder.

    Returns:
        float: The lateral surface area of the cylinder.

    Raises:
        ValueError: If either r or h is not a number.
    """
    try:
        # Calculate the lateral surface area
        lateral_area = 2 * math.pi * r * h
        # Format the result to 12 decimal places
        return round(lateral_area, 12)
    except (TypeError, ValueError):
        raise ValueError("Invalid input. r and h must be numbers.")