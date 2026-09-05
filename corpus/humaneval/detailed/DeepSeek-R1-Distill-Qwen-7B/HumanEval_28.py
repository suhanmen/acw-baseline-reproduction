from typing import List

def concatenate(strings: List[str]) -> str:
    """Concatenate list of strings into a single string

    Handles various edge cases including empty input, single element, valid and invalid inputs.

    Args:
        strings: List of strings to be concatenated.

    Returns:
        A single concatenated string.

    Raises:
        ValueError: If the input is not a list of strings.
    """
    # Validate input: ensure it's a list
    if not isinstance(strings, list):
        raise ValueError("Input must be a list of strings")

    # Validate input: ensure all elements are strings
    for element in strings:
        if not isinstance(element, str):
            raise ValueError("All elements in the list must be strings")

    # Handle empty list case
    if not strings:
        return ""

    # Initialize result string
    result = ""

    # Concatenate all strings in the list
    for string in strings:
        result += string

    return result

# Example usage:
# print(concatenate([]))  # Output: ""
# print(concatenate(["a", "b", "c"]))  # Output: "abc"
# print(concatenate(["Hello", "World"]))  # Output: "HelloWorld"
# print(concatenate(["Valid", 123]))  # Raises ValueError