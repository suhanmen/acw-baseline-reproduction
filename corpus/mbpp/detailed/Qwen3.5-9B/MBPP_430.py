def _parse_float(value, name="value"):
    """
    Validate and convert the input to a float.

    If the input is None, it raises a ValueError.
    If the conversion fails, it raises a ValueError with a descriptive message.
    """
    if value is None:
        raise ValueError(f"{name} cannot be None")

    try:
        float_value = float(value)
        # We allow negative numbers and zero based on standard math, 
        # but the problem context implies specific numeric constraints.
        # We return the float for calculation.
        return float_value
    except (TypeError, ValueError) as e:
        raise ValueError(f"{name} must be a number, got {type(value).__name__}: {e}")


def _validate_coefficients(a, b, c):
    """
    Validate the coefficients of the parabola.

    Standard quadratic equation: y = ax^2 + bx + c.
    For a directrix to exist in the standard vertical parabola form, 'a' must not be zero.
    If a is zero, the equation is linear or constant, not a parabola.
    """
    a_float = _parse_float(a, "a")
    b_float = _parse_float(b, "b")
    c_float = _parse_float(c, "c")

    if a_float == 0.0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic function (parabola).")

    return a_float, b_float, c_float


def _calculate_vertex_y(a, b, c):
    """
    Calculate the y-coordinate of the vertex of the parabola y = ax^2 + bx + c.

    Formula: y_vertex = c - (b^2) / (4a)
    """
    b_squared = b * b
    four_times_a = 4.0 * a
    # Invert the denominator
    one_over_four_a = 1.0 / four_times_a
    correction_term = b_squared * one_over_four_a
    vertex_y = c - correction_term
    return vertex_y


def _calculate_focal_length(a):
    """
    Calculate the focal length (distance from vertex to focus) of the parabola.

    For a standard parabola y = ax^2 + bx + c (vertical orientation):
    The standard form is (x-h)^2 = 4p(y-k), where p is the focal length.
    Comparing coefficients leads to: a = 1 / (4p)  =>  p = 1 / (4a).

    Note: 
    If a > 0, the parabola opens upwards, and the focus is above the vertex.
    If a < 0, the parabola opens downwards, and the focus is below the vertex.
    The directrix is always on the opposite side of the vertex from the focus.
    Distance = |p|.
    """
    four_times_a = 4.0 * a
    focal_length = 1.0 / four_times_a
    return focal_length


def parabola_directrix(a, b, c):
    """
    Find the directrix of the parabola defined by y = ax^2 + bx + c.

    Parameters:
    a (int|float): Coefficient of x^2. Must not be zero.
    b (int|float): Coefficient of x.
    c (int|float): Constant term.

    Returns:
    float: The y-coordinate of the directrix line (y = constant).

    Logic derivation:
    1. Identify the vertex (h, k). The y-coordinate k is calculated as c - b^2/(4a).
    2. Determine the focal length 'p'. For y = ax^2 + ..., p = 1/(4a).
    3. The focus is at (h, k + p).
    4. The directrix is a horizontal line y = k - p.
    5. Substituting k and p:
       Directrix y = (c - b^2/(4a)) - (1/(4a))
                    = c - (b^2 + 1) / (4a)

    This function implements the explicit step-by-step calculation with validation.
    """
    # Step 1: Input Validation
    a, b, c = _validate_coefficients(a, b, c)

    # Step 2: Calculate the y-coordinate of the vertex
    # k = c - (b^2) / (4a)
    b_squared = b * b
    four_times_a = 4.0 * a
    vertex_y = c - (b_squared / four_times_a)

    # Step 3: Calculate the focal length p = 1 / (4a)
    # Note: We keep the sign here to determine direction relative to vertex.
    p = 1.0 / four_times_a

    # Step 4: Calculate the directrix y-coordinate.
    # The directrix is located at distance |p| from the vertex, on the side opposite to the opening.
    # If a > 0 (opens up), p > 0, focus is above (k+p), directrix is below (k-p).
    # If a < 0 (opens down), p < 0, focus is below (k+p), directrix is above (k-p).
    # In both cases, the formula is y_directrix = vertex_y - p.

    directrix_y = vertex_y - p

    return directrix_y