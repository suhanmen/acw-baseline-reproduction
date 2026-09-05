from __future__ import annotations

from typing import Any

def _is_valid_input(text: Any) -> bool:
    """
    Validate that the input is a string.

    Returns:
        True if the input is a string, False otherwise.
    """
    if text is None:
        return False
    if not isinstance(text, str):
        return False
    return True

def _contains_z(word: str) -> bool:
    """
    Check if a specific word (a continuous sequence of non-space characters)
    contains the character 'z' (case-insensitive).

    Args:
        word: The word to check.

    Returns:
        True if the word contains 'z' or 'Z', False otherwise.
    """
    if not word:
        return False

    word_lower = word.lower()

    for char in word_lower:
        if char == 'z':
            return True

    return False

def _extract_words(text: str) -> list[str]:
    """
    Extract all words from the input text.
    A word is defined as a continuous sequence of non-whitespace characters.

    Args:
        text: The input text string.

    Returns:
        A list of strings, where each string is a word found in the text.
    """
    words_list: list[str] = []

    current_word_buffer: str = ""

    for char in text:
        if char.isspace():
            if current_word_buffer:
                words_list.append(current_word_buffer)
                current_word_buffer = ""
        else:
            current_word_buffer += char

    if current_word_buffer:
        words_list.append(current_word_buffer)

    return words_list

def text_match_wordz(text: Any) -> str:
    """
    Matches a word containing 'z' in the given text.

    The function searches for any sequence of non-whitespace characters (a "word")
    within the input text. If any of these words contains the letter 'z' (case-insensitive),
    it returns "Found a match!". Otherwise, it returns "Not matched!".

    Edge cases handled:
        - Empty input string: Returns "Not matched!".
        - Single element (e.g., "a"): Returns "Not matched!".
        - All-equal elements (e.g., "zzz"): Returns "Found a match!".
        - Zero / negative numbers (as strings): Handled correctly if the string representation contains 'z', 
          otherwise returns "Not matched!". Note: The function operates on strings, so numeric types 
          must be passed as strings to be valid.
        - Whitespace only: Returns "Not matched!".
        - Invalid input types: Returns an error message or handles gracefully based on validation.

    Args:
        text: The input text to search within. Must be a string.

    Returns:
        A string: "Found a match!" if a word containing 'z' is found, "Not matched!" otherwise.
        For invalid inputs, it returns an error message indicating the issue.
    """
    # Validate input type explicitly
    if not _is_valid_input(text):
        return "Invalid input: text must be a string."

    # Handle empty string edge case explicitly
    if len(text) == 0:
        return "Not matched!"

    # Extract words from the text
    words = _extract_words(text)

    # Check if any word contains 'z'
    for word in words:
        if _contains_z(word):
            return "Found a match!"

    return "Not matched!"