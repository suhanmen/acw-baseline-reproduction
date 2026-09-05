from typing import Union

Number = Union[int, float]

def _validate_length(value: Number, name: str) -> None:
    """
    Validates that a numeric value is a non-negative number suitable for
    representing a geometric length.

    Args:
        value: The numeric value to validate.
        name: The name of the parameter for error messages.

    Raises:
        TypeError: If the value is not a number (int or float).
        ValueError: If the value is negative or NaN/Infinity.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number, got {type(value).__name__}")

    if isinstance(value, float) and (value != value or value == float('inf') or value == float('-inf')):
        raise ValueError(f"{name} must be a valid finite number, got {value}")

    if value < 0:
        raise ValueError(f"{name} must be non-negative, got {value}")

def _validate_positive_length(value: Number, name: str, allow_zero: bool = False) -> None:
    """
    Validates that a numeric value is non-negative (or positive if allow_zero is False).

    Args:
        value: The numeric value to validate.
        name: The name of the parameter for error messages.
        allow_zero: If False, strictly requires value > 0.

    Raises:
        TypeError: If the value is not a number.
        ValueError: If the value violates the positivity constraint.
    """
    _validate_length(value, name)

    if not allow_zero and value <= 0:
        raise ValueError(f"{name} must be strictly positive (> 0), got {value}")

def _compute_area(side_length: Number, height: Number) -> float:
    """
    Computes the area of a triangle given the length of one side and the height
    corresponding to that base.

    Formula: Area = (base * height) / 2

    Args:
        side_length: The length of the base.
        height: The perpendicular height corresponding to the base.

    Returns:
        The calculated area as a float.
    """
    product = side_length * height
    area = product / 2.0
    return area

def triangle_area(a: Number, h: Number) -> float:
    """
    Given length of a side and high return area for a triangle.

    This function calculates the area of a triangle using the formula:
    Area = (base * height) / 2

    Args:
        a: The length of the base side of the triangle.
        h: The height of the triangle corresponding to base 'a'.

    Returns:
        The area of the triangle as a float.

    Raises:
        TypeError: If 'a' or 'h' are not numeric types.
        ValueError: If 'a' or 'h' are negative, or if either is zero 
                    (as a valid triangle requires a positive base and height).

    Examples:
        >>> triangle_area(5, 3)
        7.5
        >>> triangle_area(10, 4)
        20.0
        >>> triangle_area(3, 4)
        6.0
    """
    # Explicitly validate input types and constraints
    # Step 1: Validate base 'a'
    _validate_positive_length(a, "a", allow_zero=False)

    # Step 2: Validate height 'h'
    _validate_positive_length(h, "h", allow_zero=False)

    # Step 3: Compute the area using the helper function
    result = _compute_area(a, h)

    # Step 4: Return the result
    return result