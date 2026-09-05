import math
from typing import Union

def _validate_radius_value(value: float) -> None:
    """
    Validates that the provided value is a non-negative number.

    This helper function raises a specific ValueError if the input is invalid.
    It checks for:
    1. Non-numeric types (unless they can be safely cast to float, though we expect float/int).
    2. Negative values, as a radius cannot be negative.
    3. NaN (Not a Number).
    4. Infinity (positive or negative), as a physical radius cannot be infinite.

    Parameters:
    value (float): The radius value to validate.

    Raises:
    TypeError: If value is not a number (int or float).
    ValueError: If value is negative, NaN, or infinity.
    """
    # Check type validity. We accept int and float for user convenience.
    if not isinstance(value, (int, float)):
        raise TypeError(f"Input must be a number (int or float), got {type(value).__name__}")

    # Convert to float to handle integer inputs uniformly and check numeric properties
    numeric_value = float(value)

    # Check for NaN
    if math.isnan(numeric_value):
        raise ValueError(f"Input cannot be NaN.")

    # Check for Infinity
    if math.isinf(numeric_value):
        raise ValueError(f"Input cannot be infinite.")

    # Check for negative values
    if numeric_value < 0:
        raise ValueError(f"Radius cannot be negative. Received: {numeric_value}")


def _calculate_diameter(radius: float) -> float:
    """
    Calculates the diameter of a circle given its radius.

    The formula for the diameter is: diameter = 2 * radius.

    Parameters:
    radius (float): The radius of the circle. Must be non-negative.

    Returns:
    float: The calculated diameter.
    """
    diameter = 2.0 * radius
    return diameter


def diameter_circle(radius: Union[int, float]) -> float:
    """
    Finds the diameter of a circle given its radius.

    This function acts as the primary interface for calculating the diameter.
    It performs strict validation on the input to ensure it represents a valid
    physical radius before performing the calculation.

    Parameters:
    radius (int | float): The radius of the circle.

    Returns:
    float: The diameter of the circle.

    Raises:
    TypeError: If radius is not an integer or float.
    ValueError: If radius is negative, NaN, or infinite.
    """
    # Step 1: Validate the input strictly.
    # This handles edge cases like negative numbers, infinity, and non-numbers.
    _validate_radius_value(radius)

    # Step 2: Calculate the diameter using the helper function.
    # We isolate the arithmetic to keep the main function logic clear.
    result = _calculate_diameter(radius)

    return result