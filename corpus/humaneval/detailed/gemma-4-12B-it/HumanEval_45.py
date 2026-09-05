from typing import Union

def _validate_numeric_input(value: Union[int, float], name: str) -> None:
    """
    Validates that an input is a number (int or float).

    Args:
        value: The value to check.
        name: The name of the variable for error reporting.

    Raises:
        TypeError: If the value is not an instance of int or float.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"Input '{name}' must be a numeric type (int or float), "
                        f"got {type(value).__name__} instead.")

def _validate_positive_dimensions(a: Union[int, float], h: Union[int, float]) -> None:
    """
    Validates that the dimensions are non-negative and non-zero.
    In geometry, a triangle with a side or height of 0 is degenerate.

    Args:
        a: The side length.
        h: The height.

    Raises:
        ValueError: If either dimension is less than or equal to zero.
    """
    if a <= 0:
        raise ValueError(f"Side length 'a' must be greater than zero. Received: {a}")
    if h <= 0:
        raise ValueError(f"Height 'h' must be greater than zero. Received: {h}")

def triangle_area(a: Union[int, float], h: Union[int, float]) -> float:
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    # Step 1: Validate types of inputs
    _validate_numeric_input(a, "a")
    _validate_numeric_input(h, "h")

    # Step 2: Validate geometric validity (non-degenerate)
    _validate_positive_dimensions(a, h)

    # Step 3: Calculate the area
    # The formula for the area of a triangle is (base * height) / 2
    # Here, 'a' represents the base side length.
    base_length = float(a)
    height_value = float(h)

    product_of_dimensions = base_length * height_value
    area = product_of_dimensions / 2.0

    # Step 4: Return the final calculated area
    return area