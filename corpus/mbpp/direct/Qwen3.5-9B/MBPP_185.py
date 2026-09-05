def parabola_focus(a, b, c):
    """
    Given a quadratic equation ax^2 + bx + c = 0, find the focus of the corresponding parabola.
    """
    import math

    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a parabola.")

    # Vertex x-coordinate
    h = -b / (2 * a)

    # Vertex y-coordinate
    k = a * h**2 + b * h + c

    # Focus is at (h, k + 1/(4a))
    p = 1 / (4 * a)
    y_focus = k + p

    return (h, y_focus)