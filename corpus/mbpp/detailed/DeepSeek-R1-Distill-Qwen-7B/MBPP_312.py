def volume_cone(radius, height):
    """
    Calculate the volume of a cone.

    Parameters:
    radius (float): The radius of the cone's base.
    height (float): The height of the cone.

    Returns:
    float: The volume of the cone.

    Raises:
    ValueError: If radius or height are not positive numbers.
    """
    # Validate inputs
    if not (isinstance(radius, (int, float)) and isinstance(height, (int, float))):
        raise ValueError("Radius and height must be numbers.")
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive numbers.")

    # Calculate the volume using the formula V = (1/3) * π * r^2 * h
    pi = 3.141592653589793
    volume = (1.0/3.0) * pi * (radius ** 2) * height

    return volume