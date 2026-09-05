import string

def dig_let(input_string: str) -> tuple[int, int]:
    """
    Calculates the number of digits and the number of alphabetic letters 
    in a given string.

    Args:
        input_string (str): The string to analyze.

    Returns:
        tuple[int, int]: A tuple containing (digit_count, letter_count).

    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input type
    if not isinstance(input_string, str):
        raise TypeError(f"Input must be a string, but received {type(input_string).__name__}")

    # Initialize counters
    digit_count = 0
    letter_count = 0

    # Define what constitutes a digit and a letter clearly.
    # We use string.digits for '0123456789' 
    # and string.ascii_letters for 'abcdef...XYZ'
    valid_digits = set(string.digits)
    valid_letters = set(string.ascii_letters)

    # Iterate through each character in the input string
    # We use a standard loop to ensure every step is explicitly visible
    for character in input_string:
        # Handle potential edge cases like whitespace, symbols, or emojis
        # These will be ignored by both counters.

        # Check if the character is a digit
        if character in valid_digits:
            digit_count += 1

        # Check if the character is an alphabetic letter
        elif character in valid_letters:
            letter_count += 1

        # If the character is neither (e.g., '.', ' ', '!', '@'),
        # we do nothing, as the problem only asks for digits and letters.

    # Return the final counts as a tuple
    return (digit_count, letter_count)

# The following assertions verify the requirements provided in the prompt.
if __name__ == "__main__":
    # Test Case 1: Only letters
    assert dig_let("python") == (0, 6)

    # Wait, let's re-read the prompt requirements:
    # assert dig_let("python") == (6, 0)
    # Looking at the prompt's assertions again:
    # assert dig_let("python") == (6, 0)
    # This implies the first number is letters and the second is digits?
    # Let's re-examine the prompt: "calculate the number of digits and letters"
    # Usually, "digits and letters" maps to (digits, letters).
    # However, the provided assertions say:
    # "python" (6 letters, 0 digits) -> (6, 0)
    # "program" (7 letters, 0 digits) -> (7, 0)
    # "python3.0" (6 letters, 2 digits) -> (6, 2)
    # This means the format is (letter_count, digit_count).

    # I will adjust the internal logic to match the specific assertion order provided.
    pass

def dig_let(input_string: str) -> tuple[int, int]:
    """
    Revised to strictly match the assertion order: (letter_count, digit_count)
    as defined by the prompt's provided test cases.
    """
    if not isinstance(input_string, str):
        raise TypeError(f"Input must be a string, but received {type(input_string).__name__}")

    letter_count = 0
    digit_count = 0

    valid_digits = set("0123456789")
    valid_letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

    for character in input_string:
        if character in valid_letters:
            letter_count += 1
        elif character in valid_digits:
            digit_count += 1

    return (letter_count, digit_count)

# Final verification against prompt assertions:
# assert dig_let("python") == (6, 0)   -> 6 letters, 0 digits. Correct.
# assert dig_let("program") == (7, 0)  -> 7 letters, 0 digits. Correct.
# assert dig_let("python3.0") == (6, 2) -> 6 letters ('python'), 2 digits ('3', '0'). Correct.