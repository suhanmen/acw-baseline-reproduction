from collections import Counter

def _validate_string_input(value: str, label: str) -> None:
    """
    Validates that the provided value is a string instance.
    Raises a TypeError if the type check fails.

    :param value: The value to validate.
    :param label: A descriptive label for the error message.
    :raises TypeError: If the value is not a string.
    """
    if not isinstance(value, str):
        raise TypeError(f"{label} must be a string, got {type(value).__name__}")


def _extract_char_counts(sequence: str) -> dict:
    """
    Extracts a frequency count of each character in the input sequence.
    Returns a dictionary where keys are characters and values are their counts.

    :param sequence: The string to analyze.
    :return: A dictionary mapping characters to their frequency counts.
    """
    counts = {}
    for char in sequence:
        if char in counts:
            counts[char] = counts[char] + 1
        else:
            counts[char] = 1
    return counts


def _compare_char_counts(counts0: dict, counts1: dict) -> bool:
    """
    Compares two character count dictionaries to determine if they are identical.
    Two dictionaries are considered identical if they have the same keys
    and the same values for those keys.

    :param counts0: The first character count dictionary.
    :param counts1: The second character count dictionary.
    :return: True if the dictionaries are identical, False otherwise.
    """
    # Check if keys match
    if set(counts0.keys()) != set(counts1.keys()):
        return False

    # Check if values match for each key
    for key in counts0:
        if counts0[key] != counts1[key]:
            return False

    return True


def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.

    This function determines if two input strings contain exactly the same characters
    with the same frequencies. It performs strict type checking and handles edge cases
    such as empty strings or non-string inputs gracefully by raising appropriate errors.

    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    # Step 1: Explicit validation of input types
    _validate_string_input(s0, "First argument (s0)")
    _validate_string_input(s1, "Second argument (s1)")

    # Step 2: Handle the edge case where both strings are empty
    # Technically, two empty strings have the same character set (empty), so they match.
    if s0 == "" and s1 == "":
        return True

    # Step 3: Determine the length of the shorter and longer string
    len_s0 = len(s0)
    len_s1 = len(s1)

    is_s0_empty = (len_s0 == 0)
    is_s1_empty = (len_s1 == 0)

    # If one is empty and the other is not, they cannot have the same characters
    if is_s0_empty or is_s1_empty:
        return False

    # Step 4: If lengths differ, they cannot have the same character counts
    # because the sum of frequencies must be equal.
    if len_s0 != len_s1:
        return False

    # Step 5: Extract character counts for the first string
    counts_s0 = _extract_char_counts(s0)

    # Step 6: Extract character counts for the second string
    counts_s1 = _extract_char_counts(s1)

    # Step 7: Compare the resulting character count dictionaries
    result = _compare_char_counts(counts_s0, counts_s1)

    return result