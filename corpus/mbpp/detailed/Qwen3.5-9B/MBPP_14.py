from typing import Tuple, Union

Number = Union[int, float]


def _validate_dimensions(a: Number, b: Number, c: Number) -> None:
    """
    Validates that the input dimensions are positive numbers.

    Raises:
        TypeError: If any argument is not a number (int or float).
        ValueError: If any argument is not a positive number (<= 0).
    """
    # Check for numeric types
    if not isinstance(a, (int, float)):
        raise TypeError(f"Expected a number for dimension 'a', got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Expected a number for dimension 'b', got {type(b).__name__}")
    if not isinstance(c, (int, float)):
        raise TypeError(f"Expected a number for dimension 'c', got {type(c).__name__}")

    # Check for positive values
    if a <= 0:
        raise ValueError(f"Dimension 'a' must be positive, got {a}")
    if b <= 0:
        raise ValueError(f"Dimension 'b' must be positive, got {b}")
    if c <= 0:
        raise ValueError(f"Dimension 'c' must be positive, got {c}")


def _calculate_base_area(a: Number, b: Number) -> Number:
    """
    Calculates the area of the triangular base.
    Formula: (base * height) / 2

    In this context, we treat 'a' as the base and 'b' as the height of the triangle.
    This aligns with the provided test cases where side lengths are multiplied by another.
    Note: For a general triangle with side lengths x, y, z, Heron's formula would be needed.
    However, the problem signature provides three numbers and the test cases (10,8,6)->240 
    strongly imply that these represent: Base (a), Height (b), and Length of Prism (c).
    Volume = (Area of Triangle) * Length = ((a * b) / 2) * c.

    Args:
        a: The base length of the triangle.
        b: The height of the triangle corresponding to base 'a'.

    Returns:
        The area of the triangular base.
    """
    base_length = a
    triangle_height = b

    # Calculate area: (base * height) / 2
    product_of_base_and_height = base_length * triangle_height
    base_area = product_of_base_and_height / 2.0

    return base_area


def _calculate_volume(base_area: Number, prism_length: Number) -> Number:
    """
    Calculates the volume of the prism.
    Formula: Base Area * Length

    Args:
        base_area: The area of the triangular base.
        prism_length: The length of the prism (the third dimension).

    Returns:
        The total volume of the triangular prism.
    """
    volume = base_area * prism_length
    return volume


def find_Volume(a: Number, b: Number, c: Number) -> Number:
    """
    Calculates the volume of a triangular prism given three dimensions.

    The function assumes the inputs represent:
    - 'a': The base length of the triangular face.
    - 'b': The height of the triangular face.
    - 'c': The length (or depth) of the prism.

    The volume is calculated as: Volume = (a * b * c) / 2.

    Args:
        a: A positive number representing the base of the triangle.
        b: A positive number representing the height of the triangle.
        c: A positive number representing the length of the prism.

    Returns:
        The calculated volume as a number (int or float).

    Raises:
        TypeError: If any input is not a number.
        ValueError: If any input is zero or negative.
    """
    # Step 1: Validate all inputs explicitly
    _validate_dimensions(a, b, c)

    # Step 2: Calculate the area of the triangular base
    # We use a helper function to ensure clarity and separate logic
    base_area = _calculate_base_area(a, b)

    # Step 3: Calculate the total volume by multiplying base area by the prism length
    final_volume = _calculate_volume(base_area, c)

    return final_volume