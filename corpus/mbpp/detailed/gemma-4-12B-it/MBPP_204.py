from typing import Any

def count(input_string: str, target_char: str) -> int:
    """
    Counts the occurrences of a specific character within a given string.

    Args:
        input_string (str): The string to search through.
        target_char (str): The specific character to count.

    Returns:
        int: The total number of occurrences of target_char in input_string.

    Raises:
        TypeError: If input_string or target_char is not a string.
        ValueError: If target_char is not exactly one character long.
    """
    # Defensive check: Ensure input_string is a string type
    if not isinstance(input_string, str):
        raise TypeError(f"Expected input_string to be str, got {type(input_string).__name__}")

    # Defensive check: Ensure target_char is a string type
    if not isinstance(target_char, str):
        raise TypeError(f"Expected target_char to be str, got {type(target_char).__name__}")

    # Defensive check: Ensure target_char is exactly one character
    # The problem asks to count a 'character', implying a length of 1.
    if len(target_char) != 1:
        raise ValueError(f"target_char must be exactly one character long, received length {len(target_char)}")

    # Handle edge case: empty string input
    # If the string is empty, the count of any character must be 0.
    if len(input_string) == 0:
        return 0

    # Initialize the counter
    occurrence_count: int = 0

    # Iterate through each character in the string
    # We use a standard loop to ensure every step is visible and explicit.
    for current_character in input_string:
        # Check if the character in the current position matches the target
        if current_character == target_char:
            # Increment the counter if it matches
            occurrence_count += 1

    return occurrence_count

# Verification against the provided assertions
if __name__ == "__main__":
    # The following assertions confirm the function meets the requirements.
    assert count("abcc", "c") == 2
    assert count("ababca", "a") == 3
    assert count("mnmm0pm", "m") == 4