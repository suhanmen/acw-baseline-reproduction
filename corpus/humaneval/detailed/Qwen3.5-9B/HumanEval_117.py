import re
from typing import List, Set

# Define a set of all consonants (both lowercase and uppercase)
CONSONANTS: Set[str] = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')

def _is_consonant(char: str) -> bool:
    """
    Determines if a single character is a consonant.

    Args:
        char: A single character string.

    Returns:
        True if the character is a consonant, False otherwise.
    """
    return char in CONSONANTS

def _count_consonants(word: str) -> int:
    """
    Counts the number of consonants in a given word.

    Args:
        word: A string representing the word.

    Returns:
        An integer representing the count of consonants in the word.
    """
    count = 0
    for char in word:
        if _is_consonant(char):
            count += 1
    return count

def _is_valid_n(n: int) -> bool:
    """
    Validates if the integer n is a natural number (0, 1, 2, ...).

    Args:
        n: The integer to validate.

    Returns:
        True if n is a natural number, False otherwise.
    """
    return isinstance(n, int) and n >= 0

def _split_into_words(s: str) -> List[str]:
    """
    Splits the input string into words based on whitespace.

    Args:
        s: The input string.

    Returns:
        A list of words extracted from the string.
    """
    # Split by whitespace and filter out empty strings that might result from multiple spaces
    words = s.split()
    return words

def select_words(s: str, n: int) -> List[str]:
    """
    Given a string s and a natural number n, returns a list of all words 
    from string s that contain exactly n consonants, in the order they appear.

    Args:
        s: Input string containing words separated by spaces.
        n: Natural number representing the exact count of consonants required.

    Returns:
        A list of words from s that have exactly n consonants.

    Raises:
        TypeError: If s is not a string or n is not an integer.
        ValueError: If n is negative.
    """
    # Step 1: Validate input types
    if not isinstance(s, str):
        raise TypeError(f"Expected 's' to be a string, got {type(s).__name__}")
    if not isinstance(n, int):
        raise TypeError(f"Expected 'n' to be an integer, got {type(n).__name__}")

    # Step 2: Validate n value (must be non-negative natural number)
    if n < 0:
        raise ValueError(f"Expected 'n' to be a non-negative integer, got {n}")

    # Step 3: Handle empty string case explicitly
    if not s:
        return []

    # Step 4: Split the string into words
    words = _split_into_words(s)

    # Step 5: Filter words based on consonant count
    result: List[str] = []

    for word in words:
        # Count consonants in the current word
        consonant_count = _count_consonants(word)

        # Check if the count matches the required number n
        if consonant_count == n:
            result.append(word)

    return result