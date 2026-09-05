def octal_to_decimal(number):
    """
    Convert an octal number to its decimal equivalent.

    Args:
        number (str): A string representing an octal number.

    Returns:
        int: The decimal value of the octal number.

    Raises:
        ValueError: If the input is not a valid octal number.
    """
    # Handle empty input
    if not number:
        return 0

    # Check if all characters are valid octal digits
    if not all(c in '01234567' for c in number):
        raise ValueError("Invalid octal digit found")

    # Handle single-digit case
    if len(number) == 1:
        return int(number)

    # Convert each character to an integer
    digits = [int(c) for c in number]

    decimal_value = 0
    base = 8

    # Calculate the decimal value
    for i, digit in enumerate(reversed(digits)):
        decimal_value += digit * (base ** i)

    return decimal_value