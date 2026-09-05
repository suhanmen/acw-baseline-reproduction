def remove_dirty_chars(source_string: str, characters_to_remove: str) -> str:
    """
    Removes all characters from the source_string that are present in the characters_to_remove string.
    The removal is case-sensitive.

    Args:
        source_string (str): The string from which characters need to be removed.
        characters_to_remove (str): The string containing characters that should be removed from source_string.

    Returns:
        str: A new string with all characters from source_string that appear in characters_to_remove removed.

    Raises:
        TypeError: If either source_string or characters_to_remove is not a string.
    """

    # Validate input types explicitly
    if not isinstance(source_string, str):
        raise TypeError(f"source_string must be a string, got {type(source_string).__name__}")

    if not isinstance(characters_to_remove, str):
        raise TypeError(f"characters_to_remove must be a string, got {type(characters_to_remove).__name__}")

    # Handle edge case where the string to search for characters in is empty
    # In this case, no characters should be removed based on the logic "present in the second string"
    if len(characters_to_remove) == 0:
        return source_string

    # Create a set of characters to remove for O(1) average time complexity lookups
    # This handles potential duplicates in the second string efficiently
    characters_to_remove_set = set(characters_to_remove)

    # Initialize a list to hold the characters that will form the result string
    result_characters = []

    # Iterate explicitly over each character in the source string
    for current_char in source_string:
        # Check if the current character exists in our set of characters to remove
        if current_char in characters_to_remove_set:
            # Skip the character (do not add to the result list)
            continue

        # If the character is not in the removal set, keep it
        result_characters.append(current_char)

    # Join the list of kept characters to form the final result string
    final_result = "".join(result_characters)

    return final_result