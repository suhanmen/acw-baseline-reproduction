from collections import Counter
from typing import List, Tuple, Union, Optional, Dict


def _validate_input_words(
    words: List[str],
    error_message: str = "Input must be a list of strings."
) -> None:
    """
    Validates that the input list contains only string elements.

    Parameters:
        words: The list to validate.
        error_message: A custom error message if validation fails.

    Raises:
        TypeError: If the input is not a list or if it contains non-string elements.
    """
    if not isinstance(words, list):
        raise TypeError(f"Expected a list, but got {type(words).__name__}. {error_message}")

    for index, word in enumerate(words):
        if not isinstance(word, str):
            raise TypeError(
                f"Element at index {index} is not a string. "
                f"Expected str, got {type(word).__name__}. {error_message}"
            )


def _build_word_frequency_map(words: List[str]) -> Dict[str, int]:
    """
    Builds a frequency map of words from the input list.

    Parameters:
        words: A list of string words.

    Returns:
        A dictionary where keys are words and values are their counts.
    """
    frequency_map: Dict[str, int] = {}

    for word in words:
        current_count = frequency_map.get(word, 0)
        frequency_map[word] = current_count + 1

    return frequency_map


def _extract_common_words(
    frequency_map: Dict[str, int],
    threshold: int
) -> List[Tuple[str, int]]:
    """
    Extracts all words that have a count greater than or equal to the threshold.
    This helper is used to handle cases where the top N or all words above a count are needed.

    Parameters:
        frequency_map: The dictionary of word counts.
        threshold: The minimum count required for a word to be included.

    Returns:
        A list of tuples (word, count) for words meeting the threshold.
    """
    common_words: List[Tuple[str, int]] = []

    for word, count in frequency_map.items():
        if count >= threshold:
            common_words.append((word, count))

    return common_words


def _sort_words_alphabetically(word_count_list: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
    Sorts a list of (word, count) tuples alphabetically by word.

    This ensures a deterministic output order when counts are equal or 
    when sorting is required for consistency.

    Parameters:
        word_count_list: A list of (word, count) tuples.

    Returns:
        A new list of tuples sorted by the word in ascending alphabetical order.
    """
    return sorted(word_count_list, key=lambda item: item[0])


def count_common(words: List[str]) -> List[Tuple[str, int]]:
    """
    Counts the most common words in a list and returns them sorted alphabetically.

    The function calculates the frequency of each word in the input list.
    It then identifies the maximum frequency among all words.
    Finally, it returns a list of all words that have this maximum frequency,
    sorted alphabetically.

    Behavior for edge cases:
    - Empty list: Returns an empty list.
    - Single element: Returns the word with its count.
    - All elements equal: Returns the single word with its total count.
    - Invalid input (non-list or non-strings): Raises a TypeError.

    Parameters:
        words: A list of string words to analyze.

    Returns:
        A list of tuples containing the word and its count.
        The list is sorted alphabetically by the word.

    Raises:
        TypeError: If the input is not a list or contains non-string elements.
    """
    # Step 1: Validate the input structure and contents
    _validate_input_words(words)

    # Handle the empty input case explicitly before processing
    if not words:
        return []

    # Step 2: Calculate the frequency of each word
    frequency_map = _build_word_frequency_map(words)

    # Step 3: Determine the maximum frequency (count) present in the map
    max_frequency = 0
    for count in frequency_map.values():
        if count > max_frequency:
            max_frequency = count

    # Step 4: Identify all words that match the maximum frequency
    most_common_words = _extract_common_words(frequency_map, max_frequency)

    # Step 5: Sort the result alphabetically by word to ensure deterministic order
    sorted_result = _sort_words_alphabetically(most_common_words)

    return sorted_result