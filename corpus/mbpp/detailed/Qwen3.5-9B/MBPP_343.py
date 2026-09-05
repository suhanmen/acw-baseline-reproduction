def is_digit_character(char_code: int) -> bool:
    """
    Determine if a given Unicode character code represents a digit.

    This function checks if the character falls within the standard ASCII
    range for digits '0' through '9'.

    Args:
        char_code (int): The integer Unicode code point of the character.

    Returns:
        bool: True if the character is a digit, False otherwise.
    """
    if not isinstance(char_code, int):
        raise TypeError("Character code must be an integer.")

    # The Unicode code point for '0' is 48
    # The Unicode code point for '9' is 57
    DIGIT_START = ord('0')
    DIGIT_END = ord('9')

    return DIGIT_START <= char_code <= DIGIT_END


def is_letter_character(char_code: int) -> bool:
    """
    Determine if a given Unicode character code represents a letter (A-Z, a-z).

    This function checks if the character falls within the standard ASCII
    ranges for uppercase (65-90) or lowercase (97-122) letters.

    Args:
        char_code (int): The integer Unicode code point of the character.

    Returns:
        bool: True if the character is a letter, False otherwise.
    """
    if not isinstance(char_code, int):
        raise TypeError("Character code must be an integer.")

    # Uppercase ASCII range
    LETTER_A = ord('A')
    LETTER_Z = ord('Z')

    # Lowercase ASCII range
    LETTER_a = ord('a')
    LETTER_z = ord('z')

    # Check if uppercase
    if LETTER_A <= char_code <= LETTER_Z:
        return True

    # Check if lowercase
    if LETTER_a <= char_code <= LETTER_z:
        return True

    return False


def count_digit_letters(input_string: str) -> tuple:
    """
    Calculate the number of digits and letters in the provided string.

    This function iterates through each character of the input string,
    classifies it as a digit or a letter using helper functions, and
    returns a tuple containing the count of digits and the count of letters.

    Edge cases handled:
    - Empty string: Returns (0, 0).
    - None input: Raises a TypeError.
    - Non-string input: Raises a TypeError.
    - Special characters/punctuation: Counted as neither digits nor letters.

    Args:
        input_string (str): The string to analyze.

    Returns:
        tuple: A tuple (digit_count, letter_count) where both are non-negative integers.

    Raises:
        TypeError: If the input is not a string.
    """
    # Explicit validation of input type
    if input_string is None:
        raise TypeError("Input cannot be None.")

    if not isinstance(input_string, str):
        raise TypeError(f"Input must be a string, received type: {type(input_string).__name__}.")

    digit_count = 0
    letter_count = 0
    total_chars = 0

    # Helper lambda to get char code safely for iteration
    def get_char_code(char: str) -> int:
        if not isinstance(char, str):
            raise ValueError("Character found in iteration is not a string.")
        return ord(char)

    # Iterate through each character explicitly
    for current_char in input_string:
        total_chars += 1

        try:
            char_code = get_char_code(current_char)
        except ValueError:
            # This case should theoretically not be reached if current_char is from a str
            continue

        # Check for digit status explicitly
        is_digit = is_digit_character(char_code)

        # Check for letter status explicitly
        is_letter = is_letter_character(char_code)

        # Accumulate counts based on conditions
        if is_digit:
            digit_count += 1
        elif is_letter:
            letter_count += 1
        # Characters that are neither digits nor letters are simply ignored

    return digit_count, letter_count