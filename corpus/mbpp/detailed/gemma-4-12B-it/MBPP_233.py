import math

def lateralsuface_cylinder(radius: float, height: float) -> float:
    """
    Calculates the lateral surface area of a cylinder.

    The lateral surface area of a cylinder is the area of the side wall,
    excluding the areas of the top and bottom circular bases.
    The formula is: Area = 2 * pi * radius * height.

    Args:
        radius (float): The radius of the base of the cylinder.
        height (float): The height of the cylinder.

    Returns:
        float: The lateral surface area.

    Raises:
        ValueError: If radius or height is negative.
        TypeError: If inputs are not numeric types.
    """
    # --- Input Validation ---

    # Check if the inputs are of correct types (int or float)
    # We accept both because Python's float operations handle ints automatically.
    if not isinstance(radius, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Both radius and height must be numeric (int or float).")

    # Check for non-positive or negative values.
    # A cylinder with a radius of 0 or a height of 0 has a lateral area of 0.
    # However, negative dimensions are physically impossible and should be caught.
    if radius < 0:
        raise ValueError("Radius cannot be a negative number.")

    if height < 0:
        raise ValueError("Height cannot be a negative number.")

    # --- Logic ---

    # Handle the degenerate cases explicitly.
    # If radius is 0, the cylinder is a line (no surface area).
    # If height is 0, the cylinder is a flat disk (no lateral surface area).
    if radius == 0 or height == 0:
        return 0.0

    # Define constants
    pi_constant = math.pi

    # Calculate the circumference of the base
    # Circumference = 2 * pi * radius
    circumference = 2.0 * pi_constant * float(radius)

    # Calculate the lateral surface area
    # Lateral Area = Circumference * Height
    lateral_area = circumference * float(height)

    return lateral_area

# The assertions provided in the problem description:
# Note: The precision in the assertions (e.g., 314.15000000000003) 
# results from the floating point representation of math.pi and multiplications.