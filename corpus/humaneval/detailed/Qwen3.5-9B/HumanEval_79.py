import re

def _validate_decimal_input(value):
    """
    Validates that the input is a valid non-negative integer.

    Args:
        value: The input value to validate.

    Raises:
        TypeError: If the input is not an integer or a float representing an integer.
        ValueError: If the input is negative, non-integer float, or NaN/Infinity.
    """
    # Check for NaN and Infinity
    import math
    if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
        raise ValueError("Input cannot be NaN or Infinity.")

    # Check type: must be int or float (that can be converted to int without loss)
    if isinstance(value, bool):
        raise TypeError("Input cannot be a boolean.")

    if isinstance(value, int):
        if value < 0:
            raise ValueError("Input must be a non-negative integer.")
        return True, int(value)

    if isinstance(value, float):
        # Check if it's an integer representation (e.g., 15.0)
        if not value.is_integer():
            raise ValueError("Input must be an integer value.")
        if value < 0:
            raise ValueError("Input must be a non-negative integer.")
        return True, int(value)

    raise TypeError(f"Input must be an integer, received {type(value).__name__}.")


def _decimal_to_binary_string(n):
    """
    Converts a non-negative integer to a binary string without '0b' prefix.

    Args:
        n: A non-negative integer.

    Returns:
        str: Binary representation consisting of '0's and '1's.
    """
    if n == 0:
        return "0"

    binary_digits = []
    current_number = n

    # Explicitly perform division and modulus to build binary string digit by digit
    while current_number > 0:
        remainder = current_number % 2
        binary_digits.append(str(remainder))
        current_number = current_number // 2

    # Digits are generated in reverse order (least significant first)
    binary_digits.reverse()
    return "".join(binary_digits)


def _format_with_boundaries(binary_content):
    """
    Wraps the binary content with 'db' at the beginning and end.

    Args:
        binary_content: The string containing only '0' and '1'.

    Returns:
        str: The formatted string with 'db' boundaries.
    """
    return "db" + binary_content + "db"


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
    # Step 1: Validate the input explicitly
    is_valid, validated_value = _validate_decimal_input(decimal)

    if not is_valid:
        # This line should theoretically not be reached due to explicit raising in validator
        raise Exception("Input validation failed.")

    # Step 2: Convert the validated integer to a binary string
    binary_representation = _decimal_to_binary_string(validated_value)

    # Step 3: Apply the boundary formatting
    final_result = _format_with_boundaries(binary_representation)

    return final_result