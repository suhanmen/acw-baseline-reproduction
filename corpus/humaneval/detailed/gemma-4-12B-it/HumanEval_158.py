from typing import List

def find_max(words: List[str]) -> str:
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    # --- Input Validation ---
    # Check if input is actually a list
    if not isinstance(words, list):
        raise TypeError(f"Input must be a list of strings, but got {type(words).__name__}")

    # Handle the empty list case
    if len(words) == 0:
        return ""

    # Ensure all elements in the list are strings
    for item in words:
        if not isinstance(item, str):
            raise TypeError(f"All elements in the list must be strings. Found: {type(item).__name__}")

    # --- Core Logic ---
    # We need to track the "best" word found so far.
    # We initialize these variables to handle the first iteration properly.
    best_word: str = ""
    max_unique_count: int = -1

    for current_word in words:
        # Calculate the number of unique characters in the current word.
        # Using a set is the standard, efficient way to count unique items.
        unique_chars = set(current_word)
        current_unique_count = len(unique_chars)

        # Logic for determining the "winner":
        # 1. If the current word has strictly more unique characters than our record.
        # 2. If the current word has the SAME number of unique characters,
        #    we must choose the one that is lexicographically smaller.

        is_better_count = current_unique_count > max_unique_count

        is_same_count_and_lexicographically_smaller = (
            current_unique_count == max_unique_count and 
            current_word < best_word
        )

        # Special case for the first word processed: 
        # since max_unique_count starts at -1, the first word will always win.
        if best_word == "" or is_better_count or is_same_count_and_lexicographically_smaller:
            # Update our trackers
            max_unique_count = current_unique_count
            best_word = current_word

    return best_word