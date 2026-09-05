from collections import Counter
from typing import Dict, List, Tuple, Union, NoReturn

def _validate_input(test: str) -> NoReturn:
    """
    Validates that the input is a string.
    Raises a TypeError if the input is not a string.
    This function will never return normally; it only raises exceptions.
    """
    if not isinstance(test, str):
        raise TypeError(
            f"Input must be a string, but received: {type(test).__name__}"
        )

def _parse_letters(test: str) -> List[str]:
    """
    Parses the input string into a list of individual lowercase letters.

    The expected format is space-separated lowercase letters (e.g., 'a b c').
    Non-alphabetic characters (other than spaces) will be filtered out or treated
    as invalid depending on strictness. Here, we strictly expect lowercase letters.

    Returns:
        A list of single-character strings representing the valid letters found.

    Raises:
        ValueError: If non-letter characters are found in the input.
    """
    if not test:
        return []

    parsed_letters: List[str] = []
    characters = test.split(' ')

    for char in characters:
        if not char:
            # Skip empty strings resulting from consecutive spaces or leading/trailing spaces
            continue

        # Ensure the character is a lowercase letter
        if 'a' <= char <= 'z':
            parsed_letters.append(char)
        else:
            raise ValueError(
                f"Invalid character found in input: '{char}'. "
                "Only space-separated lowercase letters (a-z) are allowed."
            )

    return parsed_letters

def _calculate_frequencies(parsed_letters: List[str]) -> Dict[str, int]:
    """
    Calculates the frequency of each letter in the parsed list.

    Args:
        parsed_letters: List of single-character strings.

    Returns:
        A dictionary mapping each letter to its count.
    """
    if not parsed_letters:
        return {}

    frequency_map: Dict[str, int] = {}
    for letter in parsed_letters:
        current_count = frequency_map.get(letter, 0)
        frequency_map[letter] = current_count + 1

    return frequency_map

def _find_max_count(frequency_map: Dict[str, int]) -> int:
    """
    Determines the highest frequency value in the frequency map.

    Args:
        frequency_map: Dictionary mapping letters to their counts.

    Returns:
        The integer representing the maximum count.
        Returns 0 if the map is empty.
    """
    if not frequency_map:
        return 0

    max_count = 0
    for count in frequency_map.values():
        if count > max_count:
            max_count = count

    return max_count

def _get_max_occurrence_letters(
    frequency_map: Dict[str, int], 
    max_count: int
) -> List[str]:
    """
    Identifies all letters that have the maximum occurrence count.

    Args:
        frequency_map: Dictionary mapping letters to their counts.
        max_count: The known maximum count value.

    Returns:
        A sorted list of letters that appear with the maximum count.
    """
    result: List[str] = []
    for letter in frequency_map:
        if frequency_map[letter] == max_count:
            result.append(letter)

    # Sort the result to ensure deterministic output order
    result.sort()
    return result

def _build_result_letters(
    letters: List[str], 
    frequencies: Dict[str, int],
    target_count: int
) -> Dict[str, int]:
    """
    Constructs the final result dictionary containing only letters
    that match the target occurrence count.

    Args:
        letters: The list of unique letters present in the input (or all letters if empty input handling).
        frequencies: The full frequency map.
        target_count: The count to filter for.

    Returns:
        A dictionary of letters and their counts, restricted to those matching target_count.
    """
    final_result: Dict[str, int] = {}
    for letter in letters:
        if frequencies.get(letter, 0) == target_count:
            final_result[letter] = target_count

    return final_result

def histogram(test: str) -> Dict[str, int]:
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.

    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    # Step 1: Validate the input type
    _validate_input(test)

    # Step 2: Parse the string into a list of valid letters
    parsed_letters: List[str] = _parse_letters(test)

    # Step 3: Handle the empty input case explicitly
    if not parsed_letters:
        return {}

    # Step 4: Calculate the frequency of each letter
    frequencies: Dict[str, int] = _calculate_frequencies(parsed_letters)

    # Step 5: Find the maximum occurrence count
    max_count: int = _find_max_count(frequencies)

    # Step 6: Identify which letters have this maximum count
    # Since 'parsed_letters' might contain duplicates but we want unique keys for the result,
    # we can use the keys of the frequencies map or iterate through sorted unique letters.
    max_occurrence_letters: List[str] = _get_max_occurrence_letters(frequencies, max_count)

    # Step 7: Build the final result dictionary
    # We pass the unique letters found in frequencies to ensure the result is clean
    result_letters: List[str] = sorted(frequencies.keys())

    final_result: Dict[str, int] = _build_result_letters(result_letters, frequencies, max_count)

    return final_result