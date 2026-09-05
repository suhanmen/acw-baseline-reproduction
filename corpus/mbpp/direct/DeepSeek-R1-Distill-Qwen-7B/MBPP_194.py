def octal_to_decimal(octal_number):
    """
    Convert an octal number to a decimal number.

    Args:
        octal_number (str): The octal number to convert. Should only contain digits 0-7.

    Returns:
        int: The decimal equivalent of the octal number.

    Raises:
        ValueError: If the input is not a valid octal number.
    """
    if not all(c in '01234567' for c in octal_number):
        raise ValueError("Invalid octal number")

    decimal_value = 0
    for digit in octal_number:
        decimal_value = decimal_value * 8 + int(digit)
    return decimal_value

# Verify the solution with provided test cases
assert octal_to_decimal('25') == 21, "Test case 25 failed"
assert octal_to_decimal('30') == 24, "Test case 30 failed"
assert octal_to_decimal('40') == 32, "Test case 40 failed"
print("All test cases passed successfully!")