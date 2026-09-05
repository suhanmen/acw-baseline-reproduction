def last_Digit(n):
    """
    Returns the last digit of a given integer n.

    This function handles:
    - Positive integers
    - Negative integers (returns the last digit of the absolute value)
    - Zero

    Args:
        n (int): The integer number whose last digit is to be found.

    Returns:
        int: The last digit of the number n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not a finite number (though this is less common for int type).
    """
    # Validate input type
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    # Handle edge case: zero
    if n == 0:
        return 0

    # Handle negative numbers by taking absolute value
    # This ensures consistent behavior for negative inputs
    # e.g., -123 -> 3
    abs_value = abs(n)

    # Extract the last digit using modulo operation
    last_digit = abs_value % 10

    return last_digit