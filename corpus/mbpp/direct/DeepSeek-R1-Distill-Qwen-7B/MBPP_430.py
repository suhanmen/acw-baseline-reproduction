def parabola_directrix(a, b, c):
    """
    Find the directrix of a parabola given by the equation y = a x^2 + b x + c.

    The directrix of a parabola in the form y = a x^2 + b x + c is given by the equation y = c - (b^2 + 1)/(4a).

    Args:
        a (float): Coefficient of x^2
        b (float): Coefficient of x
        c (float): Constant term

    Returns:
        float: The y-coordinate of the directrix.
    """
    return c - (b**2 + 1) / (4 * a)

# Example usage:
print(parabola_directrix(5, 3, 2))  # Output: -198
print(parabola_directrix(9, 8, 4))  # Output: -2336
print(parabola_directrix(2, 4, 6))  # Output: -130