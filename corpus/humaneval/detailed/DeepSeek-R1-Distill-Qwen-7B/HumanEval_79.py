def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    if not isinstance(decimal, int):
        raise ValueError("Invalid input: decimal must be an integer.")

    if decimal == 0:
        binary_str = "0"
    else:
        is_negative = decimal < 0
        if is_negative:
            decimal = -decimal

        binary_digits = []
        while decimal > 0:
            remainder = decimal % 2
            binary_digits.append(str(remainder))
            decimal = decimal // 2

        if not binary_digits:
            binary_str = "0"
        else:
            binary_str = ''.join(reversed(binary_digits))

    if is_negative:
        binary_str = ''.join(reversed(binary_str))

    return f"db{binary_str}db"