import copy

def _validate_array(input_list):
    """
    Validates that the input is a list (or tuple) of integers.
    Raises a TypeError if the input is not a sequence of integers.
    """
    if not isinstance(input_list, (list, tuple)):
        raise TypeError(f"Expected a list or tuple, but got {type(input_list).__name__}")

    for i, element in enumerate(input_list):
        if not isinstance(element, int):
            raise TypeError(f"Element at index {i} is not an integer: {type(element).__name__}")

def _validate_k(input_k, array_length):
    """
    Validates that k is a valid integer within the range [0, len(arr)].
    Raises a TypeError if k is not an integer.
    Raises a ValueError if k is out of range.
    """
    if not isinstance(input_k, int) or isinstance(input_k, bool):
        raise TypeError(f"Expected an integer for k, but got {type(input_k).__name__}")

    if not (0 <= input_k <= array_length):
        raise ValueError(f"k must be between 0 and {array_length} inclusive, but got {input_k}")

def _get_sorted_top_k(numeric_list, k_value):
    """
    Helper function to extract the top k elements from a list of numbers
    and return them sorted in ascending order.
    """
    if k_value == 0:
        return []

    # Create a copy to avoid modifying the original list
    working_list = copy.copy(numeric_list)

    # Sort the working list in descending order to easily pick the largest elements
    working_list.sort(reverse=True)

    # Extract the first k elements (the k largest)
    top_k_elements = working_list[:k_value]

    # Sort the extracted elements in ascending order for the final result
    top_k_elements.sort()

    return top_k_elements

def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """

    # Step 1: Validate the type and content of the input array
    _validate_array(arr)

    # Step 2: Determine the length of the validated array
    array_length = len(arr)

    # Step 3: Validate the input parameter k
    _validate_k(k, array_length)

    # Step 4: Retrieve the sorted top k elements
    result = _get_sorted_top_k(arr, k)

    # Step 5: Return the final result
    return result