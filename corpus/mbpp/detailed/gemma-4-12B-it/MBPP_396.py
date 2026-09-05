import re
from typing import Union

def check_char(input_string: str) -> str:
    """
    Checks whether the given string starts and ends with the same character 
    using a regular expression.

    Args:
        input_string (str): The string to validate.

    Returns:
        str: "Valid" if the string starts and ends with the same character, 
             otherwise "Invalid".
    """
    # Handle case where input is not a string
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string.")

    # Handle empty string edge case
    # An empty string does not have a starting or ending character to compare.
    if len(input_string) == 0:
        return "Invalid"

    # Handle single character string edge case
    # A single character is both the start and the end character.
    if len(input_string) == 1:
        return "Valid"

    # Regex explanation:
    # ^         : Start of the string
    # (.)       : Capture group 1: Match any character (except newline)
    # .*        : Match any sequence of characters in between
    # \1        : Back-reference to Capture group 1 (must match the first char)
    # $         : End of the string
    #
    # Note: Since regex engine evaluates from left to right, we use a 
    # back-reference to ensure the last character matches the first.

    # We use re.DOTALL to ensure '.' matches newlines if they are present.
    pattern = r"^(.).*\1$"

    # Perform the regex match
    match_result = re.match(pattern, input_string, re.DOTALL)

    # Check if the regex matched the full logic
    if match_result is not None:
        return "Valid"
    else:
        # Special case check: The regex ^(.).*\1$ requires at least 
        # two characters to match (start char and end char).
        # However, the problem logic implies that for a string like "aa",
        # it is Valid. 
        # If the string is "aba", it is Valid.
        # If the string is "abc", it is Invalid.

        # Let's double check the regex logic for strings of length 2.
        # Example "aa": ^(a).*\1$ -> (a) matches 'a', .* matches empty, \1 matches 'a'. Result: Valid.

        # Since we already handled length 1, and length 0,
        # and the regex handles length >= 2, this is exhaustive.
        return "Invalid"

# Assertion tests provided in the prompt
if __name__ == "__main__":
    assert check_char("abba") == "Valid"
    assert check_char("a") == "Valid"
    assert check_char("abcd") == "Invalid"