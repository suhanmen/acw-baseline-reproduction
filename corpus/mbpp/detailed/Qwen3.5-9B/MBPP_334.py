def check_validity(side_a: float, side_b: float, side_c: float) -> bool:
    """
    Determines whether three given side lengths can form a valid non-degenerate triangle.

    A triangle is valid if and only if:
    1. All sides are strictly greater than zero.
    2. The sum of any two sides is strictly greater than the third side (Triangle Inequality Theorem).

    Parameters:
        side_a (float): Length of the first side.
        side_b (float): Length of the second side.
        side_c (float): Length of the third side.

    Returns:
        bool: True if the sides form a valid triangle, False otherwise.

    Raises:
        TypeError: If any of the inputs are not numeric (int or float).
    """
    # Step 1: Validate that the inputs are of a numeric type.
    # We explicitly check for int and float. Other types (strings, None, etc.) are invalid.
    is_side_a_numeric = _is_numeric_value(side_a)
    is_side_b_numeric = _is_numeric_value(side_b)
    is_side_c_numeric = _is_numeric_value(side_c)

    if not (is_side_a_numeric and is_side_b_numeric and is_side_c_numeric):
        raise TypeError("All sides must be numeric values (int or float).")

    # Step 2: Validate that all sides are strictly positive.
    # A side length of zero or negative is physically impossible for a triangle.
    is_a_positive = side_a > 0
    is_b_positive = side_b > 0
    is_c_positive = side_c > 0

    if not (is_a_positive and is_b_positive and is_c_positive):
        return False

    # Step 3: Check the Triangle Inequality Theorem.
    # For sides a, b, and c to form a triangle, the following three conditions must ALL be true:
    # 1. a + b > c
    # 2. a + c > b
    # 3. b + c > a
    # We compute these sums first to make the logic explicit.
    sum_ab = side_a + side_b
    sum_ac = side_a + side_c
    sum_bc = side_b + side_c

    is_ab_greater_than_c = sum_ab > side_c
    is_ac_greater_than_b = sum_ac > side_b
    is_bc_greater_than_a = sum_bc > side_a

    # The triangle is valid only if all three inequality conditions are met.
    return is_ab_greater_than_c and is_ac_greater_than_b and is_bc_greater_than_a


def _is_numeric_value(value: any) -> bool:
    """
    Helper function to check if a value is an integer or a float.
    This is used to validate input types before performing arithmetic comparisons.

    Parameters:
        value (any): The value to check.

    Returns:
        bool: True if the value is an int or a float, False otherwise.
    """
    # Note: In strict Python, we might use isinstance(value, (int, float))
    # However, we must be careful not to accept boolean values (bool is a subclass of int).
    # Although the problem description implies geometric sides, good defensive code
    # often treats booleans as invalid inputs for geometric measurements.
    # Based on standard behavior for such problems, we exclude booleans to be strict.

    if type(value) is bool:
        return False

    if isinstance(value, (int, float)):
        return True

    return False