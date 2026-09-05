import math

def volume_cylinder(radius: float, height: float) -> float:
    """
    Calculates the volume of a cylinder given its radius and height.

    The formula used is: Volume = pi * (radius^2) * height

    Args:
        radius (float): The radius of the cylinder's base.
        height (float): The height of the cylinder.

    Returns:
        float: The calculated volume.

    Raises:
        ValueError: If radius or height are negative.
        TypeError: If radius or height are not numeric types.
    """
    # Step 1: Validate that the inputs are of numeric types (int or float)
    is_radius_numeric = isinstance(radius, (int, float))
    is_height_numeric = isinstance(height, (int, float))

    if not is_radius_numeric or not is_height_numeric:
        raise TypeError("Both radius and height must be integers or floats.")

    # Step 2: Validate that the dimensions are non-negative.
    # While a zero dimension results in zero volume, a negative dimension is physically impossible.
    if radius < 0:
        raise ValueError("The radius cannot be a negative number.")

    if height < 0:
        raise ValueError("The height cannot be a negative number.")

    # Step 3: Handle the degenerate case where radius or height is zero.
    # If either is zero, the volume is mathematically zero.
    if radius == 0 or height == 0:
        return 0.0

    # Step 4: Calculate the area of the circular base.
    # Area = pi * r^2
    radius_squared = float(radius ** 2)
    base_area = math.pi * radius_squared

    # Step 5: Calculate the final volume.
    # Volume = Area of base * height
    volume = base_area * float(height)

    return volume

if __name__ == "__main__":
    # Provided assertions
    assert volume_cylinder(10, 5) == 1570.7500000000002
    assert volume_cylinder(4, 5) == 251.32000000000002
    assert volume_cylinder(4, 10) == 502.64000000000004