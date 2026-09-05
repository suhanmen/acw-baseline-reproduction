def diameter_circle(radius):
    """
    Calculate the diameter of a circle given its radius.

    Args:
        radius (int/float): The radius of the circle.

    Returns:
        float|int: The diameter of the circle.

    Raises:
        ValueError: If the radius is not a valid number or is negative.

    Example:
        >>> diameter_circle(10)
        20
        >>> diameter_circle(40)
        80
        >>> diameter_circle(15)
        30
    """
    # Check if the input is a number
    if not isinstance(radius, (int, float)):
        raise ValueError("Invalid input: radius must be a number.")

    # Check if the radius is non-negative
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    # Calculate the diameter
    diameter = radius * 2

    # Return the diameter
    return diameter

# Test the function with the given assertions
assert diameter_circle(10) == 20, "Failed assertion: diameter_circle(10) should be 20"
assert diameter_circle(40) == 80, "Failed assertion: diameter_circle(40) should be 80"
assert diameter_circle(15) == 30, "Failed assertion: diameter_circle(15) should be 30"

# Optional: Handle cases where radius is zero or a positive number
# The function already handles these as part of its input validation and calculation