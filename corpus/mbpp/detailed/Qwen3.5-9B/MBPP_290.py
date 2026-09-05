from typing import Any, List, Tuple, Optional, Union

Number = Union[int, float]
ListElement = List[Number]
ResultTuple = Tuple[int, ListElement]

def validate_list_of_lists(input_list: Any) -> None:
    """
    Validates that the input is a list and that all elements within it are lists.

    Args:
        input_list: The input to validate.

    Raises:
        TypeError: If input_list is not a list, or if any element is not a list.
    """
    if not isinstance(input_list, list):
        raise TypeError(f"Expected a list of lists, but got {type(input_list).__name__}")

    if len(input_list) == 0:
        raise ValueError("The list of lists cannot be empty.")

    for index, item in enumerate(input_list):
        if not isinstance(item, list):
            raise TypeError(f"Element at index {index} is not a list: {type(item).__name__}")

def calculate_list_length(inner_list: ListElement) -> int:
    """
    Calculates the number of elements in a specific inner list.

    Args:
        inner_list: The inner list to measure.

    Returns:
        The length of the inner list as an integer.
    """
    return len(inner_list)

def find_max_length_and_element(input_list: List[ListElement]) -> ResultTuple:
    """
    Finds the maximum length among all inner lists and returns a tuple
    containing that maximum length and the corresponding inner list.

    Args:
        input_list: A validated list of lists.

    Returns:
        A tuple (max_length, list_with_max_length).
    """
    max_length: int = -1
    max_length_list: ListElement = []

    # Iterate through each inner list
    for inner_list in input_list:
        current_length: int = calculate_list_length(inner_list)

        # Check if the current list is longer than the max found so far
        if current_length > max_length:
            max_length = current_length
            max_length_list = inner_list

    # Return the result tuple
    return (max_length, max_length_list)

def max_length(input_data: Any) -> ResultTuple:
    """
    Public function to find the list of lists with maximum length.

    This function validates the input, checks for edge cases, and returns
    a tuple containing the maximum length found and the list that possesses
    that length.

    Args:
        input_data: Expected to be a list of lists of numbers.

    Returns:
        A tuple (max_length, longest_list).

    Raises:
        TypeError: If the input structure is invalid.
        ValueError: If the input list is empty.
    """
    # Step 1: Validate the input structure and types
    validate_list_of_lists(input_data)

    # Step 2: Calculate the maximum length and identify the corresponding list
    return find_max_length_and_element(input_data)