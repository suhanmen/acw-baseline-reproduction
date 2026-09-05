from typing import List, Optional, Union

Number = Union[int, float]


def _validate_input_list(input_list: object) -> None:
    """
    Validates that the input is a list and that all elements are strings.

    Raises:
        TypeError: If the input is not a list or if any element is not a string.
    """
    if not isinstance(input_list, list):
        raise TypeError(f"Expected input to be a list of strings, but got type: {type(input_list).__name__}")

    for index, item in enumerate(input_list):
        if not isinstance(item, str):
            raise TypeError(f"Expected all elements to be strings, but element at index {index} is of type: {type(item).__name__}")


def _find_longest_word_length(words: List[str]) -> int:
    """
    Calculates the length of the longest word in the provided list.

    Assumes the input list is already validated to contain only strings.

    Returns:
        The length of the longest string. Returns 0 if the list is empty.
    """
    max_length = 0

    for word in words:
        current_length = len(word)
        if current_length > max_length:
            max_length = current_length

    return max_length


def len_log(word_list: object) -> int:
    """
    Finds and returns the length of the longest word in a list of strings.

    This function performs strict validation on the input:
    1. It must be a list.
    2. All elements within the list must be strings.

    If validation fails, a TypeError is raised with a descriptive message.
    If the list is empty, the function returns 0.

    Args:
        word_list: A list containing strings.

    Returns:
        An integer representing the length of the longest string in the list.

    Raises:
        TypeError: If the input structure or element types are invalid.
    """
    _validate_input_list(word_list)

    longest_word_length = _find_longest_word_length(word_list)

    return longest_word_length