def remove_Occ(string, char_to_remove):
    """
    Removes the first and last occurrence of a specified character from a string.

    Args:
        string: The input string.
        char_to_remove: The character to remove.

    Returns:
        The modified string after removing the first and last occurrence of the specified character.

    Raises:
        ValueError: If the input conditions are not met.
    """
    # Validate inputs
    if not string:
        raise ValueError("Input string cannot be empty.")
    if not isinstance(char_to_remove, str) or len(char_to_remove) != 1:
        raise ValueError("char_to_remove must be a single character string.")

    # Find the first occurrence index
    first = None
    for i, c in enumerate(string):
        if c == char_to_remove:
            first = i
            break
    if first is None:
        return string  # character not found, return original string

    # Find the last occurrence index
    last = None
    for i, c in enumerate(string):
        if c == char_to_remove:
            last = i
    # Check if first and last are the same (single occurrence)
    if first == last:
        return string  # only one occurrence, return original

    # Create the new string by excluding first and last characters
    return string[:first] + string[first+1:last] + string[last+1:]