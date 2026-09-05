from typing import List, Optional, Union

Number = Union[int, float]

def validate_list_input(data: List[Number]) -> None:
    """
    Validates that the input is a list and contains only numeric types.
    Raises a TypeError if validation fails.
    """
    if not isinstance(data, list):
        raise TypeError(f"Input must be a list, but got {type(data).__name__}.")

    if not data:
        # An empty list is technically valid for returning an empty list of indices,
        # but we explicitly handle it here to ensure the logic path is clear.
        return

    for index, item in enumerate(data):
        if not isinstance(item, (int, float)):
            raise TypeError(
                f"Element at index {index} is not a number. "
                f"Found type: {type(item).__name__}"
            )


def find_minimum_value(data: List[Number]) -> Number:
    """
    Iterates through the data to find the single minimum numeric value.
    Returns the minimum value found.
    """
    current_minimum: Number = data[0]

    for i in range(1, len(data)):
        current_value: Number = data[i]

        if current_value < current_minimum:
            current_minimum = current_value

    return current_minimum


def find_indices_of_value(data: List[Number], target_value: Number) -> List[int]:
    """
    Iterates through the data and collects all indices where the element
    matches the target value exactly.
    """
    matching_indices: List[int] = []

    for i in range(len(data)):
        if data[i] == target_value:
            matching_indices.append(i)

    return matching_indices


def position_min(data: List[Number]) -> List[int]:
    """
    Finds all index positions of the minimum values in a given list.

    Args:
        data: A list of numeric values (int or float).

    Returns:
        A list of integer indices corresponding to the occurrences of the minimum value.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.

    Example:
        position_min([12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54])
        returns [3, 11]
    """
    # Step 1: Validate the input structure and contents
    validate_list_input(data)

    # Step 2: Handle the edge case where the list is empty
    if len(data) == 0:
        return []

    # Step 3: Determine the minimum value in the list
    min_value: Number = find_minimum_value(data)

    # Step 4: Find all indices where the minimum value occurs
    result_indices: List[int] = find_indices_of_value(data, min_value)

    return result_indices