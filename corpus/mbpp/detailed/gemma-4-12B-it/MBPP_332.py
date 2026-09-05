from typing import Dict

def char_frequency(input_string: str) -> Dict[str, int]:
    """
    Counts the frequency of each character in a given string.

    Args:
        input_string (str): The string to analyze.

    Returns:
        Dict[str, int]: A dictionary where keys are characters and 
                         values are their respective counts.

    Raises:
        TypeError: If the input_string is not a string.
    """
    # Step 1: Validate Input Type
    # We ensure the input is specifically a string to prevent 
    # attribute errors or unexpected behavior with other iterables.
    if not isinstance(input_string, str):
        raise TypeError(f"Input must be a string, but received {type(input_string).__name__}")

    # Step 2: Handle the empty string case
    # If the string is empty, the frequency dictionary should be empty.
    if len(input_string) == 0:
        return {}

    # Step 3: Initialize the frequency dictionary
    # Using a standard dictionary to store counts.
    frequency_map: Dict[str, int] = {}

    # Step 4: Iterate through the string
    # We process the string character by character to build the map.
    for char in input_string:
        # Check if the character is already present in the dictionary
        if char in frequency_map:
            # Increment the existing count
            current_count = frequency_map[char]
            new_count = current_count + 1
            frequency_map[char] = new_count
        else:
            # If the character is new, initialize it with a count of 1
            # This handles the first occurrence of any unique character.
            frequency_map[char] = 1

    # Step 5: Return the final mapping
    return frequency_map

if __name__ == "__main__":
    # Test cases provided in the problem description
    assert char_frequency('python') == {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
    assert char_frequency('program') == {'p': 1, 'r': 2, 'o': 1, 'g': 1, 'a': 1, 'm': 1}
    assert char_frequency('language') == {'l': 1, 'a': 2, 'n': 1, 'g': 2, 'u': 1, 'e': 1}

    # Edge cases
    assert char_frequency('') == {}
    assert char_frequency('aaaaa') == {'a': 5}
    assert char_frequency(' ') == {' ': 1}
    assert char_frequency('A a') == {'A': 1, ' ': 1, 'a': 1}