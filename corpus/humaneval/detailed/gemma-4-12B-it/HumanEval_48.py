from typing import Any

def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Defensive Programming: Validate that the input is actually a string.
    # While type hinting suggests str, runtime checks ensure production stability.
    if not isinstance(text, str):
        raise TypeError(f"Input must be a string, but received {type(text).__name__}")

    # Handle edge case: Empty string.
    # By definition, an empty string is a palindrome as it reads the same forwards and backwards.
    if len(text) == 0:
        return True

    # Handle edge case: Single character.
    # A single character is always a palindrome.
    if len(text) == 1:
        return True

    def get_character_at_index(input_str: str, index: int) -> str:
        """Helper to retrieve a character at a specific index."""
        return input_str[index]

    # We use a two-pointer approach to compare characters from both ends.
    # This is O(n) time complexity and O(1) space complexity (ignoring the input string).
    left_index: int = 0
    right_index: int = len(text) - 1

    while left_index < right_index:
        # Retrieve characters from both ends
        left_char: str = get_character_at_index(text, left_index)
        right_char: str = get_character_at_index(text, right_index)

        # Check if the characters at these positions match
        if left_char != right_char:
            # If any mismatch is found, it is not a palindrome
            return False

        # Move the pointers towards the center
        left_index += 1
        right_index -= 1

    # If the loop completes without returning False, the string is a palindrome.
    return True