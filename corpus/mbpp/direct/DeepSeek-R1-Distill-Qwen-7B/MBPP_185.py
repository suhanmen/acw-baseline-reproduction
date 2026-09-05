def parabola_focus(a, b, c):
    # The equation of the parabola is y = ax^2 + bx + c
    # The focus of a parabola in the form y = ax^2 + bx + c is given by:
    # Vertex x-coordinate: -b/(2a)
    # Vertex y-coordinate: c - b^2/(4a) + 1/(4a) (since the standard form is y = a(x - h)^2 + k)
    # The focus is (h, k + 1/(4a))
    h = -b / (2 * a)
    k = c - (b**2) / (4 * a) + 1 / (4 * a)
    return (h, k)