import typing

def check_integer(input_string: str) -> bool:
    """
    Determines whether a given string represents a valid integer.

    A valid integer string:
    - Can represent a positive integer (e.g., "123").
    - Can represent a negative integer (e.g., "-123").
    - Can represent zero (e.g., "0" or "-0").
    - Does not contain decimal points, spaces, or alphabetic characters.
    - Is not an empty string.

    Args:
        input_string (str): The string to validate.

    Returns:
        bool: True if the string is a valid integer, False otherwise.
    """

    # Requirement: Handle non-string inputs gracefully.
    # Although the signature implies a string, defensive programming
    # ensures we don't crash on unexpected types.
    if not isinstance(input_string, str):
        return False

    # Edge Case: Empty string is not an integer.
    if len(input_string) == 0:
        return False

    # Edge Case: A single character that is just a sign (e.g., "-" or "+")
    # is not an integer.
    if len(input_string) == 1:
        if input_string == "-" or input_string == "+":
            return False
        # If it's a single digit, it's valid.
        # We'll let the logic below handle single digits.

    # Step 1: Identify the sign.
    # We use a pointer/index to track where the numeric part starts.
    start_index = 0
    is_negative = False

    if input_string[0] == '-':
        is_negative = True
        start_index = 1
    elif input_string[0] == '+':
        # Explicitly handle the plus sign.
        start_index = 1

    # After handling the sign, check if there are any remaining characters.
    # If the string was just "-" or "+", the substring will be empty.
    numeric_part = input_string[start_index:]

    if len(numeric_part) == 0:
        return False

    # Step 2: Validate that every character in the numeric part is a digit.
    # We iterate explicitly to ensure production-grade readability.
    for char in numeric_part:
        # We check if the character is a digit (0-9).
        # This excludes decimals (.), spaces, and exponents (e).
        if not char.isdigit():
            return False

    # Step 3: Final verification.
    # At this point, we have confirmed the string consists of an optional sign
    # followed by one or more digits.
    return True

# The following assertions verify the requirements.
if __name__ == "__main__":
    assert check_integer("python") == False
    assert check_integer("1") == True
    assert check_integer("12345") == True
    # Additional defensive checks
    assert check_integer("-50") == True
    assert check_integer("+100") == True
    assert check_integer("0") == True
    assert check_integer("") == False
    assert check_integer("1.5") == False
    assert check_integer(" 123 ") == False
    assert check_integer("-") == False
    assert check_integer("+") == False
    assert check_integer("12a3") == False