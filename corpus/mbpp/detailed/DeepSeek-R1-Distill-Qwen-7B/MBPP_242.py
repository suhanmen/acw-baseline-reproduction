def count_charac(s):
    """
    Counts the total characters in a string.

    Args:
        s (str): The input string to count characters from.

    Returns:
        int: The count of characters in the string if it's valid.
             0 if the input is invalid (not a string, negative length, etc.)
    """
    # Check if the input is a string
    if not isinstance(s, str):
        return 0

    # Check if the string has a negative length
    if len(s) < 0:
        return 0

    # For valid input, return the length of the string
    return len(s)