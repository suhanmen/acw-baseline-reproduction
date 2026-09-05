def check_integer(candidate_string: str) -> bool:
    """
    Determines whether the given string represents a valid integer.

    This function validates the input strictly according to standard integer formatting rules:
    - The string must not be empty.
    - The string must consist solely of digits (0-9), with an optional leading '+' or '-'.
    - If a sign is present, it must be the very first character.
    - If a sign is present, at least one digit must follow.
    - If no sign is present, the string must contain at least one digit.
    - Whitespace is not allowed.

    Parameters
    ----------
    candidate_string : str
        The string to evaluate.

    Returns
    -------
    bool
        True if the string represents a valid integer, False otherwise.
    """

    # Define a set of valid characters that can appear in an integer string.
    # These are digits, plus sign, minus sign, and newline (for explicit handling below if needed).
    # However, standard integer representation usually forbids newline unless specified.
    # Based on standard interpretation: only digits, '+', '-'.
    VALID_DIGIT_CHARS = set('0123456789')
    VALID_SIGN_CHARS = set('+-')

    # Helper function to validate the sign character
    def is_valid_sign_char(char: str) -> bool:
        return char in VALID_SIGN_CHARS

    # Helper function to validate digit character
    def is_valid_digit_char(char: str) -> bool:
        return char in VALID_DIGIT_CHARS

    # Edge Case: Handle empty string explicitly
    if candidate_string == "":
        return False

    # Edge Case: Handle string with only whitespace (if any) explicitly
    # Although the problem implies simple strings, defensive coding suggests checking for invisible chars.
    # We will treat any whitespace as invalid unless the string is empty (handled above).
    # Python's .isspace() handles standard whitespace.
    if candidate_string.isspace():
        return False

    # Edge Case: Check for leading or trailing whitespace immediately
    # Even if .isspace() returned False, we should ensure no spaces are present anywhere.
    if " " in candidate_string:
        return False

    # Initialize state tracking variables
    has_sign = False
    sign_char_at_start = False
    seen_digit = False

    # Iterate through the string character by character
    for current_index in range(0, len(candidate_string)):
        current_char = candidate_string[current_index]

        # Check for sign characters
        if current_char in VALID_SIGN_CHARS:
            # If we already encountered a sign, having another sign is invalid (e.g., "++1", "+-1")
            if has_sign:
                return False

            # Mark that we have seen a sign
            has_sign = True

            # Check if this sign is at the very beginning of the string
            if current_index == 0:
                sign_char_at_start = True
            else:
                # A sign found later in the string (not at start) is invalid
                return False
            continue

        # If we are here, the character is not a sign. It must be a digit.
        if not is_valid_digit_char(current_char):
            # If it's not a sign and not a digit, it's an invalid character
            return False

        # Mark that we have seen at least one digit
        seen_digit = True

    # Final validation logic based on state variables:
    # 1. If a sign was present, we MUST have seen a digit after it.
    #    (e.g., "+", "-0" -> True, "+" -> False)
    if has_sign and not seen_digit:
        return False

    # 2. If no sign was present, we MUST have seen a digit.
    #    (e.g., "" -> False, "abc" -> False, "1" -> True)
    # Note: The empty string case was already handled at the start, but this ensures
    # consistency if the logic were refactored.
    if not has_sign and not seen_digit:
        return False

    # If all checks pass, the string is a valid integer representation
    return True