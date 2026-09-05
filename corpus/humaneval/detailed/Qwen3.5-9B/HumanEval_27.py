import string

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    >>> flip_case('')
    ''
    >>> flip_case('aaa')
    'AAA'
    >>> flip_case('AAA')
    'aaa'
    >>> flip_case('aB3!')
    'Ab3!'
    >>> flip_case('xyzXYZ123!@#')
    'XyZxYz123!@#'
    """

    # Validate that the input is indeed a string
    if not isinstance(string, str):
        raise TypeError(f"Expected a string input, but received {type(string).__name__}")

    # Define a helper function to flip the case of a single character explicitly
    def flip_char_case(char: str) -> str:
        """
        Flips the case of a single character.
        - Lowercase -> Uppercase
        - Uppercase -> Lowercase
        - Other (digits, symbols) -> No change
        """
        # Check if the character is lowercase
        if char in string.ascii_lowercase:
            # Convert to uppercase
            return char.upper()
        # Check if the character is uppercase
        elif char in string.ascii_uppercase:
            # Convert to lowercase
            return char.lower()
        # For any other character (digits, punctuation, whitespace), return as is
        else:
            return char

    # Edge case: Empty string
    # If the string is empty, the loop range will be empty, result will be empty.
    # We explicitly handle this logic via the loop below, but noting that 
    # an empty string is valid input and should return an empty string.

    # Initialize the result string builder
    result_chars = []

    # Iterate through each character in the input string explicitly
    # We do not use a list comprehension or a built-in map to ensure step-by-step visibility
    for current_char in string:
        # Call the helper function to process the current character
        flipped_char = flip_char_case(current_char)

        # Append the processed character to our result list
        result_chars.append(flipped_char)

    # Join the list of characters into a final string
    final_result = "".join(result_chars)

    # Return the final result
    return final_result