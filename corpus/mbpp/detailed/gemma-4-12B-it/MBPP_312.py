import math

def volume_cone(radius: float, height: float) -> float:
    """
    Calculates the volume of a cone given its radius and height.

    The formula for the volume of a cone is:
    V = (1/3) * pi * r^2 * h

    Args:
        radius (float): The radius of the circular base of the cone.
        height (float): The vertical height of the cone.

    Returns:
        float: The calculated volume of the cone.

    Raises:
        ValueError: If radius or height are negative.
        TypeError: If radius or height are not numeric types.
    """
    # Validate that the inputs are of numeric types (int or float)
    is_radius_numeric = isinstance(radius, (int, float))
    is_height_numeric = isinstance(height, (int, float))

    if not is_radius_numeric or not is_height_numeric:
        raise TypeError("Both radius and height must be numeric values (int or float).")

    # Validate that dimensions are non-negative
    # A cone with zero radius or height has zero volume, which is mathematically valid.
    if radius < 0:
        raise ValueError(f"Radius cannot be negative. Provided: {radius}")

    if height < 0:
        raise ValueError(f"Height cannot be negative. Provided: {height}")

    # Handle degenerate cases explicitly
    # If radius is 0, the cone is just a line segment (volume 0)
    # If height is 0, the cone is just a flat circle (volume 0)
    if radius == 0 or height == 0:
        return 0.0

    # Calculate the area of the circular base: Area = pi * r^2
    radius_squared = float(radius ** 2)
    base_area = math.pi * radius_squared

    # Calculate the volume: Volume = (1/3) * base_area * height
    # We perform the multiplication first and then divide by 3 to maintain precision
    total_product = base_area * float(height)
    volume = total_product / 3.0

    return volume

# Verification with provided assertions
if __name__ == "__main__":
    # These assertions verify the accuracy of the formula implementation
    assert math.isclose(volume_cone(5, 12), 314.15926535897927, rel_tol=1e-9)
    assert math.isclose(volume_cone(10, 15), 1570.7963267948965, rel_tol=1e-9)
    assert math.isclose(volume_cone(19, 17), 6426.651371693521, rel_tol=1e-9)