def _is_perfect_square(value: int) -> bool:
    """
    Determine if an integer is a perfect square.

    A perfect square is an integer that is the square of an integer.
    For example, 0, 1, 4, 9, 16 are perfect squares.

    This function handles negative numbers, zero, and positive integers.
    Negative numbers are never perfect squares in the real number domain.

    Parameters:
        value (int): The integer to check.

    Returns:
        bool: True if value is a perfect square, False otherwise.
    """
    # Negative numbers cannot be perfect squares
    if value < 0:
        return False

    # Zero is a perfect square (0 = 0^2)
    if value == 0:
        return True

    # For positive numbers, we calculate the integer square root
    # and check if squaring it returns the original number.
    root = int(value ** 0.5)

    # Check if the root is exact
    return (root * root) == value


def _validate_input(number: int) -> None:
    """
    Validate the input to ensure it meets the expected criteria.

    The problem implies we are dealing with integers.
    We will raise a TypeError if the input is not an integer.
    We allow zero and negative integers for validation purposes,
    though the logic may return False for them based on mathematical properties.

    Parameters:
        number (int): The integer to validate.

    Raises:
        TypeError: If the input is not an integer.
    """
    if not isinstance(number, int):
        raise TypeError(f"Input must be an integer, got {type(number).__name__}")


def prod_Square(number: int) -> bool:
    """
    Check whether the given number can be represented by the product of two squares.

    Mathematical Derivation:
    A number N is a product of two squares if there exist integers a and b such that:
        N = a^2 * b^2
    This can be rewritten as:
        N = (a * b)^2
    Therefore, N must itself be a perfect square.

    If N is a perfect square, say N = k^2, then we can always choose a = k and b = 1.
    Then N = k^2 * 1^2, which satisfies the condition.
    So the problem reduces to checking if the number is a perfect square.

    Edge Cases Considered:
    - Negative numbers: Not perfect squares (return False).
    - Zero: 0 = 0^2 * 1^2 (return True).
    - One: 1 = 1^2 * 1^2 (return True).
    - Non-square positive integers: Return False.

    Parameters:
        number (int): The integer to check.

    Returns:
        bool: True if number is a product of two squares, False otherwise.

    Raises:
        TypeError: If the input is not an integer.
    """
    # Step 1: Validate the input type explicitly
    _validate_input(number)

    # Step 2: Determine if the number is a perfect square.
    # Based on the derivation, N is a product of two squares IF AND ONLY IF N is a perfect square.
    is_perfect = _is_perfect_square(number)

    # Step 3: Return the result
    return is_perfect