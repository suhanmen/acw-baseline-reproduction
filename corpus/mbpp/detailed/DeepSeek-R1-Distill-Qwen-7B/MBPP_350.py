def minimum_Length(s):
    """
    Find the minimum length of the string after removing exactly one character.

    Args:
        s (str): The input string.

    Returns:
        int: The minimum possible length after removing one character.

    Raises:
        TypeError: If the input is not a string.
    """
    # Step 1: Validate the input
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")

    # Handle empty string
    if len(s) == 0:
        return 0

    # Handle single-character string
    if len(s) == 1:
        return 0

    # Step 2: Count the frequency of each character
    from collections import Counter
    char_count = Counter(s)

    # Step 3: Find the character with the maximum frequency
    max_count = max(char_count.values())

    # Step 4: Create a new string by removing one occurrence of the most frequent character
    for char, count in char_count.items():
        if count == max_count:
            # Create a new string by removing one occurrence of this character
            new_string = s.replace(char, '', 1)
            return len(new_string)

    # If all characters are unique (e.g., "abcda" where each character appears once except 'a' which appears twice)
    # But since we have already handled empty and single-character strings, and 'max_count' is at least 1,
    # this case should not occur
    return len(s) - 1