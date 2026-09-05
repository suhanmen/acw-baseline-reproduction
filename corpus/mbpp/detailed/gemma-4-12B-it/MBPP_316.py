from typing import List

def find_last_occurrence(arr: List[int], target: int) -> int:
    """
    Finds the index of the last occurrence of a given target number in a list.

    Note: While the prompt mentions a 'sorted array', the provided test cases 
    contain unsorted elements (e.g., [2, 3, 5, 8, 6, 6, 8, 9, 9, 9] and 
    [2, 2, 1, 5, 6, 6, 6, 9, 9, 9]). 
    To satisfy all provided assertions, this implementation performs a 
    comprehensive linear search from right to left.

    Args:
        arr: A list of integers.
        target: The integer to search for.

    Returns:
        int: The index of the last occurrence of the target.

    Raises:
        ValueError: If the input array is empty.
        TypeError: If the input types are incorrect.
    """
    # --- Input Validation ---

    # Ensure the input is a list
    if not isinstance(arr, list):
        raise TypeError(f"Expected input 'arr' to be a list, but got {type(arr).__name__}")

    # Ensure the target is an integer
    if not isinstance(target, int):
        raise TypeError(f"Expected 'target' to be an integer, but got {type(target).__name__}")

    # Handle empty list edge case
    if len(arr) == 0:
        raise ValueError("The input list 'arr' cannot be empty.")

    # --- Search Logic ---

    # To find the LAST occurrence efficiently, we iterate backwards 
    # from the end of the list to the beginning.

    last_index_found: int = -1

    # We use a range that starts at the last index (len - 1) 
    # and goes down to 0 inclusive.
    for current_index in range(len(arr) - 1, -1, -1):
        current_element = arr[current_index]

        # Validate that the list contains only integers (defensive programming)
        if not isinstance(current_element, int):
            raise TypeError(f"List contains non-integer element at index {current_index}")

        # Check if the current element matches the target
        if current_element == target:
            # Because we are iterating backwards, the first match we find
            # is guaranteed to be the last occurrence in the list.
            last_index_found = current_index
            break

    return last_index_found

# The problem requires satisfying the following assertions:
# assert find_last_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 3
# assert find_last_occurrence([2, 3, 5, 8, 6, 6, 8, 9, 9, 9], 9) == 9
# assert find_last_occurrence([2, 2, 1, 5, 6, 6, 6, 9, 9, 9], 6) == 6