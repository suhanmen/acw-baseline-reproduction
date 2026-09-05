from typing import Tuple, Optional


def validate_inputs(string: str, substring: str) -> Tuple[bool, Optional[str]]:
    """
    Validates the inputs for the substring counting function.

    Args:
        string: The main string to search within.
        substring: The substring to search for.

    Returns:
        A tuple (is_valid, error_message). 
        is_valid is True if inputs are valid, False otherwise.
        error_message contains the specific validation failure if any, or None.
    """

    # Both inputs are required to be strings based on the type hints.
    if not isinstance(string, str):
        return False, f"The 'string' argument must be a string, received: {type(string).__name__}"

    if not isinstance(substring, str):
        return False, f"The 'substring' argument must be a string, received: {type(substring).__name__}"

    return True, None


def _is_substring_valid(substring: str) -> bool:
    """
    Checks if a substring is empty, as an empty substring creates an infinite loop 
    if we try to search for it in a non-empty string.

    Args:
        substring: The substring to check.

    Returns:
        True if the substring is valid (non-empty), False otherwise.
    """
    return len(substring) > 0


def count_occurrences_exhaustively(
    target_string: str, 
    search_substring: str, 
    start_index: int
) -> int:
    """
    Counts occurrences of search_substring in target_string starting from start_index,
    allowing for overlapping matches.

    This function implements the core logic by manually slicing and checking,
    ensuring we can catch overlapping instances (e.g., 'aaa' with 'aa').

    Args:
        target_string: The string to search within.
        search_substring: The pattern to search for.
        start_index: The current index in target_string to begin checking from.

    Returns:
        The count of valid occurrences found starting from start_index.
    """
    count = 0
    current_len = len(search_substring)
    target_len = len(target_string)

    # Loop through the target string up to the point where the substring could still fit.
    # We stop at (target_len - current_len + 1) because if we are at index i,
    # we need i + current_len <= target_len + 1 for a valid slice (exclusive end).
    # Actually, simpler logic: if start_index + len > len(target_string), we stop.

    while start_index + current_len <= target_len:
        # Perform the slice operation.
        # In Python, string slicing is forgiving about out-of-bounds indices,
        # returning an empty string or partial string, but we want to check equality.
        # If the slice length is less than the substring length, it won't match, which is fine.
        candidate_slice = target_string[start_index : start_index + current_len]

        # Compare the candidate slice with the search substring.
        if candidate_slice == search_substring:
            count += 1

        # Move to the next index. Crucially, for overlapping matches, we increment by 1.
        # If we incremented by len(substring), we would miss overlaps.
        start_index += 1

    return count


def count_overlapping_occurrences(string: str, substring: str) -> int:
    """
    Public interface for counting overlapping occurrences.

    Args:
        string: The original string.
        substring: The substring to count.

    Returns:
        The number of times substring appears in string, including overlaps.
    """

    # Handle the empty substring case explicitly to prevent infinite loops or logical errors.
    # Although validate_inputs handles it, we add a clear early return here for clarity.
    if len(substring) == 0:
        return 0

    # If the substring is longer than the string, it cannot exist within it.
    if len(substring) > len(string):
        return 0

    # If the string itself is empty and the substring is non-empty (already handled above),
    # or if substring is empty (handled above), return 0.
    if len(string) == 0:
        return 0

    return count_occurrences_exhaustively(string, substring, 0)


def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The main string to search within.
        substring (str): The substring to search for.

    Returns:
        int: The number of times substring appears in string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """

    # Step 1: Validate inputs explicitly.
    is_valid, error_message = validate_inputs(string, substring)

    if not is_valid:
        raise ValueError(error_message)

    # Step 2: Proceed to count occurrences using the specialized helper.
    result = count_overlapping_occurrences(string, substring)

    return result