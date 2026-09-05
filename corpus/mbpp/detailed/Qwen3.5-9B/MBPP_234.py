import math
from typing import Union

def validate_dimension(value: Union[int, float]) -> float:
    """
    Validates that the given dimension is a number greater than zero.

    This function checks:
    1. Whether the value is a number (int or float).
    2. Whether the value is strictly positive (greater than 0).

    Parameters:
    value (Union[int, float]): The dimension of the cube to validate.

    Returns:
    float: The validated dimension if it passes all checks.

    Raises:
    TypeError: If the input is not an integer or float.
    ValueError: If the input is less than or equal to zero.
    """
    # Check if the type is correct (integer or float)
    if not isinstance(value, (int, float)):
        raise TypeError(f"Dimension must be a number, but got {type(value).__name__}")

    # Check for floating point 'NaN' (Not a Number) specifically, 
    # though isinstance usually catches it, explicit check is defensive.
    if isinstance(value, float) and math.isnan(value):
        raise ValueError("Dimension cannot be NaN")

    # Check for infinity specifically, though isinstance usually catches it, 
    # explicit check is defensive.
    if isinstance(value, float) and math.isinf(value):
        raise ValueError("Dimension cannot be infinite")

    # Check for non-positive values
    if value <= 0:
        raise ValueError(f"Dimension must be greater than zero, but got {value}")

    # Return the value as a float for consistency in subsequent calculations
    return float(value)


def calculate_cube_volume(side_length: float) -> float:
    """
    Calculates the volume of a cube given a validated side length.

    Logic:
    Volume = side_length * side_length * side_length

    Parameters:
    side_length (float): The length of one side of the cube (must be > 0).

    Returns:
    float: The calculated volume of the cube.
    """
    # Step 1: Calculate the area of the base (side * side)
    base_area = side_length * side_length

    # Step 2: Multiply the base area by the height (which is equal to side_length)
    volume = base_area * side_length

    return volume


def volume_cube(side: Union[int, float]) -> float:
    """
    Finds the volume of a cube with a given side length.

    This function implements defensive programming practices:
    1. It validates the input to ensure it is a positive number.
    2. It handles edge cases like zero, negative numbers, non-numbers,
       NaN, and Infinity by raising specific exceptions.
    3. It calculates the volume using explicit intermediate steps.

    Parameters:
    side (Union[int, float]): The length of the cube's side.

    Returns:
    float: The volume of the cube.

    Raises:
    TypeError: If 'side' is not a number.
    ValueError: If 'side' is less than or equal to zero, NaN, or infinite.
    """
    # Step 1: Validate the input dimension explicitly
    validated_side = validate_dimension(side)

    # Step 2: Calculate and return the volume using the helper function
    return calculate_cube_volume(validated_side)