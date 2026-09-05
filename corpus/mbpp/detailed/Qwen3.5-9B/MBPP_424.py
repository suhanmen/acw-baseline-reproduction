from typing import Tuple, List, Union

def _validate_string_sequence(data: Union[Tuple[str, ...], List[str]]) -> None:
    """
    Validates that the input is a sequence (tuple or list) where every element
    is a non-empty string. Raises a TypeError if validation fails.
    """
    if not isinstance(data, (tuple, list)):
        raise TypeError(f"Expected a tuple or list of strings, but got {type(data).__name__}")

    for index, item in enumerate(data):
        if not isinstance(item, str):
            raise TypeError(
                f"All elements must be strings. At index {index}, found an object of type "
                f"{type(item).__name__}"
            )
        if len(item) == 0:
            raise ValueError(
                f"Strings must be non-empty. At index {index}, the string is empty."
            )


def _extract_last_char(input_string: str) -> str:
    """
    Extracts the last character from a validated non-empty string.
    Returns the character as a single-character string.
    """
    # Accessing the last index directly
    last_index = len(input_string) - 1
    return input_string[last_index]


def extract_rear(data: Tuple[str, ...]) -> List[str]:
    """
    Extracts only the rear (last) index element of each string in the given tuple.

    Args:
        data: A tuple of non-empty strings.

    Returns:
        A list of strings, where each string is the last character of the corresponding
        input string.

    Raises:
        TypeError: If data is not a tuple or list, or if any element is not a string.
        ValueError: If any string in the tuple is empty.
    """
    # Step 1: Validate the input data structure and content
    _validate_string_sequence(data)

    # Step 2: Initialize an empty list to store the results
    result_list = []

    # Step 3: Iterate through each string in the input tuple explicitly
    # We use an explicit loop to avoid hidden iteration overhead and to allow
    # clear naming of the current element and its position.
    for current_index, current_string in enumerate(data):
        # Safety check: although validation passed, we re-check index existence 
        # for defensive programming if the logic were to change or if data 
        # was somehow mutated (though Python tuples are immutable, this habit helps).
        if current_index >= len(data):
            raise IndexError(f"Index {current_index} is out of range for data of length {len(data)}.")

        # Step 4: Extract the rear character using the helper function
        rear_character = _extract_last_char(current_string)

        # Step 5: Append the extracted character to the result list
        result_list.append(rear_character)

    # Step 6: Return the populated list
    return result_list