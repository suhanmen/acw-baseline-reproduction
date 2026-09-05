from typing import List, Union

def sum_range_list(numbers: List[Union[int, float]], start_index: int, end_index: int) -> Union[int, float]:
    """
    Calculates the sum of numbers in a list between two specified indices, 
    inclusive of both the start and end indices.

    Args:
        numbers: A list of integers or floats.
        start_index: The starting index of the range.
        end_index: The ending index of the range (inclusive).

    Returns:
        The sum of the numbers within the range.

    Raises:
        ValueError: If input types are invalid or indices are out of bounds.
        TypeError: If the input list contains non-numeric elements.
    """
    # Step 1: Validate that the input list exists and is not empty
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list as input, but received {type(numbers).__name__}")

    if len(numbers) == 0:
        # Based on the problem description, if the list is empty, 
        # any range calculation is technically 0 or an error. 
        # We will return 0 for an empty list to be safe.
        return 0

    # Step 2: Validate index types
    if not isinstance(start_index, int) or not isinstance(end_index, int):
        raise TypeError("Indices must be integers.")

    # Step 3: Check for boundary conditions and logical errors in indices
    list_length = len(numbers)

    # Check if indices are within the valid bounds of the list
    if start_index < 0 or start_index >= list_length:
        raise ValueError(f"Start index {start_index} is out of bounds for list of length {list_length}")

    if end_index < 0 or end_index >= list_length:
        raise ValueError(f"End index {end_index} is out of bounds for list of length {list_length}")

    # Check if start_index is logically before end_index
    # The problem implies a range [start, end]. If start > end, the range is technically empty or invalid.
    if start_index > end_index:
        # Depending on interpretation, this could be 0 or an error. 
        # Given the assertions, we expect start <= end.
        raise ValueError(f"Start index ({start_index}) must be less than or equal to end index ({end_index})")

    # Step 4: Extract the sub-list for the specified range
    # Python slicing is [start:stop], where 'stop' is exclusive. 
    # Since the requirement is between indices (inclusive), we use end_index + 1.
    # We calculate the slice explicitly to ensure visibility.
    actual_start = start_index
    actual_end = end_index + 1

    sub_list = numbers[actual_start:actual_end]

    # Step 5: Validate that all elements in the range are numeric
    for item in sub_list:
        if not isinstance(item, (int, float)):
            raise TypeError(f"List contains non-numeric element: {item} (type: {type(item).__name__})")

    # Step 6: Calculate the sum
    total_sum = 0
    for value in sub_list:
        total_sum += value

    return total_sum

if __name__ == "__main__":
    # Assertions provided in the problem description
    assert sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 8, 10) == 29
    assert sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 5, 7) == 16
    assert sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 7, 10) == 38