def upper_ctr(input_string: str) -> int:
    """
    Counts the number of upper case characters in a given string.

    The function iterates through each character in the string and 
    increments a counter if the character is an uppercase letter.
    """
    # Validate input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    # Initialize the counter
    uppercase_count = 0

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is uppercase
        # isupper() returns True for A-Z and other uppercase unicode letters
        if char.isupper():
            uppercase_count += 1

    # Return the final count
    return uppercase_count