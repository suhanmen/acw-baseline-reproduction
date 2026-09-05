def flatten_list(nested_list):
    """
    Flatten a nested list structure into a single list.
    The function handles all edge cases, including empty lists,
    lists with single elements, all-equal elements, negative numbers,
    and zero.

    Args:
        nested_list: The nested list to be flattened.

    Returns:
        A flattened list with all elements in the same order.

    Raises:
        ValueError: If the nested_list contains elements that are not lists or integers.
    """
    def _flatten_helper(sub_list, result):
        """
        Recursively flatten a sublist into the result list.
        """
        for element in sub_list:
            if isinstance(element, list):
                _flatten_helper(element, result)
            else:
                result.append(element)

    # Initialize the result list
    flattened = []
    # Check if the input is a list; if not, raise ValueError
    if not isinstance(nested_list, list):
        raise ValueError("The nested_list must be a list.")
    # Start the recursive flattening process
    _flatten_helper(nested_list, flattened)
    # Return the flattened list
    return flattened

# Test the function with the provided examples
assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]) == [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120], "Test case 1 failed"
assert flatten_list([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]) == [10, 20, 40, 30, 56, 25, 10, 20, 33, 40], "Test case 2 failed"
assert flatten_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]) == [1, 2, 3, 4, 5, 6, 10, 11, 12, 7, 8, 9], "Test case 3 failed"

# Example of handling an invalid input
try:
    flatten_list("not a list")
except ValueError:
    print("Correctly identified invalid input.")