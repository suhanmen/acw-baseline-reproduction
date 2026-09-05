import string

def _is_uppercase_char(character):
    """
    Helper function to check if a single character is an uppercase letter.

    Args:
        character (str): A single character string to check.

    Returns:
        bool: True if the character is an uppercase letter (A-Z), False otherwise.
    """
    # Method 1: Using string constants (more explicit and readable for this specific use case)
    if not isinstance(character, str):
        return False

    if len(character) != 1:
        return False

    return character in string.ascii_uppercase

def _get_ascii_code_for_uppercase(char):
    """
    Helper function to get the ASCII code of an uppercase character.

    Args:
        char (str): An uppercase character string.

    Returns:
        int: The ASCII code of the character.

    Raises:
        ValueError: If the character is not an uppercase letter.
    """
    if not isinstance(char, str):
        raise ValueError("Input must be a string character.")

    if len(char) != 1:
        raise ValueError("Input must be a single character string.")

    if not _is_uppercase_char(char):
        raise ValueError(f"Character '{char}' is not an uppercase letter.")

    return ord(char)

def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    # Step 1: Validate the input type
    if not isinstance(s, str):
        raise TypeError(f"Expected string input, but received type: {type(s).__name__}")

    # Initialize the accumulator variable for the sum
    total_ascii_sum = 0

    # Initialize a list to store valid ASCII codes for debugging/clarity if needed
    # (though we just sum them, this step makes the flow explicit)
    valid_ascii_codes = []

    # Step 2: Iterate through each character in the input string explicitly
    for index, current_char in enumerate(s):
        # Explicit check for character type within the string (defensive programming)
        if not isinstance(current_char, str):
            raise ValueError(f"Character at index {index} is not a string: {type(current_char).__name__}")

        # Explicit check for single character (defensive programming)
        if len(current_char) != 1:
            raise ValueError(f"Character at index {index} is not a single character: '{current_char}'")

        # Step 3: Check if the current character is an uppercase letter
        if _is_uppercase_char(current_char):
            # Step 4: Calculate the ASCII code for the valid uppercase character
            ascii_code = _get_ascii_code_for_uppercase(current_char)

            # Step 5: Append the valid code to our list (explicit step)
            valid_ascii_codes.append(ascii_code)

            # Step 6: Add the code to the running total
            total_ascii_sum += ascii_code

    # Step 7: Return the final calculated sum
    return total_ascii_sum