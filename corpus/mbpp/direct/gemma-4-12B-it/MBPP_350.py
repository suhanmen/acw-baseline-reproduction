def minimum_Length(s: str) -> int:
    """
    Minimize the length of the string by removing all occurrences of 
    only one character from the input string.

    The goal is to find which character, when removed entirely, 
    results in the shortest possible string length.
    """
    if not s:
        return 0

    # Calculate the length of the string after removing all occurrences
    # of each unique character present in the string.
    # The result is the minimum of these lengths.
    unique_chars = set(s)
    min_len = len(s)

    for char in unique_chars:
        # Count how many times this specific character appears
        count = s.count(char)
        # The length if this character is removed is total length minus its count
        current_len = len(s) - count
        if current_len < min_len:
            min_len = current_len

    return min_len