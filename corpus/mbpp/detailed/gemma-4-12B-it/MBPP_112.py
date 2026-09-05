import math

def perimeter(radius: float, height: float) -> float:
    """
    Calculates the perimeter of a cylinder.

    In the context of common geometry problems involving a "perimeter" 
    of a 3D shape like a cylinder, it typically refers to the sum 
    of the circumferences of the two circular bases and the lengths 
    of the vertical lines (heights) if projected, but based on the 
    provided assertions, the logic follows a specific pattern.

    Assertion analysis:
    1. perimeter(2, 4) == 12  => (2 * 2) + (2 * 4) = 4 + 8 = 12
    2. perimeter(1, 2) == 6   => (2 * 1) + (2 * 2) = 2 + 4 = 6
    3. perimeter(3, 1) == 8   => (2 * 3) + (2 * 1) = 6 + 2 = 8

    Pattern: Perimeter = (2 * radius) + (2 * height)
    This is equivalent to the perimeter of a rectangle with sides 
    radius and height.

    Args:
        radius (float): The radius of the cylinder base.
        height (float): The height of the cylinder.

    Returns:
        float: The calculated perimeter.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inputs are negative.
    """

    # Validate input types
    if not isinstance(radius, (int, float)):
        raise TypeError(f"Radius must be a number, got {type(radius).__name__}")

    if not isinstance(height, (int, float)):
        raise TypeError(f"Height must be a number, got {type(height).__name__}")

    # Validate input values (physical dimensions cannot be negative)
    if radius < 0:
        raise ValueError(f"Radius cannot be negative. Received: {radius}")

    if height < 0:
        raise ValueError(f"Height cannot be negative. Received: {height}")

    # Calculation steps
    # Based on the assertions: Perimeter = 2 * radius + 2 * height

    diameter_component = 2 * radius
    height_component = 2 * height

    total_perimeter = diameter_component + height_component

    # Return as float to ensure consistency
    return float(total_perimeter)

if __name__ == "__main__":
    # These assertions verify the requirements provided in the prompt
    assert perimeter(2, 4) == 12
    assert perimeter(1, 2) == 6
    assert perimeter(3, 1) == 8