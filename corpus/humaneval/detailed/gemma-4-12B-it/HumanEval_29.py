from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    # Input validation: Ensure the list of strings is actually a list
    if not isinstance(strings, list):
        raise TypeError(f"Expected a list of strings, but received {type(strings).__name__}")

    # Input validation: Ensure the prefix is actually a string
    if not isinstance(prefix, str):
        raise TypeError(f"Expected prefix to be a string, but received {type(prefix).__name__}")

    # Initialize an empty list to store the results that meet the criteria
    filtered_results: List[str] = []

    # If the input list is empty, we can return the empty results immediately
    if len(strings) == 0:
        return filtered_results

    # Iterate through every element provided in the input list
    for item in strings:
        # Defensive check: Ensure each element in the list is actually a string
        # This prevents the code from crashing if the input list is heterogeneous
        if not isinstance(item, str):
            # In production code, we might log this or skip. 
            # Here, we treat non-string items as non-matches.
            continue

        # Determine if the current string starts with the desired prefix
        # The .startswith() method is the standard, production-grade way 
        # to perform this check in Python.
        is_match: bool = item.startswith(prefix)

        # If the condition is satisfied, add it to our results collection
        if is_match:
            filtered_results.append(item)

    # Return the final filtered collection
    return filtered_results