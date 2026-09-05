def decimal_To_Binary(n):
    """
    Converts a decimal number to its binary representation as an integer.
    """
    if n == 0:
        return 0

    binary_str = ""
    while n > 0:
        binary_str = str(n % 2) + binary_str
        n = n // 2

    return int(binary_str)

if __name__ == "__main__":
    assert decimal_To_Binary(10) == 1010
    assert decimal_To_Binary(1) == 1
    assert decimal_To_Binary(20) == 10100