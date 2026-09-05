def binary_to_integer(binary_tuple: tuple) -> str:
    """
    Converts a binary tuple to its decimal integer representation as a string.
    """
    decimal_value = 0
    for bit in binary_tuple:
        decimal_value = (decimal_value << 1) | bit
    return str(decimal_value)