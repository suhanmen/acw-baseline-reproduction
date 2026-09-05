from typing import Any

def unique_Characters(input_string: str) -> bool:
    """
    Checks whether all the characters in a given string are unique.

    A character is considered unique if it appears exactly once in the 
    provided string. If any character repeats, the function returns False.

    Args:
        input_string (str): The string to be checked for unique characters.

    Returns:
        bool: True if all characters are unique, False otherwise.

    Raises:
        TypeError: If the input provided is not a string.
    """
    # Input Validation: Ensure the input is actually a string.
    if not isinstance(input_string, str):
        raise TypeError(f"Expected input of type 'str', but received '{type(input_string).__name__}'.")

    # Edge Case: An empty string technically has no repeating characters.
    # In most set theory contexts, an empty set has unique elements.
    if len(input_string) == 0:
        return True

    # Edge Case: A string with a single character always has unique characters.
    if len(input_string) == 1:
        return True

    # Logic: Use a set to keep track of characters we have encountered so far.
    # Sets in Python provide O(1) average time complexity for lookups and insertions.
    seen_characters = set()

    # Iterate through each character in the input string.
    for index, current_char in enumerate(input_string):
        # Check if the current character has already been added to our set.
        is_already_seen = current_char in seen_characters

        if is_already_seen:
            # If we find a character that is already in the set, 
            # it means the string contains duplicates.
            return False

        # If it is a new character, add it to the set.
        seen_characters.add(current_char)

    # If the loop completes without returning False, all characters are unique.
    return True

# Assertions to verify correctness
if __name__ == "__main__":
    # Test case 1: Duplicate characters
    assert unique_Characters('aba') == False

    # Test case 2: All unique characters
    assert unique_Characters('abc') == True

    # Test case 3: Multiple duplicate characters
    assert unique_Characters('abab') == False

    # Additional test cases for robustness
    assert unique_Characters('') == True          # Empty string
    assert unique_Characters('a') == True         # Single char
    assert unique_Characters('aaaaa') == False    # All same
    assert unique_Characters('Aa') == True        # Case sensitivity check
    assert unique_Characters('12345') == True     # Numbers as strings
    assert unique_Characters('!@#$%') == True     # Symbols