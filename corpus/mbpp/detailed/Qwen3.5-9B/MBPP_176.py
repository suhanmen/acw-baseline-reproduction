def _validate_positive_number(value, param_name):
    """
    Validates that a given numeric value is strictly positive.

    Returns:
        The value if valid.

    Raises:
        TypeError: If the value is not a number (int or float).
        ValueError: If the value is zero or negative.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"{param_name} must be a number (int or float), got {type(value).__name__}")

    if value <= 0:
        raise ValueError(f"{param_name} must be a positive number (> 0), got {value}")

    return value

def _validate_triangle_sides(a, b, c):
    """
    Validates that three given values can form a valid non-degenerate triangle.

    A valid triangle must satisfy:
    1. All sides are positive numbers.
    2. The sum of any two sides must be strictly greater than the third side
       (Triangle Inequality Theorem).

    Returns:
        The tuple (a, b, c) if valid.

    Raises:
        TypeError: If any side is not a number.
        ValueError: If any side is non-positive or if the triangle inequality fails.
    """
    # Step 1: Validate types
    _validate_positive_number(a, "Side a")
    _validate_positive_number(b, "Side b")
    _validate_positive_number(c, "Side c")

    # At this point, we know a, b, and c are positive numbers.

    # Step 2: Check Triangle Inequality Theorem
    # Condition 1: a + b > c
    if (a + b) <= c:
        raise ValueError(
            f"Sides do not form a valid triangle: "
            f"a + b ({a} + {b} = {a + b}) is not strictly greater than c ({c})."
        )

    # Condition 2: a + c > b
    if (a + c) <= b:
        raise ValueError(
            f"Sides do not form a valid triangle: "
            f"a + c ({a} + {c} = {a + c}) is not strictly greater than b ({b})."
        )

    # Condition 3: b + c > a
    if (b + c) <= a:
        raise ValueError(
            f"Sides do not form a valid triangle: "
            f"b + c ({b} + {c} = {b + c}) is not strictly greater than a ({a})."
        )

    return (a, b, c)

def perimeter_triangle(side_a, side_b, side_c):
    """
    Calculates the perimeter of a triangle given the lengths of its three sides.

    This function is defensive and production-grade. It validates the inputs
    explicitly to ensure mathematical correctness and handles edge cases such as:
    - Non-numeric inputs
    - Zero or negative lengths
    - Degenerate triangles (where the sum of two sides equals the third)

    The perimeter is the sum of the lengths of the three sides: P = a + b + c.

    Args:
        side_a (int or float): The length of the first side.
        side_b (int or float): The length of the second side.
        side_c (int or float): The length of the third side.

    Returns:
        int or float: The perimeter of the triangle.

    Raises:
        TypeError: If any argument is not a number.
        ValueError: If any argument is non-positive or if the inputs do not form
                    a valid triangle.

    Examples:
        >>> perimeter_triangle(10, 20, 30)
        60
        >>> perimeter_triangle(3, 4, 5)
        12
        >>> perimeter_triangle(25, 35, 45)
        105
    """

    # Validate inputs and ensure they form a valid triangle
    _validate_triangle_sides(side_a, side_b, side_c)

    # Calculate perimeter
    calculated_perimeter = side_a + side_b + side_c

    return calculated_perimeter