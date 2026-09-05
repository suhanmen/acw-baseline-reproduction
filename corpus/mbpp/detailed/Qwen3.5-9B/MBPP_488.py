import math
from typing import Union

Number = Union[int, float]

def _validate_side_length(side_length: Number) -> None:
    """
    Validates that the input side_length is a valid number (int or float)
    and is strictly positive.

    Raises:
        TypeError: If the input is not an int or float.
        ValueError: If the input is not greater than zero.
    """
    if not isinstance(side_length, (int, float)):
        raise TypeError(f"Side length must be a number (int or float), got {type(side_length).__name__}")

    if math.isnan(side_length):
        raise ValueError("Side length cannot be NaN.")

    if math.isinf(side_length):
        raise ValueError("Side length cannot be infinite.")

    if side_length <= 0:
        raise ValueError(f"Side length must be greater than zero, got {side_length}")

def _calculate_regular_pentagon_area(side_length: Number) -> float:
    """
    Calculates the area of a regular pentagon given its side length.

    The formula for the area of a regular pentagon is:
    Area = (5 * s^2) / (4 * tan(π / 5))
    where s is the side length.

    Args:
        side_length: The length of one side of the pentagon.

    Returns:
        The calculated area of the pentagon as a float.
    """
    # Define mathematical constants
    pi = math.pi
    five = 5
    four = 4

    # Calculate the square of the side length
    squared_side_length = side_length ** 2

    # Calculate the denominator term: 4 * tan(pi / 5)
    # We use math.tan for high precision trigonometric calculation
    angle = pi / 5
    tangent_of_angle = math.tan(angle)
    denominator = four * tangent_of_angle

    # Calculate the numerator term: 5 * s^2
    numerator = five * squared_side_length

    # Perform the final division to get the area
    calculated_area = numerator / denominator

    return calculated_area

def area_pentagon(side_length: Number) -> float:
    """
    Calculates and returns the area of a regular pentagon with a given side length.

    This function assumes the pentagon is regular (all sides equal, all angles equal).
    It performs strict validation on the input to ensure mathematical correctness
    and handles edge cases explicitly.

    Args:
        side_length: The length of the side of the pentagon. Must be a positive number.

    Returns:
        The area of the pentagon as a float.

    Raises:
        TypeError: If side_length is not an int or float.
        ValueError: If side_length is not greater than zero.
    """
    # Step 1: Explicitly validate the input parameter
    _validate_side_length(side_length)

    # Step 2: Calculate the area using the specialized helper function
    result = _calculate_regular_pentagon_area(side_length)

    # Step 3: Return the result
    # The result is guaranteed to be a float by the helper function
    return result