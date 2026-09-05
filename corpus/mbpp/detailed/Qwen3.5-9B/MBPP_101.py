from typing import List, Any, Optional, Union

Number = Union[int, float]

def _validate_index(k: int, array_length: int) -> None:
    """
    Validates that the index k is within the valid range for an array of given length.
    We use 0-based indexing for internal logic, but the problem's examples imply
    that k=1 refers to the smallest element, k=2 refers to the second smallest, etc.
    Therefore, valid k must be between 1 and array_length (inclusive).

    Arguments:
        k: The rank of the element to find (1-based).
        array_length: The number of elements in the input array.

    Raises:
        ValueError: If k is out of bounds (less than 1 or greater than array_length).
        TypeError: If k is not an integer.
    """
    # Check for type safety explicitly
    if not isinstance(k, int):
        raise TypeError(f"Argument 'k' must be an integer, got {type(k).__name__}")

    # Check logical bounds
    if k < 1 or k > array_length:
        raise ValueError(f"Argument 'k' ({k}) is out of bounds for an array of length {array_length}. "
                         f"Valid range is 1 to {array_length}.")

def _find_nth_smallest_element(data: List[Number], n: int) -> Number:
    """
    Finds the nth smallest element in a list of numbers using a stable sorting approach.
    While QuickSelect (O(n) average) is more efficient asymptotically, 
    full sorting (O(n log n)) is often clearer to read and less prone to implementation bugs
    for this specific problem statement where performance constraints aren't strictly defined.
    Given the requirement for "thorough, defensive, production-grade code" and "explicit control flow",
    implementing a robust, step-by-step sort with manual tracking of values is chosen here.

    This function handles the logic by:
    1. Creating a copy of the data to avoid modifying the original.
    2. Sorting the copy.
    3. Returning the element at the specific rank index.

    Arguments:
        data: The list of numbers to search.
        n: The 1-based rank of the element to retrieve.

    Returns:
        The nth smallest number.

    Raises:
        ValueError: If n is invalid relative to the length of 'data'.
    """
    # Calculate the length of the data provided
    length_of_data = len(data)

    # Re-validate n against the actual data length just in case, though _validate_index usually handles this first
    if n < 1 or n > length_of_data:
        raise ValueError(f"Rank {n} is invalid for a list of length {length_of_data}.")

    # Create a new list to store sorted values.
    # We do not modify the input list directly.
    sorted_values: List[Number] = list(data)

    # Perform a stable sort on the copy.
    # We use the built-in sort which is stable in Python.
    sorted_values.sort()

    # Calculate the 0-based index corresponding to the 1-based rank n.
    target_index = n - 1

    # Retrieve the value at the calculated index.
    result_value = sorted_values[target_index]

    return result_value

def kth_element(input_array: Any, k: Any, sort_key: Any = None) -> Number:
    """
    Finds the kth smallest element in a given list of numbers.

    This function serves as the main entry point. It performs strict input validation
    before delegating the sorting logic to the helper function.

    Parameters:
        input_array (List[Number]): The list of numbers to search within.
        k (int): The rank (1-based) of the element to find (e.g., 1 for smallest, 2 for second smallest).
        sort_key: Currently unused placeholder to maintain signature flexibility if needed later.
                   Ignored in current implementation.

    Returns:
        Number: The kth smallest element in the list.

    Raises:
        TypeError: If inputs are of incorrect types.
        ValueError: If the list is empty, k is out of bounds, or other logical errors occur.
    """

    # --- Step 1: Type and Value Validation for input_array ---
    # Check if input_array is None
    if input_array is None:
        raise ValueError("Input array cannot be None.")

    # Check if input_array is a list (or sequence)
    if not isinstance(input_array, list):
        raise TypeError(f"Expected input_array to be a list, got {type(input_array).__name__}.")

    # Check if the list is empty
    if len(input_array) == 0:
        raise ValueError("Input array cannot be empty.")

    # Validate that all elements in the array are numbers
    index_of_first_invalid_element = -1
    for i, element in enumerate(input_array):
        if not isinstance(element, (int, float)):
            index_of_first_invalid_element = i
            break

    if index_of_first_invalid_element != -1:
        raise TypeError(
            f"All elements in the array must be numbers (int or float). "
            f"Found {type(input_array[index_of_first_invalid_element]).__name__} at index {index_of_first_invalid_element}."
        )

    # --- Step 2: Validation for parameter k ---
    # Check if k is an integer
    if not isinstance(k, int):
        raise TypeError(f"Parameter 'k' must be an integer, received {type(k).__name__}.")

    # Note: We allow k to be a negative integer in the argument check here,
    # but the bounds check below will catch it. Python's int type includes negatives.

    # Get the length of the array for validation
    array_length = len(input_array)

    # Validate k bounds (1-based)
    _validate_index(k, array_length)

    # --- Step 3: Execution ---
    # Call the helper function to perform the actual search logic
    found_element = _find_nth_smallest_element(input_array, k)

    return found_element