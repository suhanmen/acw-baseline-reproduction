def unique_Characters(input_string: str) -> bool:
    """
    Checks whether all characters in the given string are unique.

    This function validates the input, handles edge cases explicitly,
    and returns True if every character in the string appears exactly once,
    False otherwise.

    :param input_string: The string to check for uniqueness.
    :return: True if all characters are unique, False otherwise.
    """

    # Step 1: Validate input type explicitly
    if not isinstance(input_string, str):
        raise TypeError(f"Input must be of type 'str', got '{type(input_string).__name__}'")

    # Step 2: Handle empty string edge case
    if len(input_string) == 0:
        return True

    # Step 3: Use a set to track seen characters efficiently
    seen_characters = set()

    # Step 4: Iterate through each character in the string
    for current_char in input_string:

        # Check if the character has already been encountered
        if current_char in seen_characters:
            return False

        # Add the current character to the set of seen characters
        seen_characters.add(current_char)

    # If the loop completes without returning False, all characters are unique
    return True