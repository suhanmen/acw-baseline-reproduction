def validate_string_input(data):
    """
    Validates that the input is a string and returns the data if valid.
    Raises a TypeError if the input is not a string.

    Args:
        data: The data to validate.

    Returns:
        The validated string data.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(data, str):
        raise TypeError(f"Input must be a string, but got {type(data).__name__}")
    return data

def is_valid_pattern_match(text):
    """
    Checks if the text matches the pattern: exactly one 'a' followed by one or more 'b's.
    The string must end immediately after the last 'b'.

    Args:
        text: The string to check.

    Returns:
        True if the text matches the pattern, False otherwise.
    """
    # Pattern: 'a' followed by at least one 'b', nothing else.
    # We can do this manually without regex to show the logic explicitly.

    # Check if string is empty
    if len(text) == 0:
        return False

    # Check if string has only one character
    if len(text) == 1:
        return False

    # Check first character is 'a'
    first_char = text[0]
    if first_char != 'a':
        return False

    # Check the rest of the characters (from index 1 to end) are all 'b'
    # Since length is > 1, index 1 exists.
    remaining_part = text[1:]

    # Check if remaining part is empty (would mean "a" alone, which fails "one or more b's")
    if len(remaining_part) == 0:
        return False

    # Verify all characters in the remaining part are 'b'
    for char_index in range(len(remaining_part)):
        current_char = remaining_part[char_index]
        if current_char != 'b':
            return False

    # If we passed all checks, it is a match
    return True

def format_match_result(is_matched):
    """
    Formats the boolean match result into the required string output.

    Args:
        is_matched: Boolean indicating if a match was found.

    Returns:
        String "Found a match!" if matched, "Not matched!" otherwise.
    """
    if is_matched:
        return "Found a match!"
    else:
        return "Not matched!"

def text_match_one(text):
    """
    Main function to match a string that has an 'a' followed by one or more 'b's.

    Args:
        text (str): The input string to analyze.

    Returns:
        str: "Found a match!" if the pattern is matched, otherwise "Not matched!".

    Edge Cases Handled:
        - Empty string: Returns "Not matched!"
        - Single character (e.g., "a", "b"): Returns "Not matched!"
        - Multiple 'a's (e.g., "aa"): Returns "Not matched!"
        - No 'b's after 'a' (e.g., "a"): Returns "Not matched!"
        - Non-b characters after 'a' (e.g., "ac"): Returns "Not matched!"
        - Input not a string: Raises TypeError
    """
    # Step 1: Validate the input type
    validated_text = validate_string_input(text)

    # Step 2: Perform the pattern matching logic
    match_found = is_valid_pattern_match(validated_text)

    # Step 3: Format and return the result
    result_message = format_match_result(match_found)

    return result_message