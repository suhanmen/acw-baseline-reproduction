import math

def _validate_inputs(number_of_sides: int, side_length: float) -> None:
    """
    Validates the inputs for the area of a regular polygon calculation.

    Raises:
        TypeError: If the types of the arguments are incorrect.
        ValueError: If the values are out of the expected bounds.
    """
    # Validate number_of_sides
    if not isinstance(number_of_sides, int):
        raise TypeError(f"number_of_sides must be an integer, got {type(number_of_sides).__name__}")

    if number_of_sides <= 0:
        raise ValueError(f"number_of_sides must be a positive integer, got {number_of_sides}")

    # Validate side_length
    if not isinstance(side_length, (int, float)):
        raise TypeError(f"side_length must be a number (int or float), got {type(side_length).__name__}")

    if side_length <= 0:
        raise ValueError(f"side_length must be a positive number, got {side_length}")


def _calculate_apothem(side_length: float, number_of_sides: int) -> float:
    """
    Calculates the apothem of a regular polygon.

    The apothem is the distance from the center to the midpoint of a side.
    Formula: a = (side_length) / (2 * tan(pi / n))
    """
    # Calculate the internal angle divisor
    pi_divisor = math.pi / number_of_sides

    # Calculate the tangent of that angle
    tangent_value = math.tan(pi_divisor)

    # Calculate the apothem
    apothem_value = side_length / (2.0 * tangent_value)

    return apothem_value


def area_polygon(number_of_sides: int, side_length: float) -> float:
    """
    Calculates the area of a regular polygon given the number of sides and the side length.

    The formula used is: Area = (1/4) * n * s^2 * cot(pi/n)
    This is mathematically equivalent to: Area = (1/2) * perimeter * apothem

    Args:
        number_of_sides (int): The number of sides of the regular polygon (must be >= 3).
        side_length (float): The length of one side of the polygon (must be > 0).

    Returns:
        float: The calculated area of the polygon.

    Raises:
        TypeError: If inputs are not of the expected type.
        ValueError: If inputs are out of valid range.
    """
    # Step 1: Validate inputs to ensure they are reasonable before calculation
    _validate_inputs(number_of_sides, side_length)

    # A regular polygon must have at least 3 sides to form a closed shape.
    # While our validation allows n >= 1, geometrically n < 3 is impossible for a standard polygon area.
    # The problem implies standard polygons, so we enforce n >= 3 here for geometric validity.
    if number_of_sides < 3:
        raise ValueError(f"A polygon must have at least 3 sides. Got {number_of_sides}.")

    # Step 2: Calculate the perimeter of the polygon
    perimeter = number_of_sides * side_length

    # Step 3: Calculate the apothem
    apothem = _calculate_apothem(side_length, number_of_sides)

    # Step 4: Calculate the area using the formula: Area = (1/2) * Perimeter * Apothem
    # Using 0.5 explicitly for clarity instead of a float literal division
    area_result = 0.5 * perimeter * apothem

    return area_result