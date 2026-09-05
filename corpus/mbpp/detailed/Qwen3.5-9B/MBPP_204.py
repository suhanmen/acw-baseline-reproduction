def count_char_occurrences(target_string: str, target_character: str) -> int:
    """
    Counts the number of occurrences of a specific character within a given string.

    This function performs strict input validation to ensure the target character
    is a single character and the target string is a standard string type.
    It handles edge cases such as empty strings or strings where the character does not exist.
    The logic iterates through the string explicitly to count matches.

    Parameters:
    target_string (str): The string in which to search for the character.
    target_character (str): The character to count. Must be a string of length 1.

    Returns:
    int: The number of times the target_character appears in the target_string.

    Raises:
    TypeError: If target_string is not a string or target_character is not a string.
    ValueError: If target_character is not a single character string.
    """

    # Validate the type of the main input string
    if not isinstance(target_string, str):
        raise TypeError(f"The 'target_string' must be a string. Received: {type(target_string).__name__}")

    # Validate the type of the character to search
    if not isinstance(target_character, str):
        raise TypeError(f"The 'target_character' must be a string. Received: {type(target_character).__name__}")

    # Validate that the character to search is exactly one character long
    if len(target_character) != 1:
        raise ValueError(f"The 'target_character' must be a single character string. Received: '{target_character}' (length: {len(target_character)})")

    # Initialize the counter variable to zero. 
    # This explicitly tracks the total occurrences found.
    occurrence_count = 0

    # Iterate over every character in the target_string using an index loop
    # for explicit control flow, rather than using built-in aggregation methods.
    for index in range(0, len(target_string)):
        # Retrieve the character at the current index
        current_char = target_string[index]

        # Explicitly check if the current character matches the target character
        if current_char == target_character:
            # Increment the counter by one for each match found
            occurrence_count = occurrence_count + 1

    # Return the final calculated count
    return occurrence_count