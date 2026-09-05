def parabola_vertex(a, b, c):
    """
    Finds the vertex of a parabola given by the equation y = ax^2 + bx + c.
    The x-coordinate of the vertex is given by -b / (2a).
    The y-coordinate is found by substituting x into the equation.
    """
    x = -b / (2 * a)
    y = a * (x**2) + b * x + c
    return (x, y)