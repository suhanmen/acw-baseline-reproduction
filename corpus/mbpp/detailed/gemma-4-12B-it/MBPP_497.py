import math

def surfacearea_cone(radius: float, height: float) -> float:
    """
    Calculates the surface area of a right circular cone.

    The formula for the surface area of a cone is:
    Area = Base_Area + Lateral_Area
    Area = (pi * r^2) + (pi * r * s)
    where:
        r is the radius of the base.
        h is the height of the cone.
        s is the slant height, calculated as sqrt(r^2 + h^2).

    Args:
        radius (float): The radius of the base of the cone.
        height (float): The perpendicular height of the cone.

    Returns:
        float: The total surface area of the cone.

    Raises:
        ValueError: If radius or height are negative.
        TypeError: If inputs are not numeric.
    """
    # --- Input Validation ---

    # Check if inputs are integers or floats
    if not isinstance(radius, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Both radius and height must be numeric values (int or float).")

    # Check for negative dimensions
    # A cone cannot have negative physical dimensions.
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    if height < 0:
        raise ValueError("Height cannot be negative.")

    # --- Handle Degenerate Cases ---

    # If radius is 0, the surface area is 0 (it's just a line segment).
    if radius == 0:
        return 0.0

    # If height is 0, it is a flat disk with a slant height equal to the radius.
    # The formula still works, but we can treat it explicitly if needed.
    # Surface Area = pi*r^2 + pi*r*r = 2 * pi * r^2

    # --- Calculation Steps ---

    # 1. Calculate the area of the circular base.
    # Area_base = pi * r^2
    base_area = math.pi * (radius ** 2)

    # 2. Calculate the slant height (s).
    # Using Pythagorean theorem: s^2 = r^2 + h^2
    radius_squared = radius ** 2
    height_squared = height ** 2
    sum_of_squares = radius_squared + height_squared
    slant_height = math.sqrt(sum_of_squares)

    # 3. Calculate the lateral surface area.
    # Area_lateral = pi * r * s
    lateral_area = math.pi * radius * slant_height

    # 4. Calculate total surface area.
    total_surface_area = base_area + lateral_area

    return total_surface_area

if __name__ == "__main__":
    # Test cases provided in the requirements
    assert math.isclose(surfacearea_cone(5, 12), 282.7433388230814, rel_tol=1e-9)
    assert math.isclose(surfacearea_cone(10, 15), 880.5179353159282, rel_tol=1e-9)
    assert math.isclose(surfacearea_cone(19, 17), 2655.923961165254, rel_tol=1e-9)