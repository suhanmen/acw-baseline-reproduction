from typing import Union

def _validate_input(input_value: Union[str, list]) -> str:
    """
    Validates the input to ensure it is a string.
    Raises a TypeError if the input is not a string.
    Handles cases where a list is passed by converting it to a string representation,
    though the problem implies a string input based on the assertions.
    """
    if not isinstance(input_value, str):
        raise TypeError("Input must be a string.")

    # Explicitly handle None as an edge case for empty input
    if input_value is None:
        raise ValueError("Input cannot be None.")

    return input_value

def _count_occurrences(target: str) -> int:
    """
    Counts the non-overlapping occurrences of the target substring 'std' 
    in the given string.

    Steps:
    1. Initialize a counter.
    2. Iterate through the string using a while loop to check for the substring
       starting at each index.
    3. If found, increment the counter and advance the search position by 
       the length of the substring to ensure non-overlapping matches.
    4. Continue until the end of the string is reached.
    """
    occurrence_count = 0
    search_index = 0
    substring_length = len(target)

    # Handle edge case: empty target string
    if substring_length == 0:
        return 0

    while search_index <= len(target) - substring_length:
        current_slice = target[search_index : search_index + substring_length]

        if current_slice == target:
            occurrence_count += 1
            search_index += substring_length  # Advance past this occurrence
        else:
            search_index += 1  # Move to the next character

    return occurrence_count

def count_occurance(input_str: Union[str, list]) -> int:
    """
    Finds the occurrence of characters 'std' in the given string.

    This function:
    1. Validates the input type.
    2. Handles degenerate cases (None, empty string).
    3. Counts non-overlapping occurrences of the exact substring 'std'.

    Parameters:
    input_str (Union[str, list]): The input to search within. Must be a string.

    Returns:
    int: The number of times 'std' appears in the input string.

    Raises:
    TypeError: If the input is not a string.
    ValueError: If the input is None.
    """
    validated_str = _validate_input(input_str)

    if validated_str == "":
        return 0

    result = _count_occurrences(validated_str)
    return result