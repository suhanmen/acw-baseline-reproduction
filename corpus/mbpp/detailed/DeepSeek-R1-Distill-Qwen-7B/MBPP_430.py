def parabola_directrix(a, b, c):
    # Validate the input
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise ValueError("Invalid input: a, b, c must be numbers")
    if a == 0:
        raise ValueError("Coefficient 'a' must be non-zero for a valid parabola")

    # Calculate the directrix
    denominator = 4 * a
    if denominator == 0:
        raise ValueError("Division by zero error occurred")
    directrix_y = c - (b**2 - 1) / denominator

    return directrix_y