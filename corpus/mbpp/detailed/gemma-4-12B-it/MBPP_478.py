from typing import List

def remove_lowercase_substrings(input_string: str) -> str:
    """
    Removes all lowercase substrings (characters) from a given string.

    Args:
        input_string (str): The string to process.

    Returns:
        str: A new string containing only non-lowercase characters.

    Raises:
        TypeError: If the input is not a string.
    """
    # Defensive Programming: Validate input type
    if not isinstance(input_string, str):
        raise TypeError(f"Input must be a string, but received {type(input_string).__name__}")

    # Handle edge case: empty string
    if input_string == "":
        return ""

    # List to collect valid characters
    # We use a list for efficient concatenation
    result_chars: List[str] = []

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is lowercase.
        # islower() returns True only if the character is lowercase and 
        # is not a symbol or digit (e.g., '1' or '!' return False).
        is_lowercase = char.islower()

        if not is_lowercase:
            # If the character is NOT lowercase, we keep it.
            # This includes uppercase letters, digits, and punctuation.
            result_chars.append(char)

    # Join the list of characters into the final result string
    final_result = "".join(result_chars)

    return final_result

def remove_lowercase(input_string: str) -> str:
    """
    Wrapper function to satisfy the required signature and assertions.
    """
    # Defensive check for None
    if input_string is None:
        return ""

    # Call the core logic
    return remove_lowercase_substrings(input_string)

# The assertions provided in the problem description
if __name__ == "__main__":
    # These tests verify the logic against the required specifications.
    assert remove_lowercase("PYTHon") == 'PYTH'
    assert remove_lowercase("FInD") == 'FID'
    assert remove_lowercase("STRinG") == 'STRG'