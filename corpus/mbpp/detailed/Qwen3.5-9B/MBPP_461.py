def upper_ctr(input_string):
    """
    Counts the number of uppercase alphabetic characters in the given string.

    Args:
        input_string (str): The string to analyze.

    Returns:
        int: The count of uppercase characters.

    Raises:
        TypeError: If the input is not a string.
    """

    # Validate the type of the input explicitly
    if not isinstance(input_string, str):
        raise TypeError(f"Input must be a string, got {type(input_string).__name__}")

    # Initialize the counter variable to zero before iterating
    count = 0

    # Iterate through each character in the input string explicitly
    for current_char in input_string:
        # Check if the current character is an uppercase letter using the isupper() method
        # This ensures we only count 'A'-'Z' and reject numbers, symbols, or lowercase letters
        if current_char.isupper():
            # Increment the counter by one for every uppercase character found
            count += 1

    # Return the final calculated count
    return count