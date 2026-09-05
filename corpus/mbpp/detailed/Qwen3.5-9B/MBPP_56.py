def get_reverse_of_number(number: int) -> int:
    """
    Calculates the reverse of a given integer.

    This function handles negative numbers by preserving the sign,
    reversing the absolute value of the number, and then reapplying the sign.
    Leading zeros in the reversed string representation are naturally handled
    by integer conversion (e.g., reverse of 120 is 21).

    Args:
        number (int): The integer to be reversed.

    Returns:
        int: The reversed integer.
    """
    if not isinstance(number, int):
        raise TypeError(f"Expected an integer, got {type(number).__name__}")

    original_number = number

    # Handle zero explicitly, though the math below handles it too,
    # this makes the intent clear for the degenerate case.
    if number == 0:
        return 0

    # Determine the sign of the number
    sign = -1 if number < 0 else 1

    # Work with the absolute value to handle negative numbers cleanly
    abs_number = abs(number)

    # Perform the reversal using integer arithmetic
    reversed_value = 0
    current_value = abs_number

    while current_value != 0:
        digit = current_value % 10
        current_value = current_value // 10
        reversed_value = (reversed_value * 10) + digit

    # Reapply the original sign
    reversed_number = sign * reversed_value

    return reversed_number


def check_number_property(number: int) -> bool:
    """
    Checks if a given number is exactly one less than twice its reverse.

    The mathematical condition implemented is:
        number == (2 * reverse(number)) - 1

    This function includes explicit input validation to ensure the input
    is a standard integer (int). It rejects booleans (which are subclasses
    of int in Python) and non-integer types.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number satisfies the condition, False otherwise.

    Raises:
        TypeError: If the input is not a valid integer type.
    """
    # Explicit validation for input type
    # Note: We must exclude booleans because isinstance(True, int) is True
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError(
            f"Input must be a standard integer (int), got {type(number).__name__}"
        )

    # Retrieve the reversed number using our helper
    reversed_number = get_reverse_of_number(number)

    # Calculate twice the reversed number
    twice_reversed = reversed_number * 2

    # Calculate one less than twice the reversed number
    target_value = twice_reversed - 1

    # Compare the original number with the calculated target value
    is_match = (number == target_value)

    return is_match