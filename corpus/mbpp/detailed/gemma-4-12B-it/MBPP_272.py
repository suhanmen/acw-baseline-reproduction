from typing import List, Tuple, Any, Union

def rear_extract(records: List[Tuple[Any, ...]]) -> List[Any]:
    """
    Extracts the last element from each tuple in a list of tuples.

    Args:
        records (List[Tuple[Any, ...]]): A list of tuples where each tuple 
            contains multiple elements.

    Returns:
        List[Any]: A list containing only the last element of each input tuple.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If any element in the list is not a tuple or is an empty tuple.
    """
    # Validation: Ensure the input is a list
    if not isinstance(records, list):
        raise TypeError(f"Input must be a list, but received {type(records).__name__}")

    # Handle edge case: Empty list
    if len(records) == 0:
        return []

    extracted_elements: List[Any] = []

    for index, record in enumerate(records):
        # Validation: Ensure every record is a tuple
        if not isinstance(record, tuple):
            raise ValueError(
                f"Item at index {index} is not a tuple. "
                f"Received: {type(record).__name__}"
            )

        # Handle edge case: Empty tuple inside the list
        if len(record) == 0:
            raise ValueError(
                f"Tuple at index {index} is empty and has no rear element to extract."
            )

        # Logic: Access the last element of the tuple
        # Using negative indexing to specifically target the rear element
        rear_element = record[-1]

        # Append the extracted element to the result list
        extracted_elements.append(rear_element)

    return extracted_elements

# Verification against provided assertions
if __name__ == "__main__":
    # Test case 1
    result1 = rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)])
    assert result1 == [21, 20, 19]

    # Test case 2
    result2 = rear_extract([(1, 'Sai', 36), (2, 'Ayesha', 25), (3, 'Salman', 45)])
    assert result2 == [36, 25, 45]

    # Test case 3
    result3 = rear_extract([(1, 'Sudeep', 14), (2, 'Vandana', 36), (3, 'Dawood', 56)])
    assert result3 == [14, 36, 56]