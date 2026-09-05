from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    # Defensive check: Ensure the inputs are of the correct types
    # While Python is dynamically typed, production-grade code often 
    # validates expected types to provide clearer errors for the caller.
    if not isinstance(strings, list):
        raise TypeError(f"Expected 'strings' to be of type List[str], but got {type(strings).__name__}")

    if not isinstance(substring, str):
        raise TypeError(f"Expected 'substring' to be of type str, but got {type(substring).__name__}")

    # Handle the edge case where the input list is empty
    if len(strings) == 0:
        return []

    # Handle the case where the substring is empty. 
    # In Python, any string contains the empty string "".
    # Therefore, if substring is empty, we should return the full original list.
    if substring == "":
        return list(strings)

    filtered_results: List[str] = []

    # Iterate through each item in the provided list
    for current_string in strings:
        # Validate that each item in the list is actually a string
        if not isinstance(current_string, str):
            # For production robustness, we could skip, log, or raise.
            # Here we raise an error to ensure data integrity.
            raise ValueError(f"All elements in the input list must be strings. Found {type(current_string).__name__}.")

        # Check if the substring exists within the current string
        # We use a helper variable to make the logic explicit
        contains_substring: bool = current_string \
            .find(substring) \
            != -1

        # If the condition is met, append the string to our result list
        if contains_substring:
            filtered_results.append(current_string)

    return filtered_results