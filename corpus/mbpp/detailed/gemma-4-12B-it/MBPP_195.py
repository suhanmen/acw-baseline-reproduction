from typing import List, Union

def first(arr: List[int], target: int, length: int) -> int:
    """
    Finds the first position of an element in a sorted array.

    Note: The problem description mentions a "sorted array", but the 
    provided assertions include an unsorted array ([1,2,2,2,3,2,2,4,2]). 
    To satisfy all assertions, the function must perform a linear search 
    to find the first occurrence of the target value within the specified 
    length of the input list.

    Args:
        arr: A list of integers.
        target: The integer value to search for.
        length: The effective length of the array to consider.

    Returns:
        int: The 0-based index of the first occurrence of target.
        -1: If the target is not found within the specified length.

    Raises:
        ValueError: If the length provided is greater than the actual list size.
        TypeError: If inputs are not of the expected types.
    """
    # Input Validation: Type Checking
    if not isinstance(arr, list):
        raise TypeError(f"Expected 'arr' to be a list, got {type(arr).__name__}")

    if not isinstance(target, int):
        raise TypeError(f"Expected 'target' to be an integer, got {type(target).__name__}")

    if not isinstance(length, int):
        raise TypeError(f"Expected 'length' to be an integer, got {type(length).__name__}")

    # Input Validation: Boundary and Logic Checking
    actual_length = len(arr)
    if length < 0:
        raise ValueError("The provided 'length' must be a non-negative integer.")

    if length > actual_length:
        raise ValueError(
            f"Provided 'length' ({length}) exceeds the actual list size ({actual_length})."
        )

    # Handle degenerate case: empty search area
    if length == 0:
        return -1

    # Linear Search Implementation
    # We iterate through the list up to the specified 'length' index.
    # This handles sorted arrays, unsorted arrays (as per assertion 2), 
    # and duplicate elements correctly by returning the FIRST occurrence.

    current_index = 0
    found_index = -1

    while current_index < length:
        current_element = arr[current_index]

        if current_element == target:
            # Store the index and break immediately to ensure 
            # we only capture the FIRST occurrence.
            found_index = current_index
            break

        current_index += 1

    return found_index

# Validation against provided assertions
if __name__ == "__main__":
    # Assert 1: Sorted array with duplicates at the end
    # Expected: 5 (index of the first '6')
    assert first([1, 2, 3, 4, 5, 6, 6], 6, 7) == 5

    # Assert 2: Unsorted array (per requirements)
    # Expected: 1 (index of the first '2')
    # Note: The problem says "sorted array" but the test case is unsorted.
    # This implementation satisfies the assertion provided.
    assert first([1, 2, 2, 2, 3, 2, 2, 4, 2], 2, 9) == 1

    # Assert 3: Target at the start
    # Expected: 0
    assert first([1, 2, 3], 1, 3) == 0