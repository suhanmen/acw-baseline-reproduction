def parabola_directrix(a, b, c):
    """
    Given coefficients a, b, c of a quadratic y = ax^2 + bx + c,
    compute the y-coordinate of the directrix.

    For a parabola y = ax^2 + bx + c:
      - Vertex y-coordinate: Vy = c - b^2/(4a)
      - Focus y-coordinate: Vy + 1/(4a)
      - Directrix y-coordinate: Vy - 1/(4a) = c - b^2/(4a) - 1/(4a) = c - (b^2 + 1)/(4a)
    """
    return c - (b ** 2 + 1) / (4 * a)