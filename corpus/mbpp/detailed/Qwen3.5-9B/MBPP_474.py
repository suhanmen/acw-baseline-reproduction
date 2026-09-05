def replace_char(input_string: str, old_char: str, new_char: str) -> str:
    """
    Replaces all occurrences of a specified character in a string with another character.

    This function performs the following steps:
    1. Validates the input string to ensure it is a valid string.
    2. Validates the 'old_char' to ensure it is a single character string.
    3. Validates the 'new_char' to ensure it is a single character string.
    4. Iterates through each character of the input string.
    5. If the current character matches the 'old_char', it is replaced with 'new_char'.
    6. If it does not match, the original character is kept.
    7. The resulting characters are joined to form the final output string.

    Edge cases handled explicitly:
    - Empty input string: Returns an empty string.
    - Single element string: Checks and replaces if applicable.
    - All-equal elements (old_char): Replaces every instance with new_char.
    - No matches (old_char not present): Returns the original string unchanged.
    - Invalid inputs: Raises ValueError with descriptive messages.
    - Boundary values: Handles strings of length 1 correctly.
    - Negative numbers: Not applicable as input is strictly a string, but type checking is performed.

    Args:
        input_string (str): The string in which characters will be replaced.
        old_char (str): The character to be replaced. Must be exactly one character.
        new_char (str): The character to replace with. Must be exactly one character.

    Returns:
        str: A new string with all occurrences of old_char replaced by new_char.

    Raises:
        ValueError: If input_string, old_char, or new_char are not strings or if
                    old_char/new_char are not of length 1.
    """

    # Step 1: Validate input_string
    if not isinstance(input_string, str):
        raise ValueError("The 'input_string' must be a string.")

    # Step 2: Validate old_char
    if not isinstance(old_char, str):
        raise ValueError("The 'old_char' must be a string.")
    if len(old_char) != 1:
        raise ValueError("The 'old_char' must be exactly one character.")

    # Step 3: Validate new_char
    if not isinstance(new_char, str):
        raise ValueError("The 'new_char' must be a string.")
    if len(new_char) != 1:
        raise ValueError("The 'new_char' must be exactly one character.")

    # Step 4: Initialize variables for the result construction
    result_parts: list[str] = []

    # Step 5: Explicitly iterate through the input string
    for current_char in input_string:
        # Check if the current character matches the one to be replaced
        if current_char == old_char:
            # Append the replacement character
            result_parts.append(new_char)
        else:
            # Append the original character if no match
            result_parts.append(current_char)

    # Step 6: Join the parts to form the final result string
    final_output: str = "".join(result_parts)

    # Step 7: Return the final output
    return final_output