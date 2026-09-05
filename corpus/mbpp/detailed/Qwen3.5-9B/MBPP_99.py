def _validate_input(value):
    """
    Validates that the input is an integer and is non-negative.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is negative.
    """
    # Check for integer type explicitly (excluding bool, which is a subclass of int)
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"Input must be an integer, got {type(value).__name__}")

    # Check for non-negative constraint
    if value < 0:
        raise ValueError(f"Input must be a non-negative integer, got {value}")


def _convert_decimal_to_binary_core(value):
    """
    Performs the core conversion from decimal to binary using the division-by-2 algorithm.

    Algorithm:
    1. If the number is 0, return '0'.
    2. Repeatedly divide the number by 2.
    3. Collect the remainders in reverse order of generation.
    4. Join the collected remainders to form the binary string.

    Args:
        value (int): The non-negative integer to convert.

    Returns:
        str: The binary representation of the input value.
    """
    # Edge case: Zero
    if value == 0:
        return '0'

    # List to store binary digits
    binary_digits = []

    # Working variable for the loop
    current_number = value

    # Loop until the current number is reduced to 0
    while current_number > 0:
        # Calculate the remainder (0 or 1)
        remainder = current_number % 2

        # Append the remainder as a string to the list
        binary_digits.append(str(remainder))

        # Update the current number for the next iteration
        current_number = current_number // 2

    # The list contains digits in reverse order (least significant first)
    # Join them to form the final binary string
    result_string = ''.join(reversed(binary_digits))

    return result_string


def decimal_to_binary(value):
    """
    Converts a given decimal number to its binary equivalent as a string.

    This function validates the input to ensure it is a non-negative integer.
    It handles edge cases such as 0 and large numbers efficiently using
    iterative division.

    Args:
        value (int): A non-negative integer to be converted to binary.

    Returns:
        str: The binary representation of the input value.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is negative.

    Examples:
        >>> decimal_to_binary(8)
        '1000'
        >>> decimal_to_binary(18)
        '10010'
        >>> decimal_to_binary(7)
        '111'
        >>> decimal_to_binary(0)
        '0'
    """
    # Step 1: Validate the input
    _validate_input(value)

    # Step 2: Perform the conversion
    binary_representation = _convert_decimal_to_binary_core(value)

    # Step 3: Return the result
    return binary_representation