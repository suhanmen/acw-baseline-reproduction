def ascii_value(char_string: str) -> int:
    """
    Calculates the ASCII integer value for a single character string.

    This function performs rigorous input validation before attempting 
    to compute the character's ASCII value. It handles edge cases such as 
    empty strings, strings with multiple characters, and non-string inputs.

    Args:
        char_string (str): A string representing a single character.

    Returns:
        int: The ASCII integer value of the character.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty or contains more than one character.
    """

    # Step 1: Validate the type of the input argument.
    if not isinstance(char_string, str):
        # Explicitly raise an error if the input is not a string type.
        raise TypeError(f"Input must be a string, but received type: {type(char_string).__name__}")

    # Step 2: Validate that the string is not empty.
    if len(char_string) == 0:
        # Raise an error for empty strings as there is no single character to convert.
        raise ValueError("Input string cannot be empty. A single character is required.")

    # Step 3: Validate that the string contains exactly one character.
    if len(char_string) > 1:
        # Raise an error if more than one character is provided.
        raise ValueError(f"Input string contains {len(char_string)} characters. Only a single character is allowed.")

    # Step 4: Extract the single character from the valid string.
    single_char = char_string[0]

    # Step 5: Check if the character is valid in the Unicode space (which covers ASCII).
    # While ord() works for Unicode, the problem implies standard ASCII context.
    # We proceed with ord() as it returns the code point which matches ASCII for 0-127.

    # Step 6: Convert the character to its integer ASCII value.
    ascii_integer = ord(single_char)

    # Step 7: Return the calculated integer value.
    return ascii_integer