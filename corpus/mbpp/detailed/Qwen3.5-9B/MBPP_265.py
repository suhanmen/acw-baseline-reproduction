from typing import Any, List, Union

def _validate_list_input(data: Any, expected_type_name: str) -> List[Any]:
    """
    Validates that the input data is a list.
    Raises a TypeError if the input is not a list.
    """
    if not isinstance(data, list):
        raise TypeError(
            f"Input data must be a list, but got {type(data).__name__}. "
            f"Expected type: {expected_type_name}."
        )
    return data

def _validate_n_value(n: Any) -> int:
    """
    Validates that the step value 'n' is a positive integer.
    Raises a ValueError or TypeError if the validation fails.
    """
    # Check if it's an integer (excluding booleans which are subclass of int in Python)
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError(
            f"Step value 'n' must be an integer, but got {type(n).__name__}."
        )

    if n <= 0:
        raise ValueError(
            f"Step value 'n' must be a positive integer greater than 0, but got {n}."
        )

    return n

def _build_partition_result(
    data: List[Any], 
    n: int, 
    current_partition_index: int
) -> List[List[Any]]:
    """
    Helper function to build the final result structure.

    Logic:
    1. Initialize a result list with n empty sub-lists.
    2. Iterate through the data with its index.
    3. For each element, determine which sub-list it belongs to based on the index modulo n.
    4. Append the element to the correct sub-list.
    5. Return the populated list of lists.
    """
    # Create n empty partitions (sub-lists)
    partitions: List[List[Any]] = [None] * n

    # Fill each partition with the correct type
    for i in range(n):
        partitions[i] = []

    # Iterate over the data with indices
    # We use an explicit loop to demonstrate logic clearly rather than list comprehensions
    for index in range(len(data)):
        current_element = data[index]

        # Calculate the target partition index
        # The first element (index 0) goes to partition 0
        # The nth element (index n-1) goes to partition n-1
        # The (n+1)th element (index n) goes back to partition 0
        target_index = index % n

        # Append the element to the calculated partition
        partitions[target_index].append(current_element)

    return partitions

def list_split(data: Any, n: Any) -> List[List[Any]]:
    """
    Splits a list into n partitions based on the nth element rule.

    The function divides the input list into n separate lists by taking every nth element.
    - Index 0, n, 2n... go to the first list.
    - Index 1, n+1, 2n+1... go to the second list.
    - And so on until index n-1.

    Args:
        data: A list of elements to be split.
        n: A positive integer indicating the frequency of splitting.

    Returns:
        A list of n lists containing the split elements.

    Raises:
        TypeError: If data is not a list or n is not an integer.
        ValueError: If n is not positive (<= 0).
    """

    # Step 1: Validate the input data type
    validated_data = _validate_list_input(data, "list")

    # Step 2: Validate the step parameter
    validated_n = _validate_n_value(n)

    # Step 3: Handle the edge case where the input list is empty
    # If the list is empty, we still need to return n empty lists based on n
    if len(validated_data) == 0:
        return [[] for _ in range(validated_n)]

    # Step 4: Handle the edge case where n is 1
    # If n is 1, every element goes to the single partition, resulting in the original list
    if validated_n == 1:
        # We create a new list to ensure we don't mutate the input if that matters later,
        # though the logic of partitioning 1 way just returns the whole list.
        return [validated_data.copy()]

    # Step 5: Process the splitting logic using the helper function
    result = _build_partition_result(validated_data, validated_n, 0)

    # Note: The function _build_partition_result already initializes the structure correctly.
    # Even if the list is very long, the modulo arithmetic ensures correct distribution.

    return result