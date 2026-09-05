def _validate_coefficients(a, b, c):
    """
    Validate that the input coefficients are numbers (int or float).
    Raise a TypeError if any coefficient is invalid.

    :param a: Coefficient of x^2
    :param b: Coefficient of x
    :param c: Constant term
    :raises TypeError: If any parameter is not a number.
    :raises ValueError: If 'a' is zero (not a parabola).
    """
    # Check for correct types
    if not isinstance(a, (int, float)):
        raise TypeError(f"Expected 'a' to be a number, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Expected 'b' to be a number, got {type(b).__name__}")
    if not isinstance(c, (int, float)):
        raise TypeError(f"Expected 'c' to be a number, got {type(c).__name__}")

    # Check for degenerate case: 'a' cannot be zero for a parabola
    if a == 0:
        raise ValueError("Coefficient 'a' must not be zero to define a parabola.")

    return a, b, c

def _calculate_vertex_x(a, b):
    """
    Calculate the x-coordinate of the vertex (focus) using the formula: -b / (2a)

    :param a: Coefficient of x^2
    :param b: Coefficient of x
    :return: The x-coordinate of the vertex.
    """
    return -b / (2.0 * a)

def _calculate_focus_y(a, b, c):
    """
    Calculate the y-coordinate of the vertex (focus) using the formula: 
    (4ac - b^2) / (4a)

    :param a: Coefficient of x^2
    :param b: Coefficient of x
    :param c: Constant term
    :return: The y-coordinate of the vertex.
    """
    discriminant_term = 4.0 * a * c - (b ** 2.0)
    denominator = 4.0 * a
    return discriminant_term / denominator

def parabola_focus(a, b, c):
    """
    Calculate the coordinates (x, y) of the focus (vertex) of a parabola defined by 
    the quadratic equation y = ax^2 + bx + c.

    The function validates inputs, handles edge cases, and uses explicit steps 
    to ensure clarity and robustness.

    :param a: Coefficient of x^2
    :param b: Coefficient of x
    :param c: Constant term
    :return: A tuple (x, y) representing the focus of the parabola.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If 'a' is zero.
    """
    # Step 1: Validate all input coefficients
    valid_a, valid_b, valid_c = _validate_coefficients(a, b, c)

    # Step 2: Calculate the x-coordinate of the focus (vertex)
    # Formula: x_vertex = -b / (2a)
    x_focus = _calculate_vertex_x(valid_a, valid_b)

    # Step 3: Calculate the y-coordinate of the focus (vertex)
    # Formula: y_vertex = (4ac - b^2) / (4a)
    y_focus = _calculate_focus_y(valid_a, valid_b, valid_c)

    # Step 4: Return the result as a tuple
    return (x_focus, y_focus)