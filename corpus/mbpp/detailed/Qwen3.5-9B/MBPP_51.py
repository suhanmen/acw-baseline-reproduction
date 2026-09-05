def check_equilateral(side_a, side_b, side_c):
    """
    Determines whether a triangle with the given three side lengths is equilateral.

    An equilateral triangle is defined as a triangle where all three sides are equal.
    Additionally, for any valid triangle to exist, the sum of any two sides must be
    strictly greater than the third side (Triangle Inequality Theorem).

    Parameters:
        side_a (int or float): The length of the first side.
        side_b (int or float): The length of the second side.
        side_c (int or float): The length of the third side.

    Returns:
        bool: True if the triangle is equilateral, False otherwise.

    Raises:
        TypeError: If any side is not a number (int or float).
        ValueError: If any side is not positive (must be > 0).
    """

    # Step 1: Validate types. Ensure all inputs are numeric.
    if not isinstance(side_a, (int, float)) or not isinstance(side_b, (int, float)) or not isinstance(side_c, (int, float)):
        raise TypeError("All side lengths must be numbers (int or float).")

    # Step 2: Validate positivity. Side lengths must be strictly positive.
    if side_a <= 0:
        raise ValueError("Side lengths must be strictly positive numbers.")
    if side_b <= 0:
        raise ValueError("Side lengths must be strictly positive numbers.")
    if side_c <= 0:
        raise ValueError("Side lengths must be strictly positive numbers.")

    # Step 3: Check the specific condition for an equilateral triangle.
    # All three sides must be exactly equal to each other.
    if side_a == side_b and side_b == side_c:
        # If all sides are equal, the triangle inequality is automatically satisfied
        # because x + x > x simplifies to 2x > x, which is true for x > 0.
        # Therefore, no explicit triangle inequality check is needed for the equilateral case.
        return True
    else:
        # If sides are not all equal, it cannot be equilateral.
        return False