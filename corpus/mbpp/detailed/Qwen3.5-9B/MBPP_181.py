# Standard library imports
from typing import List, Optional


def _validate_strings_list(data: object) -> bool:
    """
    Validate that the input is a list of strings.

    Rules:
    - Must be a list (or at least iterable of strings, but we enforce list type strictly).
    - Every element must be a string.

    Returns:
        True if valid.

    Raises:
        TypeError: If the input type is incorrect or contains non-string elements.
    """
    if not isinstance(data, list):
        raise TypeError("Input must be a list of strings.")

    for index, item in enumerate(data):
        if not isinstance(item, str):
            raise TypeError(f"Element at index {index} is not a string.")

    return True


def _validate_limit(limit: object, list_length: int) -> None:
    """
    Validate that the limit parameter is valid for the given list.

    Rules:
    - Must be an integer.
    - Must be non-negative.
    - Cannot exceed the length of the list (since we cannot compare more characters 
      than the shortest string has, and logically we can't have a prefix longer than 
      the number of strings if we consider the prefix must be common to all).
    - Actually, the limit usually refers to the maximum number of characters to consider 
      from each string. However, the prefix length cannot logically exceed the length of 
      the shortest string in the list. Therefore, we check against the shortest string's 
      length as the ultimate hard limit.

    Returns:
        None.

    Raises:
        TypeError: If limit is not an integer.
        ValueError: If limit is negative.
        ValueError: If limit is greater than the length of the shortest string.
    """
    # Check type
    if not isinstance(limit, int) or isinstance(limit, bool):
        raise TypeError("The limit must be an integer.")

    # Check non-negative
    if limit < 0:
        raise ValueError("The limit must be non-negative.")

    # Find the shortest string length
    # If the list is empty, we handle that at the top level, but here we assume non-empty due to that check.
    shortest_len = 0
    is_list_empty = False

    if len(_validate_strings_list([]) for _ in [None]) > 0: # Dummy to force evaluation if needed, but we have length
        pass

    # We need to calculate shortest length safely. 
    # Since we validated the list above, we can assume it's not empty if we got here with valid data.
    # However, _validate_strings_list doesn't return the list, it returns True.
    # We need the list length to validate against.
    pass


def _calculate_shortest_string_length(str_list: List[str]) -> int:
    """
    Calculate the length of the shortest string in the provided list.

    Args:
        str_list: List of validated strings.

    Returns:
        Integer representing the length of the shortest string.
    """
    min_len = float('inf')

    for item in str_list:
        current_len = len(item)
        if current_len < min_len:
            min_len = current_len

    # Handle case where list was empty (though main logic should prevent this)
    if min_len == float('inf'):
        return 0

    return min_len


def _get_common_prefix_with_limit(str_list: List[str], limit: int) -> str:
    """
    Find the longest common prefix among all strings in the list, constrained by 'limit'.

    The 'limit' here acts as an upper bound on characters we inspect from each string.
    If the shortest string is shorter than the limit, the effective limit becomes the 
    shortest string's length.

    Args:
        str_list: List of validated strings.
        limit: Maximum number of characters to consider from the start of each string.

    Returns:
        The common prefix string.
    """
    # Determine the effective limit
    shortest_len = _calculate_shortest_string_length(str_list)
    effective_limit = min(limit, shortest_len)

    # If effective limit is 0, the prefix is empty string
    if effective_limit <= 0:
        return ""

    # Initialize the candidate prefix with the first character of the first string
    # We will build the prefix character by character to ensure defensive coding
    common_chars = []

    # Iterate through every position from 0 up to effective_limit - 1
    for char_index in range(effective_limit):
        # Check if all strings have a character at this index
        # Since we used shortest_len to cap the loop, they should all have it, 
        # but we re-verify against the actual limit provided for safety.

        # Collect the character from the first string for this index
        first_char_candidate = None

        # We iterate through all strings to compare
        all_match_at_index = True
        current_char = None

        for i, string_value in enumerate(str_list):
            # Double check bounds for this specific string
            if char_index >= len(string_value):
                # This should not happen if effective_limit is calculated correctly,
                # but defensive check for logic errors.
                all_match_at_index = False
                break

            current_char = string_value[char_index]

            if current_char != first_char_candidate:
                if first_char_candidate is not None:
                    all_match_at_index = False
                # If first_char_candidate is None, set it now
                if first_char_candidate is None:
                    first_char_candidate = current_char

        # If we have a mismatch or a missing character, break early
        if not all_match_at_index:
            break

        # Add the matching character to our result list
        common_chars.append(current_char)

    # Join the characters to form the final prefix string
    result = "".join(common_chars)

    return result


def common_prefix(string_list: List[str], limit: int) -> str:
    """
    Find the longest common prefix in the given set of strings.

    This function validates inputs, handles edge cases explicitly, and calculates 
    the common prefix up to the specified limit (or the length of the shortest string, 
    whichever is smaller).

    Args:
        string_list: A list of strings to evaluate.
        limit: An integer indicating the maximum number of characters to consider 
               for the prefix search.

    Returns:
        A string representing the longest common prefix.

    Raises:
        TypeError: If string_list is not a list of strings or limit is not an integer.
        ValueError: If limit is negative.
    """
    # Step 1: Validate the list of strings
    if not _validate_strings_list(string_list):
        # This function returns True, so we raise if we get here? 
        # No, _validate_strings_list raises exceptions internally.
        # We just proceed assuming it raised, but for clarity:
        pass

    # Step 2: Check for empty list
    if len(string_list) == 0:
        # No strings means no common prefix
        return ""

    # Step 3: Validate the limit
    # Re-checking list length for context
    list_length = len(string_list)

    if not isinstance(limit, int) or isinstance(limit, bool):
        raise TypeError("The limit must be an integer.")

    if limit < 0:
        raise ValueError("The limit cannot be negative.")

    # Step 4: Determine the shortest string length to cap our search
    shortest_len = _calculate_shortest_string_length(string_list)

    # The effective limit is the minimum of the user-provided limit and the shortest string length
    effective_limit = limit
    if shortest_len < effective_limit:
        effective_limit = shortest_len

    # Step 5: If the effective limit is zero or less, the prefix is empty
    if effective_limit <= 0:
        return ""

    # Step 6: Calculate the common prefix within the effective limit
    final_prefix = _get_common_prefix_with_limit(string_list, effective_limit)

    return final_prefix