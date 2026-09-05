def check_equilateral(sides):
    """
    Determine if the given sides form an equilateral triangle.

    An equilateral triangle has all three sides of equal length.

    Args:
        sides (list): A list containing three numbers.

    Returns:
        str: "Equilateral triangle" if all sides are equal, 
             "Not an equilateral triangle" otherwise.
             "Invalid input" for invalid inputs.
    """
    # Check if there are exactly three sides provided
    if len(sides) != 3:
        return "Invalid input"

    # Check if any side is non-positive
    for side in sides:
        if side <= 0:
            return "Invalid input"

    # Check if all sides are equal
    a, b, c = sides
    if a == b == c:
        return "Equilateral triangle"
    else:
        return "Not an equilateral triangle"