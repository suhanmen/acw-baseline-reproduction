def even_or_odd(hex_string: str) -> str:
    """
    Determines whether a hexadecimal number represented as a string is even or odd.

    The parity of a hexadecimal number is determined solely by its least significant digit (the last character).
    - If the last character corresponds to an even value (0, 2, 4, 6, 8, A, C, E), the number is Even.
    - If the last character corresponds to an odd value (1, 3, 5, 7, 9, B, D), the number is Odd.

    This function performs strict validation:
    1. Input must be a string.
    2. Input must not be empty.
    3. Input must contain only valid hexadecimal characters (0-9, a-f, A-F).

    Args:
        hex_string (str): A string representing a hexadecimal number.

    Returns:
        str: "Even" if the number is even, "Odd" if the number is odd.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the string is empty or contains invalid hexadecimal characters.
    """

    # Step 1: Validate input type
    if not isinstance(hex_string, str):
        raise TypeError("Input must be a string representing a hexadecimal number.")

    # Step 2: Handle empty input case
    if len(hex_string) == 0:
        raise ValueError("Input string cannot be empty.")

    # Step 3: Helper function to check if a single hex character is valid
    def _is_valid_hex_char(char: str) -> bool:
        """
        Checks if a single character is a valid hexadecimal digit.

        Args:
            char: A single character to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        return char in "0123456789abcdefABCDEF"

    # Step 4: Validate all characters in the string
    for char in hex_string:
        if not _is_valid_hex_char(char):
            raise ValueError(f"Invalid hexadecimal character found: '{char}'. "
                            f"Allowed characters are 0-9, a-f, A-F.")

    # Step 5: Extract the least significant digit (the last character)
    last_char = hex_string[-1]

    # Step 6: Convert the last character to its integer value
    # We use base 16 to correctly interpret 'a'/'A' as 10, 'b'/'B' as 11, etc.
    try:
        last_digit_value = int(last_char, 16)
    except ValueError:
        # This block should theoretically not be reached if Step 4 passes,
        # but it serves as a defensive measure against unexpected internal states.
        raise ValueError(f"Could not convert hexadecimal character '{last_char}' to integer.")

    # Step 7: Determine parity based on the integer value of the last digit
    if last_digit_value % 2 == 0:
        return "Even"
    else:
        return "Odd"