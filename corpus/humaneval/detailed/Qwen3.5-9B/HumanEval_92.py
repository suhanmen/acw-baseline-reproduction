import numbers

def _is_integer_like(value):
    """
    Check if a value is an integer.

    This function accepts integers (int) and floats (float) that have no fractional part.
    It explicitly rejects booleans (which are a subclass of int in Python) and 
    non-numeric types.

    Args:
        value: The value to check.

    Returns:
        bool: True if the value is considered an integer, False otherwise.
    """
    # Reject booleans first because True == 1 and False == 0, but they are not integers in the context of math problems usually.
    if isinstance(value, bool):
        return False

    # Must be a number type
    if not isinstance(value, numbers.Number):
        return False

    # If it's an int, it's valid. If it's a float, check the fractional part.
    if isinstance(value, int):
        return True

    # For other numeric types (like float), check if remainder is zero
    # Note: This handles float, and we've already excluded bool and non-numbers above.
    try:
        # Using % 1 is generally safe for standard floats, but let's be explicit.
        # However, direct modulo can sometimes have floating point representation issues 
        # (e.g., 3.0 % 1 might theoretically be slightly off in exotic systems, though unlikely in standard Python).
        # A safer approach for "is whole number" on floats is checking the value against its integer cast.
        if isinstance(value, float) and value.is_integer():
            return True
        return False
    except (TypeError, AttributeError):
        # Fallback for any weird numeric types that don't support is_integer or casting cleanly
        return False


def _is_integers(x, y, z):
    """
    Validate that all three inputs are integers.

    Args:
        x, y, z: The input values.

    Returns:
        bool: True if all are integers, False otherwise.
    """
    return _is_integer_like(x) and _is_integer_like(y) and _is_integer_like(z)


def _check_sum_condition(x, y, z):
    """
    Check if any of the three numbers is the sum of the other two.

    Logic:
    x == y + z
    OR
    y == x + z
    OR
    z == x + y

    Args:
        x, y, z: The integer values to compare.

    Returns:
        bool: True if the condition holds, False otherwise.
    """
    sum_yz = y + z
    sum_xz = x + z
    sum_xy = x + y

    condition_x = (x == sum_yz)
    condition_y = (y == sum_xz)
    condition_z = (z == sum_xy)

    return condition_x or condition_y or condition_z


def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.

    Examples
    any_int(5, 2, 7) ➞ True

    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True

    any_int(3.6, -2.2, 2) ➞ False



    '''
    # Step 1: Validate input count implicitly by using the provided signature.
    # The signature fixes 3 arguments, so we don't need an explicit length check for the list.
    # However, we must ensure we don't process non-numeric inputs.

    # Step 2: Check if all inputs are integers using our helper.
    # This handles cases like 3.0, 3.6, True, "3", None, etc.
    are_all_integers = _is_integers(x, y, z)

    # Early exit: if they are not all integers, return False immediately.
    if not are_all_integers:
        return False

    # Step 3: If they are integers, check the sum condition.
    is_sum_condition_met = _check_sum_condition(x, y, z)

    # Step 4: Return the result of the sum check.
    return is_sum_condition_met