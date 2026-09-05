import math

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

    # Define the prefix and suffix required by the format
    prefix = "db"
    suffix = "db"

    # Input validation: ensure the input is an integer
    # We use isinstance to strictly check for int type.
    if not isinstance(decimal, int):
        raise TypeError(f"Input must be an integer. Received: {type(decimal)}")

    # Handle negative numbers: 
    # Standard binary conversion for negative numbers varies (Two's complement, etc.)
    # However, based on the examples (15 -> 1111, 32 -> 100000), 
    # the function expects the magnitude conversion.
    # If negative is not allowed, we could raise a ValueError. 
    # Here we take the absolute value to ensure the binary conversion logic works.
    absolute_value = abs(decimal)

    # Handle the specific edge case of 0.
    # bin(0) returns '0b0', so we need to handle it to get "db0db".
    if absolute_value == 0:
        binary_string = "0"
    else:
        # Convert the decimal to a binary string.
        # bin() returns a string prefixed with '0b', e.g., bin(15) -> '0b1111'
        raw_binary_representation = bin(absolute_value)

        # Remove the '0b' prefix using string slicing.
        # We start from index 2 to skip '0' and 'b'.
        binary_string = raw_binary_representation[2:]

    # Construct the final result by concatenating prefix, binary string, and suffix.
    result = prefix + binary_string + suffix

    return result