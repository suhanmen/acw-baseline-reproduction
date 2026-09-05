from typing import Tuple, Union

Number = Union[int, float]


def _validate_coefficients(
    a: Number, b: Number, c: Number
) -> None:
    """
    Validates that the provided coefficients are valid numbers and that 'a' is not zero.

    A parabola is defined by a quadratic equation where the coefficient of x^2 (a)
    must be non-zero. If a is zero, the function becomes linear, not parabolic.

    Raises:
        TypeError: If any input is not a number (int or float).
        ValueError: If 'a' is zero.
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"Coefficient 'a' must be a number, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Coefficient 'b' must be a number, got {type(b).__name__}")
    if not isinstance(c, (int, float)):
        raise TypeError(f"Coefficient 'c' must be a number, got {type(c).__name__}")

    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a parabola.")


def _calculate_vertex_x(a: Number, b: Number) -> Number:
    """
    Calculates the x-coordinate of the vertex.

    Formula: x = -b / (2 * a)
    """
    denominator = 2 * a
    x_vertex = -b / denominator
    return x_vertex


def _calculate_vertex_y(a: Number, b: Number, c: Number, x_vertex: Number) -> Number:
    """
    Calculates the y-coordinate of the vertex by substituting x_vertex into the quadratic equation.

    Formula: y = a * x^2 + b * x + c
    """
    x_squared = x_vertex * x_vertex
    term_a = a * x_squared
    term_b = b * x_vertex
    y_vertex = term_a + term_b + c
    return y_vertex


def parabola_vertex(a: Number, b: Number, c: Number) -> Tuple[Number, Number]:
    """
    Finds the vertex (x, y) of a parabola defined by y = ax^2 + bx + c.

    The vertex of a parabola represents the maximum or minimum point of the curve.
    The x-coordinate is found using the formula -b/(2a), and the y-coordinate is found
    by evaluating the equation at that x-value.

    Args:
        a: Coefficient of the x^2 term. Must not be zero.
        b: Coefficient of the x term.
        c: Constant term.

    Returns:
        A tuple containing the x and y coordinates of the vertex (x_vertex, y_vertex).

    Raises:
        TypeError: If any of a, b, or c are not numeric types.
        ValueError: If a is zero (which would make the function linear).

    Examples:
        >>> parabola_vertex(5, 3, 2)
        (-0.3, 1.55)
        >>> parabola_vertex(9, 8, 4)
        (-0.4444444444444444, 2.2222222222222223)
        >>> parabola_vertex(2, 4, 6)
        (-1.0, 4.0)
    """
    # Step 1: Validate inputs explicitly before any calculation
    _validate_coefficients(a, b, c)

    # Step 2: Calculate the x-coordinate of the vertex
    x_vertex = _calculate_vertex_x(a, b)

    # Step 3: Calculate the y-coordinate of the vertex using the calculated x
    y_vertex = _calculate_vertex_y(a, b, c, x_vertex)

    # Step 4: Return the result as a tuple
    return (x_vertex, y_vertex)