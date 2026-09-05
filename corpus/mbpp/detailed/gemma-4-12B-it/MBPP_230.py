def replace_blank(input_string: str, replacement_char: str) -> str:
    """
    Replaces all blank space characters (' ') in a given string with 
    a specified replacement character.

    Args:
        input_string (str): The string containing spaces to be replaced.
        replacement_char (str): The character to insert in place of spaces.

    Returns:
        str: The modified string.

    Raises:
        TypeError: If input_string is not a string or replacement_char is not a string.
        ValueError: If replacement_char is not exactly one character long.
    """
    # --- Input Validation ---

    # Check if input_string is a string
    if not isinstance(input_string, str):
        raise TypeError(f"Expected input_string to be str, got {type(input_string).__name__}")

    # Check if replacement_char is a string
    if not isinstance(replacement_char, str):
        raise TypeError(f"Expected replacement_char to be str, got {type(replacement_char).__name__}")

    # Ensure the replacement character is exactly one character
    # While the prompt implies a single character, we validate for production safety
    if len(replacement_char) != 1:
        # Special case: if it's empty, we might want to treat it as a deletion,
        # but the prompt implies a replacement of a space with a character.
        # We enforce a single character for strictness.
        raise ValueError("replacement_char must be exactly one character long.")

    # --- Edge Case Handling ---

    # If the input string is empty, return an empty string immediately
    if len(input_string) == 0:
        return ""

    # If there are no spaces in the string, return the original string
    if " " not in input_string:
        return input_string

    # --- Processing Logic ---

    # We build the result string character by character to maintain 
    # explicit control flow and clarity.

    result_chars = []

    for current_char in input_string:
        if current_char == " ":
            # If the character is a space, append the replacement
            result_chars.append(replacement_char)
        else:
            # Otherwise, append the original character
            result_chars.append(current_char)

    # Join the list of characters into a final string
    final_result = "".join(result_chars)

    return final_result

# The following assertions verify the requirements:
if __name__ == "__main__":
    # Provided test cases
    assert replace_blank("hello people", '@') == "hello@people"
    assert replace_blank("python program language", '$') == "python$program$language"
    assert replace_blank("blank space", "-") == "blank-space"

    # Additional production-grade edge cases
    assert replace_blank("", "@") == ""                 # Empty input
    assert replace_blank("   ", "*") == "***"           # Only spaces
    assert replace_blank("no_spaces", "@") == "no_spaces" # No spaces
    assert replace_blank("a b c", "!") == "a!b!c"        # Multiple spaces
    assert replace_blank(" ", "X") == "X"                # Single space