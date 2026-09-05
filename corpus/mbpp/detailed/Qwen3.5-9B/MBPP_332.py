from collections import defaultdict
from typing import Dict


def char_frequency(input_string: str) -> Dict[str, int]:
    """
    Counts the frequency of each character in the given string.

    This function performs robust character counting with explicit validation
    and edge case handling. It returns a dictionary where keys are characters
    and values are their occurrence counts.

    Args:
        input_string (str): The string to analyze. Must be a valid string.

    Returns:
        Dict[str, int]: A dictionary mapping each unique character to its count.

    Raises:
        TypeError: If the input is not a string instance.
    """
    # Step 1: Validate Input Type
    if not isinstance(input_string, str):
        raise TypeError(f"Input must be a string, got {type(input_string).__name__}")

    # Step 2: Handle Edge Case - Empty String
    # An empty string has no characters, so the result should be an empty dictionary.
    if len(input_string) == 0:
        return {}

    # Step 3: Initialize a dictionary to store counts.
    # We use a defaultdict with an int factory for convenience, but we could 
    # also use a standard dict with explicit .setdefault() or .get().
    # Here we use a standard dict to make the increment logic fully explicit.
    frequency_map: Dict[str, int] = {}

    # Step 4: Iterate through each character in the string explicitly.
    # We do not use comprehensions or one-liners to ensure clarity.
    for character in input_string:
        # Check if the character is already in our map
        if character in frequency_map:
            # Increment the existing count
            current_count = frequency_map[character]
            frequency_map[character] = current_count + 1
        else:
            # This is a new character found; initialize its count to 1
            frequency_map[character] = 1

    # Step 5: Return the populated frequency map
    return frequency_map