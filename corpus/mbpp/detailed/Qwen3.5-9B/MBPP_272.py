from typing import List, Tuple, Any, Union

def _validate_input(records: Any) -> None:
    """
    Validates that the input is a list of tuples with exactly three elements each.

    Raises:
        TypeError: If the input is not a list or if any element is not a tuple.
        ValueError: If the list is empty or if any tuple does not have exactly three elements.
    """
    # Check if the input is a list
    if not isinstance(records, list):
        raise TypeError("Input must be a list of tuples.")

    # Check if the list is empty
    if len(records) == 0:
        raise ValueError("Input list cannot be empty.")

    # Iterate over each element in the list
    for index, record in enumerate(records):
        # Check if the current element is a tuple
        if not isinstance(record, tuple):
            raise TypeError(f"Element at index {index} is not a tuple.")

        # Check if the tuple has exactly three elements
        if len(record) != 3:
            raise ValueError(f"Tuple at index {index} must have exactly three elements.")

def _extract_last_element(record: Tuple[Any, Any, Any]) -> Any:
    """
    Extracts the last element (the third element) from a tuple of three elements.

    Args:
        record: A tuple containing exactly three elements.

    Returns:
        The third element of the tuple.
    """
    # Ensure we have the correct number of elements before accessing index 2
    if len(record) < 3:
        raise ValueError(f"Tuple must have at least three elements to extract the rear one.")

    return record[2]

def rear_extract(records: List[Tuple[Any, Any, Any]]) -> List[Any]:
    """
    Performs rear element extraction from a list of tuples records.

    This function extracts the last element from each tuple in the input list.
    Each tuple is expected to have exactly three elements, and the function 
    returns a list containing the third element of each tuple in the same order.

    Args:
        records: A list of tuples, where each tuple has exactly three elements.

    Returns:
        A list containing the third element from each tuple in the input list.

    Raises:
        TypeError: If the input is not a list or contains non-tuple elements.
        ValueError: If the input list is empty or contains tuples with incorrect sizes.
    """
    # Validate the input structure and contents
    _validate_input(records)

    # Initialize a list to hold the extracted rear elements
    extracted_elements: List[Any] = []

    # Iterate through each record in the validated list
    for record in records:
        # Extract the last element from the current record
        rear_element = _extract_last_element(record)
        # Append the extracted element to our result list
        extracted_elements.append(rear_element)

    # Return the list of extracted elements
    return extracted_elements