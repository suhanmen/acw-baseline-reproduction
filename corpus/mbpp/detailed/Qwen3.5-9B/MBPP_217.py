# Type hints for clarity and type safety
from typing import Optional


def _find_first_repeated_index_char(char_list: list) -> tuple[Optional[int], Optional[str]]:
    """
    Helper function to find the index and character of the first repeated element.

    Args:
    char_list: A list of characters.

    Returns:
    A tuple containing the index of the first repeated character and the character itself.
    If no repetition is found, returns (-1, None).
    """
    seen_characters: set[str] = set()

    # Iterate through each character in the list
    for current_index in range(len(char_list)):
        current_char: str = char_list[current_index]

        # Check if the character is already in the set of seen characters
        if current_char in seen_characters:
            # Return the index and the character immediately upon finding a repeat
            return current_index, current_char

        # Add the character to the set if it hasn't been seen before
        seen_characters.add(current_char)

    # If we finish the loop without finding a repeat, return sentinel values
    return -1, None


def first_Repeated_Char(input_string: str) -> str:
    """
    Finds the first repeated character in the given string.

    This function iterates through the string, keeping track of characters encountered so far.
    If a character is encountered that has already been seen, it is returned immediately 
    as the first repeated character.

    If no characters are repeated, the function returns a null character '\0'.

    Args:
    input_string (str): The string to search for repeated characters.

    Returns:
    str: The first repeated character if found, otherwise '\0'.

    Raises:
    TypeError: If the input is not a string.
    """

    # Explicit input validation: Check if the input is of the expected type
    if not isinstance(input_string, str):
        raise TypeError(f"Input must be a string, received {type(input_string).__name__}")

    # Edge case: Handle empty string explicitly
    if len(input_string) == 0:
        return '\0'

    # Convert the string into a list of characters to ensure we are iterating over unicode scalars
    # strictly (though iterating over the string directly also yields characters in Python 3)
    # We use the list explicitly here to separate the data structure from the logic as per requirements.
    char_list: list[str] = list(input_string)

    # Call the helper function to find the index and the character
    repeated_index: Optional[int] = -1
    repeated_char: Optional[str] = None

    repeated_index, repeated_char = _find_first_repeated_index_char(char_list)

    # Handle the case where no repetition was found
    if repeated_index == -1:
        return '\0'

    # Validate that the character retrieved is not None (defensive programming)
    if repeated_char is None:
        return '\0'

    # Ensure the character is a valid ASCII string of length 1, as implied by the problem context
    # Although the input is a string, this ensures we are dealing with a single character value.
    if not isinstance(repeated_char, str) or len(repeated_char) != 1:
        return '\0'

    return repeated_char