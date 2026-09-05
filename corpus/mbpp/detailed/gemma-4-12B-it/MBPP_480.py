from typing import Dict

def get_max_occuring_char(input_string: str) -> str:
    """
    Finds the character that appears most frequently in the given string.

    In the case of a tie between two or more characters with the same 
    maximum frequency, the character that appears first in the string 
    is returned.

    Args:
        input_string (str): The input string to analyze.

    Returns:
        str: The most frequently occurring character.

    Raises:
        ValueError: If the input string is empty or not a string.
    """
    # Validate input type
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string.")

    # Handle empty string case
    if len(input_string) == 0:
        raise ValueError("Input string cannot be empty.")

    # Step 1: Count the frequency of every character in the string.
    # We use a dictionary where keys are characters and values are counts.
    char_frequency_map: Dict[str, int] = {}

    for char in input_string:
        if char in char_frequency_map:
            char_frequency_map[char] = char_frequency_map[char] + 1
        else:
            char_frequency_map[char] = 1

    # Step 2: Identify the maximum frequency achieved by any character.
    max_frequency: int = 0
    for count in char_frequency_map.values():
        if count > max_frequency:
            max_frequency = count

    # Step 3: Find the first character in the original string that 
    # matches the max_frequency. This ensures stable behavior 
    # for ties (returning the one that appeared earliest).
    most_frequent_char: str = ""

    # We iterate through the string again to maintain order 
    # and handle the 'first occurrence' rule correctly.
    for char in input_string:
        current_count = char_frequency_map.get(char)

        if current_count == max_frequency:
            # Since we are iterating from left to right, the first 
            # character we encounter that has the max_frequency is our result.
            most_frequent_char = char
            break

    return most_frequent_char

if __name__ == "__main__":
    # The assertions provided in the prompt
    assert get_max_occuring_char("data") == "a"
    assert get_max_occuring_char("create") == "e"
    assert get_max_occuring_char("brilliant girl") == "i"