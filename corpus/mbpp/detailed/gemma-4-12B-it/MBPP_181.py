from typing import List


def common_prefix(strings: List[str], num_strings: int) -> str:
    """
    Finds the longest common prefix among the first 'num_strings' 
    elements in the provided list of strings.

    Args:
        strings: A list of strings to search for a common prefix.
        num_strings: The number of strings from the start of the list 
                      to consider.

    Returns:
        The longest common prefix as a string. Returns an empty string 
        if no common prefix exists or if the input is invalid.

    Raises:
        ValueError: If num_strings is negative or exceeds the list size.
        TypeError: If the input list contains non-string elements.
    """
    # 1. Validate input types and basic integrity
    if not isinstance(strings, list):
        raise TypeError("Input 'strings' must be a list.")

    if not isinstance(num_strings, int):
        raise TypeError("Input 'num_strings' must be an integer.")

    # 2. Handle edge cases for bounds
    if num_strings < 0:
        raise ValueError("num_strings cannot be negative.")

    if num_strings > len(strings):
        # Depending on requirements, we could raise an error or cap it.
        # The problem implies we use the count provided.
        raise ValueError("num_strings exceeds the length of the input list.")

    # 3. Handle empty input or zero requested strings
    if num_strings == 0 or len(strings) == 0:
        return ""

    # 4. Extract the subset of strings to compare
    # We only care about the first 'num_strings'
    subset = strings[:num_strings]

    # 5. Validate that all elements in the subset are strings
    for item in subset:
        if not isinstance(item, str):
            raise TypeError(f"All elements in the list must be strings. Found: {type(item)}")

    # 6. Handle subset edge cases
    if not subset:
        return ""

    # If there is only one string, the longest common prefix is the string itself
    if len(subset) == 1:
        return subset[0]

    # 7. Determine the common prefix
    # We use the first string as the initial "reference" prefix
    reference_string = subset[0]

    # If the first string is empty, the common prefix must be empty
    if not reference_string:
        return ""

    # We will iteratively shorten the reference_string until it matches 
    # the start of every string in the subset.
    current_prefix = reference_string

    for i in range(1, len(subset)):
        current_word = subset[i]

        # While the current_word does not start with current_prefix,
        # shorten the prefix by one character from the end.
        while not current_word.startswith(current_prefix):
            # If the prefix becomes empty, there is no common prefix at all
            if not current_prefix:
                return ""

            # Remove the last character
            current_prefix = current_prefix[:-1]

    return current_prefix