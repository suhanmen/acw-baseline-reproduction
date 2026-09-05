import math
import typing

def _validate_positive_number(value: float, name: str) -> float:
    """
    Validates that a given value is a positive number.

    Args:
        value: The value to validate.
        name: A descriptive name for the value (used in error messages).

    Returns:
        The validated value if it is positive.

    Raises:
        ValueError: If the value is not positive (zero or negative).
        TypeError: If the value is not a number.
    """
    if isinstance(value, (int, float)):
        if value <= 0:
            raise ValueError(f"Side length '{name}' must be a positive number, got {value}.")
        return float(value)
    else:
        raise TypeError(f"Side length '{name}' must be a number (int or float), got {type(value).__name__}.")

def _validate_triangle_inequality(a: float, b: float, c: float, label_a: str, label_b: str, label_c: str) -> None:
    """
    Validates that the three sides satisfy the triangle inequality theorem.

    For a valid triangle, the sum of any two sides must be strictly greater than the third side.

    Args:
        a, b, c: The lengths of the three sides.
        label_a, label_b, label_c: Descriptive labels for error messages.

    Raises:
        ValueError: If the triangle inequality is violated.
    """
    # Check if a + b > c
    if not (a + b > c):
        raise ValueError(
            f"Invalid triangle: The sum of {label_a} ({a}) and {label_b} ({b}) "
            f"is not greater than {label_c} ({c}). {a + b} is not greater than {c}."
        )

    # Check if a + c > b
    if not (a + c > b):
        raise ValueError(
            f"Invalid triangle: The sum of {label_a} ({a}) and {label_c} ({c}) "
            f"is not greater than {label_b} ({b}). {a + c} is not greater than {b}."
        )

    # Check if b + c > a
    if not (b + c > a):
        raise ValueError(
            f"Invalid triangle: The sum of {label_b} ({b}) and {label_c} ({c}) "
            f"is not greater than {label_a} ({a}). {b + c} is not greater than {a}."
        )

def _check_isosceles_condition(a: float, b: float, c: float) -> bool:
    """
    Checks if a triangle is isosceles based on side lengths.

    A triangle is isosceles if at least two of its sides are equal in length.

    Args:
        a, b, c: The lengths of the three sides.

    Returns:
        True if the triangle is isosceles, False otherwise.
    """
    is_pair_ab_equal = (a == b)
    is_pair_ac_equal = (a == c)
    is_pair_bc_equal = (b == c)

    has_equal_pair = is_pair_ab_equal or is_pair_ac_equal or is_pair_bc_equal

    return has_equal_pair

def print_check_isosceles(a: float, b: float, c: float) -> None:
    """
    Prints whether the triangle with sides a, b, and c is isosceles or not.

    This function performs the following steps:
    1. Validates that all inputs are numbers.
    2. Validates that all inputs are positive.
    3. Validates that the sides can form a valid triangle (triangle inequality).
    4. Checks if the triangle is isosceles (at least two sides are equal).
    5. Prints the result to stdout.

    Args:
        a: Length of the first side.
        b: Length of the second side.
        c: Length of the third side.

    Raises:
        ValueError: If inputs are non-positive or do not form a valid triangle.
        TypeError: If inputs are not numbers.
    """
    # Step 1 & 2: Validate inputs and convert to float
    try:
        side_a = _validate_positive_number(a, "side a")
        side_b = _validate_positive_number(b, "side b")
        side_c = _validate_positive_number(c, "side c")
    except (ValueError, TypeError) as error:
        print(f"Error: {error}")
        return

    # Step 3: Validate triangle inequality
    _validate_triangle_inequality(
        side_a, side_b, side_c,
        "side a", "side b", "side c"
    )

    # Step 4: Check isosceles condition
    is_isosceles = _check_isosceles_condition(side_a, side_b, side_c)

    # Step 5: Print the result explicitly
    if is_isosceles:
        print("The triangle is isosceles.")
    else:
        print("The triangle is not isosceles.")