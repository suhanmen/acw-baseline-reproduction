def even_or_odd(hex_string: str) -> str:
    """
    Checks whether a hexadecimal number is even or odd.

    Args:
        hex_string (str): A string representing a hexadecimal number.

    Returns:
        str: "Even" if the number is even, "Odd" otherwise.
    """
    # Convert the hexadecimal string to an integer using base 16
    decimal_value = int(hex_string, 16)

    # Check if the decimal value is even or odd
    if decimal_value % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    assert even_or_odd("AB3454D") == "Odd"
    assert even_or_odd("ABC") == "Even"
    assert even_or_odd("AAD") == "Odd"