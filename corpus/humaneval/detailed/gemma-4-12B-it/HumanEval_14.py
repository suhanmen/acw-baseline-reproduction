from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Validate that the input is a string
    if not isinstance(string, str):
        raise TypeError(f"Input must be a string, but received {type(string).__name__}")

    # Define the resulting list to store prefixes
    prefixes: List[str] = []

    # Handle the edge case of an empty string explicitly.
    # Based on the docstring example 'abc' -> ['a', 'ab', 'abc'],
    # an empty string results in an empty list because there are no non-empty prefixes.
    if not string:
        return prefixes

    # Calculate the length of the input string to determine the iteration range
    string_length: int = len(string)

    # Iterate through the string to build prefixes of increasing lengths.
    # The range starts at 1 because a prefix must contain at least one character.
    # The range ends at string_length + 1 to include the full string.
    for current_length in range(1, string_length + 1):
        # Slice the string from the beginning to the current index
        current_prefix: str = string[0:current_length]

        # Append the valid prefix to our results list
        prefixes.append(current_prefix)

    return prefixes