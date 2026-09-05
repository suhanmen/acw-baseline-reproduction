import math

def area_pentagon(s):
    """
    Calculate the area of a regular pentagon given its side length.

    Args:
        s (float|int): The length of a side of the pentagon. Must be a positive number.

    Returns:
        float: The area of the pentagon, rounded to 15 decimal places.

    Raises:
        ValueError: If the input is not a positive number.
    """
    # Validate the input
    if not isinstance(s, (int, float)) or s <= 0:
        raise ValueError("Side length must be a positive number.")

    # Calculate the area using the formula for a regular pentagon
    area = (5 * s ** 2) / (4 * math.tan(math.pi / 5))

    # Round the result to 15 decimal places for consistency with test cases
    return round(area, 15)