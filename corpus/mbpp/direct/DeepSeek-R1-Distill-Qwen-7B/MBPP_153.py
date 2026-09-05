def parabola_vertex(a, b, c):
    """
    Find the vertex of a parabola given by the equation y = ax^2 + bx + c.

    The vertex (h, k) of a parabola can be found using the formulas:
        h = -b/(2a)
        k = c - b^2/(4a)

    Args:
        a (float): The coefficient of x^2
        b (float): The coefficient of x
        c (float): The constant term

    Returns:
        tuple: A tuple containing the x and y coordinates of the vertex.
    """
    h = -b / (2 * a)
    k = c - (b ** 2) / (4 * a)
    return (h, k)

# Example usage:
# print(parabola_vertex(1, 2, 3))  # Output: (-1.0, 2.0)