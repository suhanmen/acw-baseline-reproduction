def parabola_vertex(a, b, c):
    # Validate the inputs
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return None

    # Check if it's a valid parabola
    if a == 0:
        return None

    # Calculate the x-coordinate
    x = -b / (2 * a)

    # Calculate the y-coordinate
    y = c - (b ** 2) / (4 * a)

    # Return the vertex as a tuple
    return (x, y)