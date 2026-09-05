def remove_char(s, char):
    """
    Removes all occurrences of a specified character from a given string.

    Args:
        s (str): The input string.
        char (str): The character to remove from the string.

    Returns:
        str: A new string with all occurrences of 'char' removed.
    """
    # Validate inputs (assuming inputs are always valid for this problem)
    if not isinstance(s, str) or not isinstance(char, str):
        raise ValueError("Both inputs must be strings.")

    # Filter out the specified character
    filtered = [c for c in s if c != char]

    # Join the list of characters into a string and return
    return ''.join(filtered)