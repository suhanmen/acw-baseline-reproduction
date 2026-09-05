from typing import List, Any, Union, Tuple

def _validate_nested_list(
    input_data: List[List[Any]]
) -> Tuple[bool, Union[str, None]]:
    """
    Validates that the input is a non-empty list of lists with uniform inner length.

    Returns:
        A tuple (is_valid, error_message).
        If valid, error_message is None.
        If invalid, error_message describes the issue.
    """
    # Check if the main list is None
    if input_data is None:
        return False, "Input cannot be None."

    # Check if the main list is empty
    if len(input_data) == 0:
        return False, "The outer list must contain at least one inner list."

    # Check if the first element is itself a list
    if not isinstance(input_data[0], list):
        return False, "All elements in the outer list must be lists."

    # Check if all elements in the outer list are lists
    for index, item in enumerate(input_data):
        if not isinstance(item, list):
            return False, f"Element at index {index} is not a list."

    # Check if the first list is empty (which implies all must be empty for uniformity)
    if len(input_data[0]) == 0:
        # If the first list is empty, all subsequent lists must also be empty to be uniform
        for index, item in enumerate(input_data):
            if len(item) != 0:
                return False, f"Inner list at index {index} is not empty, but the first list is empty."
        return True, None

    # Determine the expected length based on the first non-empty list found so far
    # Since we checked the first one above, we use its length as the standard
    expected_length = len(input_data[0])

    # Validate length of every inner list matches the expected length
    for index, item in enumerate(input_data):
        if len(item) != expected_length:
            return False, f"Inner list at index {index} has length {len(item)}, expected {expected_length}."

    return True, None


def _validate_index(
    index: int,
    number_of_rows: int
) -> Tuple[bool, Union[str, None]]:
    """
    Validates that the specified index is an integer within valid bounds.

    Returns:
        A tuple (is_valid, error_message).
    """
    # Check type
    if not isinstance(index, int):
        return False, "The specified index must be an integer."

    # Check bounds (negative and positive)
    if index < 0 or index >= number_of_rows:
        return False, f"Index {index} is out of range for a list with {number_of_rows} rows."

    return True, None


def _extract_elements(
    rows: List[List[Any]],
    column_index: int
) -> List[Any]:
    """
    Extracts elements from the specified column index in each row.

    Args:
        rows: The validated 2D list.
        column_index: The column index to extract from each row.

    Returns:
        A list containing the elements at the specified column index.
    """
    extracted_values: List[Any] = []

    for row in rows:
        # Safety check (should be redundant due to prior validation, but good for defense)
        if len(row) <= column_index:
            raise ValueError(
                f"Column index {column_index} exceeds the length of row with index {rows.index(row)}."
            )
        extracted_values.append(row[column_index])

    return extracted_values


def specified_element(
    nested_list: List[List[Any]],
    index: int
) -> List[Any]:
    """
    Extracts every first or specified element from a given two-dimensional list.

    This function validates the input structure and indices to ensure robustness
    against malformed data, empty inputs, or out-of-bounds indices.

    Args:
        nested_list: A two-dimensional list (list of lists).
        index: The integer index of the column to extract from each row.

    Returns:
        A list containing the elements from the specified column index for each row.

    Raises:
        ValueError: If the input data or index is invalid.
        TypeError: If the types of the arguments are incorrect.
    """
    # Step 1: Type checking for the main arguments
    if not isinstance(nested_list, list):
        raise TypeError("The 'nested_list' argument must be a list.")

    if not isinstance(index, int):
        raise TypeError("The 'index' argument must be an integer.")

    # Step 2: Validate the structure of the nested list
    is_valid_structure, error_message = _validate_nested_list(nested_list)
    if not is_valid_structure:
        raise ValueError(f"Invalid nested list structure: {error_message}")

    # Step 3: Determine the number of rows
    number_of_rows: int = len(nested_list)

    # Step 4: Validate the index
    is_valid_index, error_message = _validate_index(index, number_of_rows)
    if not is_valid_index:
        raise ValueError(f"Invalid index provided: {error_message}")

    # Step 5: Perform the extraction
    result_list: List[Any] = _extract_elements(nested_list, index)

    return result_list