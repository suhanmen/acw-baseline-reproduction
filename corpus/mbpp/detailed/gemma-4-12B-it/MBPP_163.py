import math

def area_polygon(num_sides: int, side_length: float) -> float:
    """
    Calculates the area of a regular polygon given the number of sides 
    and the length of each side.

    Args:
        num_sides (int): The number of sides of the regular polygon.
        side_length (float): The length of each side.

    Returns:
        float: The area of the regular polygon.

    Raises:
        ValueError: If num_sides is less than 3 or if side_length is non-positive.
        TypeError: If input types are incorrect.
    """

    # --- Input Validation ---

    # Validate type of num_sides
    if not isinstance(num_sides, int):
        raise TypeError(f"num_sides must be an integer, got {type(num_sides).__name__}")

    # Validate type of side_length
    if not isinstance(side_length, (int, float)):
        raise TypeError(f"side_length must be a number, got {type(side_length).__name__}")

    # Validate geometric constraints for a polygon
    # A polygon must have at least 3 sides.
    if num_sides < 3:
        raise ValueError(f"A polygon must have at least 3 sides. Received: {num_sides}")

    # Side length must be strictly positive to have an area.
    if side_length <= 0:
        raise ValueError(f"Side length must be greater than zero. Received: {side_length}")

    # --- Calculation Logic ---

    # The formula for the area of a regular polygon is:
    # Area = (n * s^2) / (4 * tan(pi / n))
    # Where:
    # n = number of sides
    # s = length of a side

    # Step 1: Calculate the square of the side length
    side_squared = float(side_length) ** 2

    # Step 2: Calculate the numerator (n * s^2)
    numerator = float(num_sides) * side_squared

    # Step 3: Calculate the denominator
    # We use math.pi for high precision and math.tan for the trigonometric calculation.
    # The interior angle calculation involves pi / n.
    angle_denominator = float(num_sides)
    angle_in_radians = math.pi / angle_denominator

    tangent_value = math.tan(angle_in_radians)

    # Safety check for division by zero (though impossible for n >= 3)
    if tangent_value == 0:
        raise ValueError("Calculation error: tangent of the internal angle resulted in zero.")

    denominator = 4.0 * tangent_value

    # Step 4: Final division
    area = numerator / denominator

    return area

# Internal assertions to ensure correctness based on problem requirements
if __name__ == "__main__":
    # Verification of provided test cases
    assert math.isclose(area_polygon(4, 20), 400.00000000000006, rel_tol=1e-12)
    assert math.isclose(area_polygon(10, 15), 1731.1969896610804, rel_tol=1e-12)
    assert math.isclose(area_polygon(9, 7), 302.90938549487214, rel_tol=1e-12)