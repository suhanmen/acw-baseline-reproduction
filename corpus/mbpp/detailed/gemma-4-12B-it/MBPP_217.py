from typing import Optional

def first_Repeated_Char(input_string: str) -> str:
    """
    Finds the first character in a string that appears more than once.
    The 'first' is defined by the order of occurrence in the string: 
    as soon as a character is encountered that has been seen before, 
    that character is returned.

    If no characters are repeated, the function returns the null character '\0'.

    Args:
        input_string (str): The string to search for repeated characters.

    Returns:
        str: The first repeated character, or '\0' if no repetitions exist.

    Raises:
        TypeError: If the input_string is not a string.
    """
    # 1. Input Validation
    if not isinstance(input_string, str):
        raise TypeError(f"Expected input of type 'str', but received '{type(input_string).__name__}'.")

    # 2. Handle Empty Input Edge Case
    # An empty string has no characters, therefore no repeats.
    if len(input_string) == 0:
        return '\0'

    # 3. Data Structure Initialization
    # We use a set to store characters we have encountered while iterating.
    # Sets provide O(1) average time complexity for lookups.
    seen_characters = set()

    # 4. Iteration Logic
    # We iterate through the string character by character.
    # The first time we find a character already present in 'seen_characters',
    # that character is, by definition, the first repeated character.
    for current_char in input_string:
        # Check if the current character has been seen before
        is_already_seen = current_char in seen_characters

        if is_already_seen:
            # This is the first character we've encountered for a second time.
            return current_char

        # If it's the first time seeing this character, add it to our set.
        seen_characters.add(current_char)

    # 5. Final Fallback
    # If the loop completes without returning, no character was repeated.
    return '\0'

# The following assertions are provided to ensure compliance with problem requirements.
if __name__ == "__main__":
    # Test cases provided in the prompt
    assert first_Repeated_Char("Google") == "o"
    assert first_Repeated_Char("data") == "a"
    assert first_Repeated_Char("python") == '\0'

    # Additional edge cases
    assert first_Repeated_Char("") == '\0'           # Empty string
    assert first_Repeated_Char("abcde") == '\0'       # No repeats
    assert first_Repeated_Char("aaaaa") == "a"        # Immediate repeat
    assert first_Repeated_Char("abba") == "b"         # Non-adjacent repeat
    assert first_Repeated_Char("1122") == "1"         # Numbers as strings
    assert first_Repeated_Char("  ") == " "           # Whitespace