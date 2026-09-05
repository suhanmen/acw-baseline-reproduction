def _validate_string_input(value) -> str:
    """
    Validates that the input is a string and not empty or None.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty.

    Returns:
        The validated and casted string.
    """
    if value is None:
        raise ValueError("Input cannot be None.")

    if not isinstance(value, str):
        raise TypeError(f"Input must be a string, got {type(value).__name__}.")

    if len(value) == 0:
        raise ValueError("Input string cannot be empty.")

    return value


def _count_substring_ends(input_string: str) -> int:
    """
    Counts the number of substrings where the first and last characters are equal.

    This function uses the frequency counting approach:
    1. Count the frequency of each character in the string.
    2. For each character with frequency 'n', the number of substrings it can form
       (including single-character substrings) is n * (n + 1) / 2.
       This is derived from the fact that any pair of positions (i, j) where 
       i <= j and s[i] == s[j] forms a valid substring.

    Args:
        input_string (str): The string to analyze. Must be validated before calling.

    Returns:
        int: The total count of substrings with equal first and last characters.
    """
    # Dictionary to store character frequencies
    char_frequency = {}

    # Iterate over the string to count each character
    current_index = 0
    while current_index < len(input_string):
        current_char = input_string[current_index]

        if current_char in char_frequency:
            char_frequency[current_char] = char_frequency[current_char] + 1
        else:
            char_frequency[current_char] = 1

        current_index = current_index + 1

    total_substrings = 0

    # Iterate over each unique character found
    unique_chars = list(char_frequency.keys())
    char_count = len(unique_chars)
    index = 0

    while index < char_count:
        char = unique_chars[index]
        frequency = char_frequency[char]
        index = index + 1

        # Calculate number of substrings for this character using combination formula C(n, 2) + n
        # C(n, 2) = n * (n - 1) / 2 represents pairs (start, end) where start < end
        # + n represents single character substrings where start == end
        # Combined: n * (n - 1) / 2 + n = n * (n + 1) / 2

        combinations = (frequency * (frequency + 1)) // 2
        total_substrings = total_substrings + combinations

    return total_substrings


def count_Substring_With_Equal_Ends(input_str) -> int:
    """
    Counts the number of substrings with the same first and last character.

    A substring is defined by a start index and an end index (inclusive).
    For example, in "aba":
    - "a" (indices 0,0) -> matches
    - "b" (indices 1,1) -> matches
    - "a" (indices 2,2) -> matches
    - "aba" (indices 0,2) -> matches ('a' == 'a')
    Total: 4

    Args:
        input_str: The string to process.

    Returns:
        int: The count of substrings with matching start and end characters.

    Raises:
        TypeError: If input is not a string.
        ValueError: If input is None or an empty string.
    """
    # Step 1: Explicitly validate the input arguments
    validated_input = _validate_string_input(input_str)

    # Step 2: Perform the counting logic on the validated string
    result = _count_substring_ends(validated_input)

    return result