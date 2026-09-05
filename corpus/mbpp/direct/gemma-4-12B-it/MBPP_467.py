def decimal_to_Octal(decimal_num: int) -> int:
    """
    Converts a decimal number to its octal representation as an integer.

    Args:
        decimal_num (int): The decimal integer to convert.

    Returns:
        int: The octal representation of the decimal number.
    """
    if decimal_num == 0:
        return 0

    octal_str = ""
    temp_num = decimal_num

    while temp_num > 0:
        remainder = temp_num % 8
        octal_str = str(remainder) + octal_str
        temp_num //= 8

    return int(octal_str)

if __name__ == "__main__":
    assert decimal_to_Octal(10) == 12
    assert decimal_to_Octal(2) == 2
    assert decimal_to_Octal(33) == 41