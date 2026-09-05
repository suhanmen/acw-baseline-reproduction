import re
from typing import Tuple, Any

def _validate_input(s: Any) -> str:
    """
    Validates that the input is a non-empty string.
    Raises a ValueError if the input is invalid.

    Args:
        s: The input to validate.

    Returns:
        The validated string.

    Raises:
        ValueError: If the input is not a string or is empty.
    """
    if not isinstance(s, str):
        raise ValueError(f"Input must be a string, got {type(s).__name__} instead.")

    if len(s) == 0:
        raise ValueError("Input string cannot be empty.")

    return s

def _construct_regex_pattern() -> str:
    """
    Constructs the regex pattern to match strings where the first and last
    characters are the same.

    Returns:
        A regex pattern string.
        The pattern uses ^ to match start, and $ to match end.
        It captures the first character and uses a backreference to ensure
        the last character is identical.
        The middle portion (.*) is greedy and matches any characters in between.
    """
    # The pattern logic:
    # ^       : Assert start of string
    # (.)     : Capture group 1, matches exactly one character (the first one)
    # .*      : Matches any sequence of characters (including empty sequence)
    # \\1     : Backreference to group 1, ensuring the next character (last one) is the same
    # $       : Assert end of string
    # Note: We anchor the backreference to the end. Since .* is greedy, it will 
    # consume as much as possible, leaving the very last character for \\1 to match.

    return r"^(.).*\\1$"

def _check_regex_match(pattern_str: str, text: str) -> bool:
    """
    Attempts to match the compiled pattern against the text.

    Args:
        pattern_str: The raw pattern string to compile and use.
        text: The text to test against the pattern.

    Returns:
        True if the entire text matches the pattern, False otherwise.
    """
    try:
        compiled_pattern = re.compile(pattern_str)
        # fullmatch ensures the entire string matches the pattern, not just a part of it
        # match would only check from the start, so fullmatch is semantically correct here.
        return bool(compiled_pattern.fullmatch(text))
    except re.error as e:
        # In a production environment, we might want to log this or handle it differently.
        # Here we re-raise as a generic error or return False depending on strictness.
        # For this specific problem, a malformed pattern is an internal error.
        raise RuntimeError(f"Invalid regular expression pattern provided: {e}") from e

def check_char(input_string: Any) -> str:
    """
    Checks whether the given string starts and ends with the same character.
    Uses regular expressions to perform the check.

    Args:
        input_string: The string to be checked.

    Returns:
        "Valid" if the string starts and ends with the same character.
        "Invalid" otherwise.

    Raises:
        ValueError: If the input is not a valid non-empty string.
    """
    # Step 1: Validate the input to ensure it is a non-empty string.
    validated_string = _validate_input(input_string)

    # Step 2: Construct the regex pattern.
    # Pattern: ^(.).*\1$
    # Explanation:
    # ^ - Start of string
    # (.) - Capture the first character
    # .* - Match any characters in between (zero or more)
    # \1 - Match the exact character captured in the first group (the last character)
    # $ - End of string
    regex_pattern = _construct_regex_pattern()

    # Step 3: Perform the regex check.
    is_match = _check_regex_match(regex_pattern, validated_string)

    # Step 4: Return the appropriate result string based on the match.
    if is_match:
        return "Valid"
    else:
        return "Invalid"