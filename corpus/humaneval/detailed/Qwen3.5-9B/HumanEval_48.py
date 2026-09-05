from typing import Optional


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
    # Step 1: Validate input type explicitly
    if not isinstance(text, str):
        raise TypeError(f"Expected input of type 'str', but got '{type(text).__name__}'")

    # Step 2: Normalize the input string to handle case sensitivity and whitespace
    # according to standard palindrome definitions (case-insensitive, ignoring non-alphanumeric).
    normalized_text: str = _normalize_string(text)

    # Step 3: Check for empty or single-character strings after normalization
    length: int = len(normalized_text)

    if length <= 1:
        return True

    # Step 4: Validate that the normalized string is not empty (should be covered by length check,
    # but explicit check for clarity)
    if length == 0:
        return True

    # Step 5: Use two-pointer technique to compare characters from both ends
    return _are_characters_mirror_sequence(normalized_text, length)


def _normalize_string(text: str) -> str:
    """
    Helper function to normalize the input string.
    - Converts to lowercase to make the check case-insensitive.
    - Removes all non-alphanumeric characters.

    Args:
        text: The original string input.

    Returns:
        A normalized string containing only lowercase alphanumeric characters.
    """
    normalized_chars: list[str] = []

    for character in text:
        if character.isalnum():
            normalized_chars.append(character.lower())

    return "".join(normalized_chars)


def _are_characters_mirror_sequence(sequence: str, length: int) -> bool:
    """
    Helper function to check if a sequence of characters is a palindrome.
    Uses an iterative two-pointer approach for efficiency and clarity.

    Args:
        sequence: The string sequence to check.
        length: The length of the sequence (passed for explicit control flow).

    Returns:
        True if the sequence is a palindrome, False otherwise.
    """
    # Initialize pointers
    left_index: int = 0
    right_index: int = length - 1

    # Iterate while left pointer is less than right pointer
    while left_index < right_index:
        left_char: str = sequence[left_index]
        right_char: str = sequence[right_index]

        # Explicit comparison
        if left_char != right_char:
            return False

        # Move pointers inward
        left_index += 1
        right_index -= 1

    # If loop completes without returning False, it is a palindrome
    return True