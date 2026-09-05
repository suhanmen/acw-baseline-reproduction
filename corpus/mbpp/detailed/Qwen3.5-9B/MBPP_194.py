def _validate_octal_string(input_string):
    """
    Validates that the input string represents a valid non-negative octal number.

    Rules:
    1. The string must not be empty.
    2. The string must contain only digits from '0' to '7'.
    3. The string must not have any leading/trailing whitespace.

    Raises:
        ValueError: If the input string is invalid.
    """
    # Check for empty string or None after stripping
    if not input_string:
        raise ValueError("Input string cannot be empty.")

    # Normalize whitespace: strip leading and trailing whitespace
    normalized_string = input_string.strip()

    if not normalized_string:
        raise ValueError("Input string contains only whitespace.")

    # Check for negative sign (octal numbers in this context are treated as non-negative representations)
    # The problem examples use positive integers. If a sign is present, we treat it as invalid 
    # unless we are strictly parsing a signed integer, but standard octal conversion implies non-negative.
    # Based on examples (25, 30, 40), we expect pure digit strings.
    if normalized_string.startswith('-'):
        raise ValueError("Negative numbers are not supported in this octal to decimal conversion.")

    # Iterate over every character to ensure it is a valid octal digit (0-7)
    for index, char in enumerate(normalized_string):
        if not ('0' <= char <= '7'):
            raise ValueError(f"Invalid character '{char}' at position {index}. Octal digits must be between '0' and '7'.")

    return normalized_string


def _convert_digit_to_value(char):
    """
    Converts a single octal digit character to its integer value.

    Args:
        char (str): A single character representing an octal digit.

    Returns:
        int: The integer value of the octal digit (0-7).
    """
    # While ord() could be used, explicit logic is clearer and more defensive
    if char == '0':
        return 0
    elif char == '1':
        return 1
    elif char == '2':
        return 2
    elif char == '3':
        return 3
    elif char == '4':
        return 4
    elif char == '5':
        return 5
    elif char == '6':
        return 6
    elif char == '7':
        return 7
    else:
        # This case should theoretically never be reached if validation passes
        raise ValueError(f"Unexpected character logic error for: {char}")


def octal_To_Decimal(octal_string):
    """
    Converts a string representation of an octal number to its decimal (base-10) integer equivalent.

    The function performs strict validation on the input string to ensure it is a valid 
    non-negative octal number consisting solely of digits 0-7.

    Algorithm:
    1. Validate the input string format.
    2. Initialize an accumulator variable for the result.
    3. Iterate through each character of the string from left to right.
    4. Convert the current character to its integer octal value.
    5. Multiply the current result by the base (8) and add the new digit's value.
    6. Return the final accumulated integer.

    Args:
        octal_string (str): A string representing a non-negative octal number.

    Returns:
        int: The decimal equivalent of the input octal number.

    Raises:
        ValueError: If the input string is not a valid octal number representation.
    """
    # Step 1: Validate the input string
    validated_string = _validate_octal_string(octal_string)

    # Initialize the result accumulator
    decimal_value = 0

    # Process each digit in the string
    # We iterate from the most significant digit (left) to the least significant (right)
    for digit_char in validated_string:
        # Convert the current character to its integer value
        current_digit_value = _convert_digit_to_value(digit_char)

        # Shift the current total to the left (multiply by base 8)
        # and add the current digit's value
        decimal_value = (decimal_value * 8) + current_digit_value

    return decimal_value