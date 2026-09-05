import re
from typing import Optional

def _validate_input_string(input_string: str) -> str:
    """
    Validates that the input is indeed a string.

    Raises:
        TypeError: If the input is not a string.

    Returns:
        The validated string.
    """
    if not isinstance(input_string, str):
        raise TypeError(f"Input must be a string, got {type(input_string).__name__}")

    return input_string

def _pattern_matches_lowercase_sequence(match: re.Match) -> bool:
    """
    Helper function to ensure the regex match corresponds to lowercase letters.
    While the regex pattern itself guarantees this, this function makes the logic
    explicit for clarity and potential future modification if the rule changes.

    Args:
        match: The regex match object.

    Returns:
        True if the matched substring consists entirely of lowercase letters.
    """
    matched_text = match.group(0)

    # Check if the matched text is empty (shouldn't happen with the pattern, but for safety)
    if len(matched_text) == 0:
        return False

    # Check if every character is a lowercase letter
    for char in matched_text:
        if not char.islower():
            return False

    return True

def remove_lowercase(input_string: str) -> str:
    """
    Removes all contiguous substrings of lowercase letters from the given string.

    This function uses regular expressions to identify sequences of one or more
    lowercase ASCII letters and removes them from the input string.

    The process:
    1. Validates the input is a string.
    2. Defines a regex pattern to match one or more lowercase letters.
    3. Uses regex substitution to replace all matches with an empty string.

    Args:
        input_string: The source string to process.

    Returns:
        A new string with all lowercase letter sequences removed.

    Raises:
        TypeError: If the input is not a string.
    """

    # Step 1: Validate the input explicitly
    validated_input = _validate_input_string(input_string)

    # Step 2: Define the regular expression pattern.
    # The pattern '[a-z]+' matches one or more lowercase ASCII letters.
    # We use raw string notation for the regex pattern.
    lowercase_pattern: str = r'[a-z]+'

    # Step 3: Check for empty input early to avoid unnecessary processing,
    # though the regex logic handles it correctly anyway.
    if len(validated_input) == 0:
        return ""

    # Step 4: Perform the substitution.
    # re.sub(pattern, repl, string) replaces all occurrences of the pattern
    # with the replacement string. Here, we replace matches with an empty string.
    result_string: str = re.sub(lowercase_pattern, "", validated_input)

    return result_string