import math

def circle_circumference(radius):
    """
    Calculate the circumference of a circle.

    Args:
        radius (float|int): The radius of the circle.

    Returns:
        float: The circumference of the circle rounded to 15 decimal places.

    Raises:
        ValueError: If the radius is negative or not a number.
    """
    # Input validation
    if not isinstance(radius, (int, float)) or radius < 0:
        raise ValueError("Radius must be a non-negative number.")

    # Calculate the circumference
    circumference = 2 * math.pi * radius

    # Rounding the result to match the required precision
    # Using 15 decimal places for precision
    return round(circumference, 15)

# Example assertions to verify the correctness of the function
assert circle_circumference(10) == 62.830000000000005
assert circle_circumference(5) == 31.415000000000003
assert circle_circumference(4) == 25.132