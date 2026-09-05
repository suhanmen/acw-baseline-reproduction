def remove_splchar(input_string: str) -> str:
    """
    Removes all non-alphanumeric characters from the input string.

    Alphanumeric characters are defined as:
    - Letters (a-z, A-Z)
    - Digits (0-9)

    All other characters (spaces, punctuation, special symbols, etc.) are removed.

    Args:
        input_string (str): The string to process.

    Returns:
        str: A new string containing only the alphanumeric characters from the input.

    Raises:
        TypeError: If the input is not a string.
    """
    # Validate that the input is a string instance
    if not isinstance(input_string, str):
        raise TypeError(
            f"Expected input of type 'str', but received type '{type(input_string).__name__}'."
        )

    # Initialize an empty list to build the result.
    # Using a list is more efficient than string concatenation in a loop.
    result_characters = []

    # Iterate through each character in the input string explicitly.
    for current_char in input_string:
        # Check if the character is alphanumeric using Python's built-in isalnum() method.
        # This returns True only if the character is a letter or a digit.
        is_alphanumeric = current_char.isalnum()

        # If the check passes, append the character to our result list.
        if is_alphanumeric:
            result_characters.append(current_char)

    # Join the list of characters into a final string.
    filtered_string = "".join(result_characters)

    return filtered_string