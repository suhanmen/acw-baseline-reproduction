def binary_to_decimal(binary_num: int) -> int:
    """
    Converts a binary number (represented as an integer) to its decimal equivalent.
    """
    # Convert the integer to a string to iterate through each digit
    binary_str = str(binary_num)
    decimal_val = 0

    # Calculate the decimal value based on the position of each bit
    for i, digit in enumerate(reversed(binary_str)):
        if digit == '1':
            decimal_val += 2 ** i

    return decimal_val

if __name__ == "__main__":
    assert binary_to_decimal(100) == 4
    assert binary_to_decimal(1011) == 11
    assert binary_to_decimal(1101101) == 109