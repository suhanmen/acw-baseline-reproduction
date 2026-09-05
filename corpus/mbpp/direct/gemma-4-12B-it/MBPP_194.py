def octal_To_Decimal(octal_num: int) -> int:
    """
    Converts an octal number (represented as an integer) to its decimal equivalent.

    Args:
        octal_num (int): The number in octal format.

    Returns:
        int: The number in decimal format.
    """
    # Convert the integer to a string to iterate through digits,
    # then calculate the decimal value using the power of 8.
    octal_str = str(octal_num)
    decimal_val = 0
    for i, digit in enumerate(reversed(octal_str)):
        decimal_val += int(digit) * (8 ** i)
    return decimal_val

if __name__ == "__main__":
    assert octal_To_Decimal(25) == 21
    assert octal_To_Decimal(30) == 24
    assert octal_To_Decimal(40) == 32