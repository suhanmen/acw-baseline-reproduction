import re
from typing import Final

def is_allowed_specific_char(input_string: str) -> bool:
    """
    Validates if the provided string contains only lowercase letters (a-z),
    uppercase letters (A-Z), and digits (0-9).

    The validation is performed using a regular expression.

    Args:
        input_string (str): The string to be validated.

    Returns:
        bool: True if the string contains only allowed characters, False otherwise.

    Raises:
        TypeError: If the input_string is not of type str.
    """

    # Defensive check: Ensure the input is a string.
    # Production-grade code should not assume the caller is correct.
    if not isinstance(input_string, str):
        raise TypeError(f"Expected input type 'str', but received '{type(input_string).__name__}'")

    # Handle the degenerate case of an empty string.
    # Depending on the specific requirements, an empty string might be considered valid 
    # as it contains no forbidden characters. Based on the provided assertions, 
    # we assume any string that does not contain forbidden characters is valid.
    if len(input_string) == 0:
        return True

    # Define the allowed character set:
    # a-z: lowercase letters
    # A-Z: uppercase letters
    # 0-9: digits
    # The regex ^[a-zA-Z0-9]*$ ensures that:
    # ^       : The match starts at the beginning of the string.
    # [ ... ] : A character class containing the allowed characters.
    # *       : Matches zero or more of the preceding characters.
    # $       : The match ends at the very end of the string.
    # If any character outside this range exists, the regex will fail to match the whole string.

    ALLOWED_PATTERN: Final[str] = r"^[a-zA-Z0-9]*$"

    try:
        # Compile the regular expression for performance and clarity.
        # Using re.fullmatch is also an option, but explicit start/end anchors 
        # with re.match is highly standard and readable.
        pattern_object = re.compile(ALLOWED_PATTERN)

        # Perform the match.
        # re.match checks from the beginning of the string.
        # Because we included the '$' anchor, it forces the entire string to comply.
        match_result = pattern_object.match(input_string)

        # Check if the match was successful.
        if match_result is not None:
            # The string strictly contains only allowed characters.
            return True
        else:
            # The string contains at least one character not in the allowed set.
            return False

    except re.error as e:
        # This block handles potential regex engine issues, though 
        # our pattern is constant and safe.
        print(f"Internal Regex Error: {e}")
        return False

# The following assertions verify the correctness of the implementation.
if __name__ == "__main__":
    # Test Case 1: Mixed alphanumeric (Valid)
    assert is_allowed_specific_char("ABCDEFabcdef123450") == True

    # Test Case 2: Special characters (Invalid)
    assert is_allowed_specific_char("*&%@#!}{") == False

    # Test Case 3: Mixed alphanumeric (Valid)
    assert is_allowed_specific_char("HELLOhowareyou98765") == True

    # Additional edge cases for robustness
    assert is_allowed_specific_char("") == True  # Empty string
    assert is_allowed_specific_char("a") == True  # Single valid char
    assert is_allowed_specific_char(" ") == False # Space is not allowed
    assert is_allowed_specific_char("123") == True # Only digits
    assert is_allowed_specific_char("abc") == True # Only letters