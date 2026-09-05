import math

def surfacearea_sphere(radius):
    """
    Calculate the surface area of a sphere given its radius.

    Args:
        radius (float): The radius of the sphere. Must be a positive number.

    Returns:
        float: The surface area of the sphere with high precision.

    Raises:
        ValueError: If the radius is zero or negative.
    """
    # Validate the input
    if radius < 0:
        raise ValueError("Radius must be a positive number.")

    # Calculate the surface area using the formula A = 4 * π * r^2
    surface_area = 4 * math.pi * (radius ** 2)

    # Return the result with high precision
    return surface_area

# Test the function with provided examples
assert surfacearea_sphere(10) == 1256.6370614359173
assert surfacearea_sphere(15) == 2827.4333882308138
assert surfacearea_sphere(20) == 5026.548245743669