import math
from typing import Union

def _validate_input(number: float) -> float:
    """
    Validates that the input is a finite positive floating point number.

    Args:
        number (float): The number to validate.

    Returns:
        float: The validated input number.

    Raises:
        ValueError: If the input is not a finite positive number.
    """
    if not isinstance(number, float):
        raise TypeError(f"Expected float, got {type(number).__name__}")

    if math.isnan(number):
        raise ValueError("Input cannot be NaN (Not a Number).")

    if math.isinf(number):
        raise ValueError("Input cannot be infinite.")

    if number < 0:
        raise ValueError("Input must be a positive number (>= 0).")

    return number

def _extract_integer_part(number: float) -> int:
    """
    Extracts the integer part of a positive floating point number.
    The integer part is defined as the largest integer smaller than or equal to the number.
    For positive numbers, this corresponds to floor(number).

    Args:
        number (float): A validated positive floating point number.

    Returns:
        int: The integer part of the number.
    """
    # math.floor returns an integer representing the largest integer <= number
    return math.floor(number)

def _calculate_decimal_part(number: float, integer_part: int) -> float:
    """
    Calculates the decimal part of a positive floating point number.
    Decimal part = original number - integer part.

    Args:
        number (float): The original validated positive number.
        integer_part (int): The integer part calculated previously.

    Returns:
        float: The decimal part (always >= 0 and < 1).
    """
    decimal_part = number - integer_part
    return decimal_part

def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.

    Raises:
        TypeError: If the input is not a float.
        ValueError: If the input is negative, NaN, or infinite.

    Examples:
        >>> truncate_number(3.5)
        0.5
        >>> truncate_number(0.0)
        0.0
        >>> truncate_number(10.0)
        0.0
        >>> truncate_number(0.123456)
        0.123456
    """
    # Step 1: Validate the input explicitly
    validated_number = _validate_input(number)

    # Step 2: Extract the integer part using a dedicated helper
    # This ensures we use the mathematical definition of integer part (floor)
    integer_part = _extract_integer_part(validated_number)

    # Step 3: Calculate the decimal part by subtracting the integer part from the original
    # Using the original validated number ensures precision before subtraction
    decimal_part = _calculate_decimal_part(validated_number, integer_part)

    return decimal_part