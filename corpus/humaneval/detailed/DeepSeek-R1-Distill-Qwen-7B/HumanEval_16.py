def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")

    if len(string) == 0:
        return 0

    # Normalize all characters to lowercase
    normalized = string.lower()

    # Use a set to track unique characters
    unique_chars = set(normalized)

    # Return the count of unique characters
    return len(unique_chars)