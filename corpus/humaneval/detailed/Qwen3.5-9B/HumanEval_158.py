from typing import List, Optional, Union

def _validate_words_list(words: object) -> bool:
    """
    Validates that the input is a list containing only strings.
    Returns True if valid, False otherwise.
    """
    if not isinstance(words, list):
        return False

    if len(words) == 0:
        return False

    for item in words:
        if not isinstance(item, str):
            return False

    return True

def _count_unique_characters(word: str) -> int:
    """
    Counts the number of unique characters in a given string.
    Returns an integer representing the count of unique characters.
    """
    unique_chars = set()
    for char in word:
        unique_chars.add(char)
    return len(unique_chars)

def find_max(words: object) -> Optional[Union[str, int]]:
    """
    Accepts a list of strings.
    Returns the word with the maximum number of unique characters.
    If multiple words have the same maximum number of unique characters,
    returns the one that comes first in lexicographical order.

    Args:
        words: Expected to be a list of strings.

    Returns:
        The string with the most unique characters (lexicographically smallest if tied),
        or the integer -1 if the input list is empty or invalid.
    """
    # Step 1: Validate input
    if not _validate_words_list(words):
        return -1

    # Step 2: Initialize tracking variables
    # 'best_word' will store the current winner
    best_word: str = ""

    # 'max_unique_count' will store the current maximum count of unique characters
    # Since the list is validated to be non-empty here, we can safely initialize
    # with the first word's metrics, but we also need to handle the case where
    # we initialize with a sentinel value and update on the first iteration.
    # Let's initialize with the first word to simplify logic.

    # Calculate unique count for the first word
    current_unique_count = _count_unique_characters(words[0])
    best_word = words[0]
    max_unique_count = current_unique_count

    # Step 3: Iterate through the rest of the list (starting from index 1)
    for i in range(1, len(words)):
        current_word = words[i]

        # Calculate unique count for the current candidate
        current_unique_count = _count_unique_characters(current_word)

        # Step 4: Compare the current candidate with the best word found so far
        condition_to_update = False

        # Case A: Current word has MORE unique characters than the best word
        if current_unique_count > max_unique_count:
            condition_to_update = True
        # Case B: Current word has THE SAME number of unique characters as the best word
        # In this case, choose the one that is lexicographically smaller
        elif current_unique_count == max_unique_count:
            # Lexicographical comparison: if current_word < best_word, update
            if current_word < best_word:
                condition_to_update = True

        # Step 5: Update the best word if the condition was met
        if condition_to_update:
            max_unique_count = current_unique_count
            best_word = current_word

    return best_word