from typing import List, Any, Union


def flatten_list(nested_list: List[Any]) -> List[Any]:
    """
    Flattens a nested list structure into a single-dimensional list.

    The function handles arbitrarily deep nesting. It supports integers,
    floats, and other non-iterable types (except strings/bytes, which
    are treated as atoms in this context to avoid infinite recursion on
    single characters).

    Args:
        nested_list (List[Any]): A list containing elements which may be 
                                  integers, floats, or other lists.

    Returns:
        List[Any]: A flattened list containing all non-list elements.

    Raises:
        TypeError: If the input provided is not a list.
    """
    # Input validation: Ensure the top-level input is a list
    if not isinstance(nested_list, list):
        raise TypeError(f"Input must be a list, received {type(nested_list).__name__}")

    # We use a result list to collect all flattened elements.
    # Using a list and appending ensures we maintain the original order.
    flattened_result: List[Any] = []

    def recursive_flatten(current_item: Any) -> None:
        """
        Helper function to recursively traverse the nested structure.
        """
        # Check if the current item is a list.
        # We explicitly check for 'list' type. We do not treat strings 
        # or bytes as iterables to be flattened to avoid infinite recursion 
        # on single characters.
        if isinstance(current_item, list):
            # Iterate through every element in the nested list.
            for element in current_item:
                # Recursively call the helper for every element.
                recursive_flatten(element)
        else:
            # If the item is not a list, it is an atom (int, float, etc.)
            # Append it to the final result list.
            flattened_result.append(current_item)

    # Start the recursive process.
    # We iterate through the top-level list provided by the user.
    for item in nested_list:
        recursive_flatten(item)

    return flattened_result


if __name__ == "__main__":
    # The following assertions validate the requirements provided in the prompt.

    # Test Case 1: Mixed nesting depths and types
    input1 = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
    expected1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    assert flatten_list(input1) == expected1

    # Test Case 2: Multiple lists with varying lengths and duplicates
    input2 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    expected2 = [10, 20, 40, 30, 56, 25, 10, 20, 33, 40]
    assert flatten_list(input2) == expected2

    # Test Case 3: Lists of lists of uniform length
    input3 = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
    expected3 = [1, 2, 3, 4, 5, 6, 10, 11, 12, 7, 8, 9]
    assert flatten_list(input3) == expected3

    # Edge Case: Empty list
    assert flatten_list([]) == []

    # Edge Case: Deeply nested single elements
    assert flatten_list([[[[1]]]]) == [1]

    # Edge Case: List containing empty lists
    assert flatten_list([[], [[]], []]) == []

    # Edge Case: List with non-integer types (e.g., floats)
    assert flatten_list([1.5, [2.5, [3.5]]]) == [1.5, 2.5, 3.5]