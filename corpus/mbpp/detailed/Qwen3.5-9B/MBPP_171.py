def validate_side_length(side: float) -> None:
    """
    Validates that the given side length is a valid numeric value and strictly positive.

    A pentagon must have positive side lengths. Zero or negative values are invalid
    for a physical geometric shape. Non-numeric types are also rejected.

    Raises:
        TypeError: If the input is not a number (int, float, etc.).
        ValueError: If the input is a number but is zero or negative.
    """
    # Check for type validity
    if not isinstance(side, (int, float)):
        raise TypeError(
            f"Invalid input type: expected a number (int or float), but got '{type(side).__name__}'."
        )

    # Check for numeric validity (must be positive)
    if side <= 0:
        raise ValueError(
            f"Invalid side length: {side}. A side length must be strictly greater than zero."
        )


def calculate_perimeter(side: float) -> float:
    """
    Calculates the perimeter of a regular pentagon given the length of one of its sides.

    A regular pentagon has 5 sides of equal length.
    Perimeter = 5 * side_length.

    Args:
        side: The length of one side of the pentagon.

    Returns:
        The calculated perimeter as a float.
    """
    constant_sides_count = 5
    perimeter = side * constant_sides_count
    return perimeter


def perimeter_pentagon(side: float) -> float:
    """
    Calculates the perimeter of a regular pentagon given the side length.

    This function serves as the main entry point. It validates the input to ensure
    geometric validity before performing the calculation.

    Args:
        side: The length of a single side of the pentagon. Must be a positive number.

    Returns:
        The total perimeter of the pentagon.

    Raises:
        TypeError: If 'side' is not a numeric type.
        ValueError: If 'side' is zero or negative.
    """
    # Step 1: Validate the input explicitly
    validate_side_length(side)

    # Step 2: Perform the calculation using the helper function
    result = calculate_perimeter(side)

    # Step 3: Return the result
    return result