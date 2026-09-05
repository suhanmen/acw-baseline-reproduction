def dig_let(s):
    """
    Calculate the number of digits and letters in a string.

    Args:
        s (str): The input string to be analyzed.

    Returns:
        tuple: A tuple containing two integers, (number_of_digits, number_of_letters).

    Raises:
        ValueError: If the input is not a string.
    """
    # Validate the input is a string
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")

    # Initialize counters for digits and letters
    num_digits = 0
    num_letters = 0

    # Helper function to check if a character is a digit
    def is_digit(c):
        return c.isdigit()

    # Helper function to check if a character is a letter
    def is_letter(c):
        return c.isalpha()

    # Iterate through each character in the string
    for c in s:
        if is_digit(c):
            num_digits += 1
        elif is_letter(c):
            num_letters += 1

    # Return the counts as a tuple
    return (num_digits, num_letters)