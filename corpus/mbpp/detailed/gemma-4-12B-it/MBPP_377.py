from typing import Any

def remove_Char(input_string: str, char_to_remove: str) -> str:
    """
    Removes all occurrences of a specific character from a given string.

    Args:
        input_string (str): The source string to process.
        char_to_remove (str): The character to be deleted from the source string.

    Returns:
        str: A new string with all instances of char_to_remove removed.

    Raises:
        TypeError: If input_string or char_to_remove are not strings.
        ValueError: If char_to_remove is an empty string or contains more than one character.
    """
    # --- Input Validation ---

    # Check if input_string is a string
    if not isinstance(input_string, str):
        raise TypeError(f"Expected input_string to be str, got {type(input_string).__name__}")

    # Check if char_to_remove is a string
    if not isinstance(char_to_remove, str):
        raise TypeError(f"Expected char_to_remove to be str, got {type(char_to_remove).__name__}")

    # The problem implies a single character removal. 
    # If the input is empty or multiple characters, it is technically an invalid target for "a character".
    if len(char_to_remove) == 0:
        raise ValueError("char_to_remove cannot be an empty string.")

    if len(char_to_remove) > 1:
        raise ValueError("char_to_remove must be exactly one character.")

    # --- Edge Case Handling ---

    # If the input string is empty, the result is always an empty string.
    if not input_string:
        return ""

    # If the character to remove is not in the string, return the string as is.
    if char_to_remove not in input_string:
        return input_string

    # --- Core Logic ---

    # We iterate through the string and build a new list of characters.
    # Using a list and joining is O(n) and more memory efficient than string concatenation.
    result_chars = []

    for current_char in input_string:
        # Check if the current character matches the character we want to filter out.
        is_match = (current_char == char_to_remove)

        # If it's NOT a match, we keep it.
        if not is_match:
            result_chars.append(current_char)

    # Join the list into a final result string.
    final_result = "".join(result_chars)

    return final_result

if __name__ == "__main__":
    # Test cases provided in the problem description
    assert remove_Char("aba", 'a') == "b"
    assert remove_Char("toggle", 'g') == "tole"
    assert remove_Char("aabbc", 'b') == "aac"

    # Additional edge cases
    assert remove_Char("", "a") == ""              # Empty input
    assert remove_Char("aaaaa", "a") == ""        # All equal elements
    assert remove_Char("abcde", "z") == "abcde"   # Char not present
    assert remove_Char("12345", "1") == "2345"    # Numbers as strings
    assert remove_Char("   ", " ") == ""           # Whitespace