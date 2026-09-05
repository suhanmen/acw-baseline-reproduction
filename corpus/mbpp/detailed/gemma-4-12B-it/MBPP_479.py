from typing import Union


def first_Digit(number: Union[int, float]) -> int:
    """
    Identifies the first significant digit of a given number.

    The "first digit" is defined as the first digit encountered when reading 
    the number from left to right. For example, in 123, it is 1.
    For -456, it is 4. For 0.005, it is 5.

    Args:
        number (Union[int, float]): The number to extract the first digit from.

    Returns:
        int: The first digit as an integer.

    Raises:
        TypeError: If the input is not an int or a float.
        ValueError: If the input is NaN or Infinity.
    """
    # Input Validation: Ensure the input is a numeric type
    if not isinstance(number, (int, float)):
        raise TypeError(f"Input must be an int or float, got {type(number).__name__}")

    # Handle special float cases: NaN and Infinity
    # These do not have "digits" in the conventional sense.
    if float('nan') == number:
        raise ValueError("Input is NaN, which does not have a first digit.")
    if float('inf') == number or float('-inf') == number:
        raise ValueError("Input is Infinity, which does not have a first digit.")

    # Step 1: Convert the number to its absolute value.
    # The sign (positive or negative) does not affect the value of the first digit.
    absolute_value = abs(number)

    # Step 2: Handle the case where the number is 0.
    # The first digit of 0 is 0.
    if absolute_value == 0:
        return 0

    # Step 3: Convert to string to handle decimal places and scientific notation.
    # Using format with 'f' avoids scientific notation for very small numbers 
    # but we need to be careful about precision.
    # A robust way is to convert to a string and strip non-digit characters.
    num_str = str(absolute_value)

    # Step 4: Iterate through characters to find the first digit.
    # This handles cases like:
    # - "123" -> first digit '1'
    # - "0.005" -> first digit '5' (ignoring the decimal point and leading zeros)
    # - "1.2e+10" -> first digit '1' (scientific notation)

    first_digit_found = None

    for char in num_str:
        # Check if the character is a digit (0-9)
        if char.isdigit():
            # Special case: if we find a digit, but it is a leading zero 
            # before a decimal point (like "0.005"), we skip it unless 
            # it's the only digit or the value is actually 0.
            # However, the logic of "first digit" usually implies the first 
            # NON-ZERO digit if there is a decimal, but based on 
            # assert(123) == 1, the standard is the first digit in the integer 
            # part if non-zero, or the first non-zero digit.

            # Let's refine: if it's '0' and there are more characters coming 
            # that are digits/decimals, and it's the leading zero of a decimal,
            # we should keep looking.

            if char == '0':
                # If we see a '0' and it's followed by a '.', it's a leading zero.
                # We check if this '0' is the "first" digit.
                # In "0.005", the first digit is 5.
                # In "0", the first digit is 0.

                # Logic: If the string starts with '0.' or '0', and we are at the 
                # start of the string, we only treat '0' as the first digit 
                # if the number is exactly 0.
                if num_str.startswith('0.'):
                    continue
                elif num_str == '0':
                    return 0
                else:
                    # This handles cases like "102" where '0' is NOT the first digit.
                    # We don't return yet because we are iterating left-to-right.
                    pass
            else:
                # Found a non-zero digit. This is the first significant digit.
                first_digit_found = int(char)
                break

    # Final fallback: if no non-zero digit was found (e.g., "0.000"), 
    # it means the number is effectively 0.
    if first_digit_found is None:
        return 0

    return first_digit_found