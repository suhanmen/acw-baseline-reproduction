from typing import List, Union

def _is_even_length(word: str) -> bool:
    """
    Helper function to check if a word has an even length.

    Args:
        word: The string to check.

    Returns:
        True if the length of the word is even, False otherwise.
    """
    return len(word) % 2 == 0

def _get_even_words(words: List[str]) -> List[str]:
    """
    Helper function to filter a list of words, keeping only those with even lengths.

    Args:
        words: A list of strings to filter.

    Returns:
        A new list containing only the strings that have an even length.
    """
    result: List[str] = []
    for item in words:
        # Explicit check: ensure we are processing a string
        if isinstance(item, str):
            if _is_even_length(item):
                result.append(item)
    return result

def _compare_words_by_length(word_a: str, word_b: str, target_word: str) -> None:
    """
    Helper function to update the target_word if word_a is longer.

    This function serves to make the comparison logic explicit and verbose,
    breaking down the decision-making process into separate statements.

    Args:
        word_a: The candidate word being compared.
        word_b: The current best word (target).
        target_word: An output reference to store the current best word.
    """
    length_a = len(word_a)
    length_b = len(word_b)

    # Explicitly handle the case where the candidate is longer than the current best
    if length_a > length_b:
        target_word = word_a

def find_Max_Len_Even(input_string: str) -> Union[str, int]:
    """
    Finds the first maximum length of an even word in the input string.

    The function splits the input string by spaces to get individual words.
    It filters these words to keep only those with even lengths.
    Among the even-length words, it identifies the one with the maximum length.
    If multiple words share the maximum length, it returns the first one encountered.
    If no words with even lengths are found, it returns -1.

    Args:
        input_string: The input string containing words separated by spaces.

    Returns:
        The word with the maximum length among those with even lengths.
        If no such word exists, returns the integer -1.
    """

    # Step 1: Validate input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    # Step 2: Split the input string into a list of words
    # Using split() without arguments handles multiple spaces and leading/trailing spaces gracefully
    raw_words = input_string.split()

    # Step 3: Handle the empty input case explicitly
    if len(raw_words) == 0:
        return -1

    # Step 4: Filter words to keep only those with even lengths
    even_length_candidates = _get_even_words(raw_words)

    # Step 5: Handle the case where no words have even lengths
    if len(even_length_candidates) == 0:
        return -1

    # Step 6: Initialize the best word tracker
    # Start with the first candidate as the initial maximum
    best_word = even_length_candidates[0]

    # Step 7: Iterate through the remaining candidates to find the maximum length
    # We start from index 1 to skip the first one which is already set as 'best_word'
    for index in range(1, len(even_length_candidates)):
        current_candidate = even_length_candidates[index]

        # Explicitly call the helper to compare and update if necessary
        _compare_words_by_length(current_candidate, best_word, best_word)

    # Step 8: Return the final result
    return best_word