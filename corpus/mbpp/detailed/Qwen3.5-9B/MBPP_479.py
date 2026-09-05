def _is_valid_numeric_input(value: object) -> bool:
    """
    Check if the given value is a valid numeric input for the first digit extraction.

    Valid inputs are instances of int or float.
    This function does not check for the value itself (e.g., NaN or infinity),
    but rather the type conformity.

    Parameters:
    value (object): The input value to check.

    Returns:
    bool: True if the value is an int or float, False otherwise.
    """
    return isinstance(value, (int, float))

def _is_valid_non_negative_float(value: float) -> bool:
    """
    Check if a float value is valid for digit extraction.
    Negative numbers are allowed as per standard interpretation of "number",
    but the magnitude must be non-negative (which is always true for float).
    However, we must exclude NaN and Infinity.

    Parameters:
    value (float): The float value to check.

    Returns:
    bool: True if the value is a valid number (not NaN, not Inf), False otherwise.
    """
    import math
    if math.isnan(value):
        return False
    if math.isinf(value):
        return False
    return True

def _is_valid_non_negative_int(value: int) -> bool:
    """
    Check if an int value is valid for digit extraction.
    In Python, integers can be arbitrarily large, so we just check if it's not None (already handled by type check)
    and handles the zero case correctly.
    Since int cannot be NaN or Inf, we just return True for any int.
    However, we treat negative integers similarly: we extract digits from their absolute value.

    Parameters:
    value (int): The int value to check.

    Returns:
    bool: Always True for int type, as ints are always representable numbers.
    """
    return True

def _get_absolute_value(value: object) -> float:
    """
    Convert the input value to its absolute float representation.

    Parameters:
    value (object): The original numeric input.

    Returns:
    float: The absolute value of the input.
    """
    return abs(float(value))

def _extract_first_digit_from_integer(digit_str: str) -> int:
    """
    Given a string representation of an integer (possibly with leading zeros),
    extract the first digit.

    Parameters:
    digit_str (str): A string containing only digits (resulting from integer conversion).

    Returns:
    int: The first digit as an integer.
    """
    if len(digit_str) == 0:
        raise ValueError("String representation of the number cannot be empty.")

    first_char = digit_str[0]

    # Ensure the character is a valid digit
    if not first_char.isdigit():
        raise ValueError("Invalid input: characters other than digits found in integer part.")

    return int(first_char)

def _extract_first_digit_from_float(digit_str: str) -> int:
    """
    Given a string representation of a positive float (e.g., "123.456"),
    extract the first digit of the integer part.

    Parameters:
    digit_str (str): A string containing the number without signs, potentially containing a decimal point.

    Returns:
    int: The first digit as an integer.
    """
    if len(digit_str) == 0:
        raise ValueError("String representation of the number cannot be empty.")

    # Check for leading character
    first_char = digit_str[0]

    if not first_char.isdigit():
        raise ValueError("Invalid input: characters other than digits found at the start.")

    return int(first_char)

def _convert_number_to_string_representation(value: float) -> str:
    """
    Convert a float value to a string representation suitable for digit extraction.

    Parameters:
    value (float): The numeric value to convert.

    Returns:
    str: The string representation of the number.
    """
    # Using a generic string conversion might produce scientific notation for very large/small numbers.
    # However, for the purpose of "first digit", scientific notation (e.g., 1e2) starts with the coefficient.
    # To be robust and avoid scientific notation issues, we can construct a string manually or rely on default str().
    # Let's use str() first. If it results in '1e5', the first char is '1', which is correct.
    # But let's handle the specific case where str() might behave unexpectedly or if we want pure digit extraction.
    # Actually, for 123 -> "123", first is '1'. For 0.00123 -> "0.00123", first is '0'.
    # This matches the mathematical concept of the first digit of the number (0.00123 starts with 0 before decimal).
    # However, often "first digit" implies the first non-zero digit. 
    # Re-reading the problem: first_Digit(123)=1, first_Digit(12)=1.
    # It doesn't specify 0.001. Standard interpretation for "first digit of a number" usually includes the leading zero
    # if the number is between 0 and 1, OR it implies the most significant non-zero digit.
    # Given the examples are > 0 integers, let's assume standard string conversion behavior:
    # str(0.5) -> "0.5", first char '0'.
    # str(5) -> "5", first char '5'.
    # str(-5) -> "-5", first char '-'. We take absolute value before this.
    # Let's stick to str(abs(value)).

    return str(value)

def first_Digit(number: object) -> int:
    """
    Find the first digit of a given number.

    The function accepts integers and floating-point numbers.
    It validates the input types and handles edge cases such as zero, negative numbers,
    and boundary values explicitly.

    Parameters:
    number (object): The input number (int or float).

    Returns:
    int: The first digit of the number.

    Raises:
    TypeError: If the input is not an int or float.
    ValueError: If the input is NaN, Infinity, or a string (if passed as such in loose typing scenarios, though type check handles it).
    """

    # Step 1: Validate the input type
    if not _is_valid_numeric_input(number):
        raise TypeError(f"Input must be an int or float, got {type(number).__name__}.")

    # Step 2: Handle specific invalid float values (NaN, Inf) explicitly
    if _is_valid_non_negative_float(number) is False:
        raise ValueError("Input cannot be NaN or Infinity.")

    # Step 3: Convert the number to its absolute float value to handle negatives uniformly
    absolute_value = _get_absolute_value(number)

    # Step 4: Convert the absolute value to a string representation
    number_string = _convert_number_to_string_representation(absolute_value)

    # Step 5: Determine the logic path based on the presence of a decimal point or scientific notation
    # However, since we want the very first digit, we can simply check the first character.
    # But we must ensure the string is not just a sign (handled by abs) or empty.

    # Step 6: Extract the first character
    first_character = number_string[0]

    # Step 7: Verify the first character is a digit
    if not first_character.isdigit():
        # This case should theoretically not be reached if abs() and str() are used correctly
        # for standard numbers, as abs() removes the sign. 
        # Exception: If the number is 0.0, str is "0.0", first char '0'.
        # Exception: If the number is extremely small, str might be "0.0e-10", first char '0'.
        # Exception: If the number is extremely large, str might be "1e+100", first char '1'.
        raise ValueError(f"Unexpected character '{first_character}' found at the start of string '{number_string}'.")

    # Step 8: Return the integer value of the first character
    result = int(first_character)

    return result