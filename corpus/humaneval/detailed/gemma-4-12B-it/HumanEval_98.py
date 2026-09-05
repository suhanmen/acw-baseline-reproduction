from typing import Any

def is_uppercase_vowel(char: str) -> bool:
    """
    Helper function to check if a single character is an uppercase vowel.

    Args:
        char: The character to check.

    Returns:
        True if the character is 'A', 'E', 'I', 'O', or 'U', False otherwise.
    """
    # Define the set of characters that qualify as uppercase vowels
    uppercase_vowels = {'A', 'E', 'I', 'O', 'U'}

    # Check if the character is in our defined set
    is_vowel = char in uppercase_vowels
    return is_vowel

def count_upper(s: Any) -> int:
    """
    Given a string s, count the number of uppercase vowels in even indices.

    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Input Validation: Ensure the input is a string.
    # While the problem assumes a string, production-grade code should be defensive.
    if not isinstance(s, str):
        # In a production environment, we might raise a TypeError.
        # Given the prompt, we ensure we handle the logic correctly for strings.
        raise TypeError(f"Expected input type 'str', but received '{type(s).__name__}'")

    # Edge Case: Empty string.
    # The loop will not execute, and it will return 0 correctly.
    if len(s) == 0:
        return 0

    count = 0

    # We iterate through the string using indices.
    # We want to check even indices (0, 2, 4, ...).
    # Using a step of 2 in the range function is efficient and explicit.
    # Start at 0, end at the length of s, increment by 2.
    for index in range(0, len(s), 2):
        # Retrieve the character at the current even index.
        current_char = s[index]

        # Check if the character at this specific index is an uppercase vowel.
        # We use the helper function to isolate this specific logic.
        if is_uppercase_vowel(current_char):
            # If it is an uppercase vowel, increment the accumulator.
            count += 1

    # Return the total accumulated count.
    return count