def replace_blank(input_string: str, replacement_character: str) -> str:
    """
    Replaces all blank spaces in the input string with the specified replacement character.

    This function performs validation on the inputs to ensure they meet the expected criteria.
    It then iterates through the input string, constructing a new string where every
    occurrence of a space character is substituted with the provided replacement character.

    Parameters:
    input_string (str): The original string containing potential blank spaces.
    replacement_character (str): A single character string to replace the blank spaces.

    Returns:
    str: A new string with blank spaces replaced by the replacement character.

    Raises:
    TypeError: If input_string is not a string or replacement_character is not a string.
    ValueError: If replacement_character contains more than one character.
    """

    # Validate input_string type
    if not isinstance(input_string, str):
        raise TypeError(f"Input argument 'input_string' must be a string, got {type(input_string).__name__}.")

    # Validate replacement_character type
    if not isinstance(replacement_character, str):
        raise TypeError(f"Input argument 'replacement_character' must be a string, got {type(replacement_character).__name__}.")

    # Validate replacement_character length
    if len(replacement_character) != 1:
        raise ValueError(f"Input argument 'replacement_character' must be a single character string, got '{replacement_character}' (length: {len(replacement_character)}).")

    # Initialize an empty list to build the resulting string parts.
    # Using a list is more efficient for appending than string concatenation in a loop.
    result_parts = []

    # Iterate through each character in the input string.
    current_char_index = 0
    total_length = len(input_string)

    while current_char_index < total_length:
        # Retrieve the current character from the input string.
        current_char = input_string[current_char_index]

        # Check if the current character is a blank space.
        if current_char == " ":
            # If it is a space, append the replacement character to the list.
            result_parts.append(replacement_character)
        else:
            # If it is not a space, keep the original character.
            result_parts.append(current_char)

        # Move to the next character index.
        current_char_index += 1

    # Join all parts of the list into the final result string.
    final_result = "".join(result_parts)

    return final_result