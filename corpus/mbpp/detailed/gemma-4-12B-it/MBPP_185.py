from typing import Tuple

def parabola_focus(a: float, b: float, c: float) -> Tuple[float, float]:
    """
    Calculates the focus of a parabola defined by the quadratic equation 
    y = ax^2 + bx + c.

    The standard form of a vertical parabola is (x - h)^2 = 4p(y - k),
    where (h, k) is the vertex and p is the distance from the vertex to the focus.

    The vertex (h, k) for y = ax^2 + bx + c is:
    h = -b / (2a)
    k = f(h) = a(h^2) + b(h) + c

    The focal length 'p' is defined such that:
    p = 1 / (4a)

    The focus (x_f, y_f) is:
    x_f = h
    y_f = k + p

    Args:
        a: The coefficient of x^2.
        b: The coefficient of x.
        c: The constant term.

    Returns:
        A tuple (x_f, y_f) representing the coordinates of the focus.

    Raises:
        ValueError: If 'a' is zero, as a parabola requires a non-zero quadratic coefficient.
        TypeError: If any of the inputs are not numeric.
    """
    # Input Validation: Ensure all inputs are numbers
    if not all(isinstance(i, (int, float)) for i in [a, b, c]):
        raise TypeError("All coefficients (a, b, c) must be integers or floats.")

    # Edge Case: If a is 0, the equation is linear (y = bx + c), not a parabola.
    # A parabola must have a non-zero quadratic term.
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a parabola equation.")

    # Step 1: Calculate the x-coordinate of the vertex (h)
    # h = -b / (2a)
    denominator_h = 2 * a
    h = -b / denominator_h

    # Step 2: Calculate the y-coordinate of the vertex (k)
    # k = a(h^2) + b(h) + c
    h_squared = h ** 2
    term_1 = a * h_squared
    term_2 = b * h
    k = term_1 + term_2 + c

    # Step 3: Calculate the focal distance (p)
    # For y = ax^2 + bx + c, the standard form is (x - h)^2 = 4p(y - k)
    # Expanding (x - h)^2 = 4p(y - k) gives y = (1/4p)(x - h)^2 + k
    # Thus, a = 1 / (4p), which means p = 1 / (4a)
    focal_distance = 1 / (4 * a)

    # Step 4: Calculate the focus coordinates
    # The focus is located at (h, k + p) for a vertical parabola
    focus_x = h
    focus_y = k + focal_distance

    return (focus_x, focus_y)