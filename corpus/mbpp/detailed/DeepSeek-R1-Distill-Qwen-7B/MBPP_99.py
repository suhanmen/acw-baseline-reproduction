def decimal_to_binary(decimal):
    """
    Convert a decimal number to its binary equivalent.

    Args:
        decimal (int): The decimal number to convert. Must be a non-negative integer.

    Returns:
        str: The binary representation as a string.

    Raises:
        ValueError: If the input is not a non-negative integer.
    """
    # Input validation
    if not isinstance(decimal, int):
        raise ValueError("Input must be an integer.")
    if decimal < 0:
        raise ValueError("Input must be a non-negative integer.")
    if decimal == 0:
        return '0'

    # Conversion logic
    binary_digits = []
    while decimal > 0:
        remainder = decimal % 2
        binary_digits.append(str(remainder))
        decimal = decimal // 2

    # Reverse to get the correct binary order
    binary_digits.reverse()

    return ''.join(binary_digits)