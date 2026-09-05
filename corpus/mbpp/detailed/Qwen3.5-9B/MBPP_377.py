def _is_character_valid(value):
    """
    Validates that the provided value is a string of exactly one character.

    Returns:
        bool: True if valid, False otherwise.
    """
    if not isinstance(value, str):
        return False
    if len(value) != 1:
        return False
    return True


def _is_string_valid(value):
    """
    Validates that the provided value is a string.

    Returns:
        bool: True if valid, False otherwise.
    """
    return isinstance(value, str)


def remove_char(input_string, character_to_remove):
    """
    Removes all occurrences of a specific character from a given string.

    This function performs robust input validation before attempting to process
    the data. It handles edge cases such as empty strings, strings containing no
    instances of the target character, and strings containing only the target
    character.

    Args:
        input_string (str): The string from which characters will be removed.
        character_to_remove (str): The single character to remove from the input string.

    Returns:
        str: A new string with all occurrences of the specified character removed.

    Raises:
        TypeError: If input_string is not a string or if character_to_remove is not
                   a string of exactly one character.

    Examples:
        remove_char("aba", "a") -> "b"
        remove_char("toggle", "g") -> "tole"
        remove_char("aabbc", "b") -> "aac"
        remove_char("", "x") -> ""
        remove_char("aaa", "a") -> ""
    """
    # Step 1: Validate the input string type and existence
    if input_string is None:
        raise TypeError("Input string cannot be None.")

    if not _is_string_valid(input_string):
        raise TypeError(f"Expected input_string to be a string, got {type(input_string).__name__}.")

    # Step 2: Validate the character to remove type and existence
    if character_to_remove is None:
        raise TypeError("Character to remove cannot be None.")

    if not _is_character_valid(character_to_remove):
        raise TypeError(
            f"Expected character_to_remove to be a string of length 1, got '{character_to_remove}' (length {len(character_to_remove)})."
        )

    # Step 3: Define the character to target for comparison
    target_char = character_to_remove[0]

    # Step 4: Initialize an empty list to collect characters that will remain
    result_characters = []

    # Step 5: Iterate through each character in the input string explicitly
    for current_char in input_string:
        # Step 6: Check if the current character matches the target character
        if current_char != target_char:
            # Step 7: If it does not match, append it to our result list
            result_characters.append(current_char)

    # Step 8: Join the list of characters into a final string
    final_result = "".join(result_characters)

    # Step 9: Return the resulting string
    return final_result