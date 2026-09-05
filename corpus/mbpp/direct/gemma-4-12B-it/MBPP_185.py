def parabola_focus(a, b, c):
    """
    Finds the focus of a parabola given by the equation y = ax^2 + bx + c.

    The formula for the focus (x, y) of a parabola y = ax^2 + bx + c:
    The vertex (h, k) is:
    h = -b / (2a)
    k = f(h) = a(h^2) + b(h) + c

    The distance from vertex to focus is p = 1 / (4a).
    The focus is located at (h, k + p).
    """
    h = -b / (2 * a)
    k = a * (h**2) + b * h + c
    p = 1 / (4 * a)

    focus_x = h
    focus_y = k + p

    return (focus_x, focus_y)