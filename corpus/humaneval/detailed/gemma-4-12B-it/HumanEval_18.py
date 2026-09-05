from typing import Any


def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # Type validation: Ensure inputs are strings as per the signature.
    # Even though Python is dynamically typed, production code should check.
    if not isinstance(string, str):
        raise TypeError(f"Expected string for 'string' argument, got {type(string).__name__}")
    if not isinstance(substring, str):
        raise TypeError(f"Expected string for 'substring' argument, got {type(substring).__name__}")

    # Handle the case where the substring is empty.
    # Conventionally, an empty string is found at every position, but 
    # in standard counting problems, if the substring is empty, we return 0 
    # to avoid infinite loops or ambiguity.
    if len(substring) == 0:
        return 0

    # Handle the case where the original string is empty but the substring is not.
    if len(string) == 0:
        return 0

    # Initialize the counter for occurrences.
    occurrence_count: int = 0

    # Cache lengths to avoid repeated calls in the loop.
    string_length: int = len(string)
    substring_length: int = len(substring)

    # We iterate through the string. We stop at the point where the 
    # remaining characters are fewer than the length of the substring.
    # This ensures we don't check indices that would go out of bounds.
    # We use a range that includes the possibility of finding the substring 
    # ending at the very last index of the string.
    for start_index in range(string_length - substring_length + 1):
        # Extract a slice of the string starting at the current index.
        # The length of the slice is exactly the length of the substring.
        current_slice: str = string[start_index : start_index + substring_length]

        # Check if the extracted slice matches the target substring.
        # Because we increment the index by 1 every time, we naturally
        # count overlapping occurrences.
        if current_slice == substring:
            occurrence_count += 1

    return occurrence_count