def ascii_value(char: str) -> int:
    """
    Returns the ASCII integer value of a single character string.

    Args:
        char (str): A string expected to contain exactly one character.

    Returns:
        int: The ASCII value of the character.

    Raises:
        ValueError: If the input is not a string, is empty, or contains 
                    more than one character.
        TypeError: If the input type is not a string.
    """
    # Step 1: Validate input type
    # We ensure that the input is strictly a string to prevent unexpected behavior.
    if not isinstance(char, str):
        raise TypeError(f"Input must be a string, received: {type(char).__name__}")

    # Step 2: Validate input length
    # The problem asks for the value of 'a' character. 
    # An empty string or a string with multiple characters is an invalid input for this scope.
    input_length = len(char)

    if input_length == 0:
        raise ValueError("Input string cannot be empty.")

    if input_length > 1:
        raise ValueError(f"Input must be a single character, received a string of length {input_length}.")

    # Step 3: Extract the single character
    # Since we validated the length is exactly 1, this is safe.
    single_char = char[0]

    # Step 4: Convert to ASCII
    # The ord() function in Python returns the Unicode code point of the character.
    # For the standard ASCII range (0-127), Unicode code points match ASCII values exactly.
    try:
        ascii_code = ord(single_char)
    except Exception as e:
        # This block handles rare cases where ord() might fail due to environment constraints
        raise RuntimeError(f"An error occurred while calculating the ASCII value: {e}")

    # Step 5: Return the result
    return ascii_code

# Assertions to verify correctness
if __name__ == "__main__":
    assert ascii_value('A') == 65
    assert ascii_value('R') == 82
    assert ascii_value('S') == 83