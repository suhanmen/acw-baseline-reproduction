def decimal_to_binary(decimal_number):
    """
    Convert a decimal number to its binary representation as a string.

    Args:
        decimal_number (int): The decimal number to convert. Must be a non-negative integer.

    Returns:
        str: The binary representation of the number as a string.

    Raises:
        ValueError: If the input is not a valid non-negative integer.
    """
    # Validate input
    if not isinstance(decimal_number, int):
        raise ValueError("Input must be an integer.")
    if decimal_number < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Handle special case for zero
    if decimal_number == 0:
        return "0"

    # Convert to binary
    binary = ""
    n = decimal_number

    # Divide the number by 2 until we reach zero
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary  # Prepend the remainder
        n = n // 2

    return binary