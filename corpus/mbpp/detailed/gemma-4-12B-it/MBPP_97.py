from typing import List, Dict, Any

def frequency_lists(nested_list: List[List[Any]]) -> Dict[Any, int]:
    """
    Calculates the frequency count of all elements within a list of lists.

    Args:
        nested_list (List[List[Any]]): A list containing multiple sub-lists of elements.

    Returns:
        Dict[Any, int]: A dictionary where keys are the unique elements found in all
                         sub-lists and values are their respective occurrence counts.

    Raises:
        TypeError: If the input is not a list or contains non-list elements (except at the bottom).
    """
    # 1. Validate input type
    if not isinstance(nested_list, list):
        raise TypeError(f"Input must be a list, but received {type(nested_list).__name__}")

    # Initialize the dictionary to store counts
    frequency_map: Dict[Any, int] = {}

    # 2. Handle edge case: Empty outer list
    if len(nested_list) == 0:
        return frequency_map

    # 3. Iterate through the outer list
    for sub_list in nested_list:
        # Validate that each inner element is indeed a list
        if not isinstance(sub_list, list):
            raise TypeError(
                f"Expected a list of lists. Found {type(sub_list).__name__} instead of list."
            )

        # 4. Iterate through each element in the sub-list
        for item in sub_list:
            # We check for hashability because dictionary keys must be hashable.
            # Standard integers and strings are hashable; lists are not.
            try:
                # If the item is already in the map, increment its count
                if item in frequency_map:
                    current_count = frequency_map[item]
                    frequency_map[item] = current_count + 1
                else:
                    # If it's a new item, initialize its count to 1
                    frequency_map[item] = 1
            except TypeError:
                # This happens if an item is unhashable (e.g., a list inside the list)
                raise TypeError(
                    f"List contains an unhashable element of type {type(item).__name__}. "
                    "All elements within sub-lists must be hashable (e.g., ints, strings)."
                )

    return frequency_map

# The following assertions verify the logic provided in the problem description.
if __name__ == "__main__":
    # Test Case 1
    result1 = frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])
    expected1 = {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
    assert result1 == expected1

    # Test Case 2
    result2 = frequency_lists([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    expected2 = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1}
    assert result2 == expected2

    # Test Case 3
    result3 = frequency_lists([[20, 30, 40, 17], [18, 16, 14, 13], [10, 20, 30, 40]])
    expected3 = {20: 2, 30: 2, 40: 2, 17: 1, 18: 1, 16: 1, 14: 1, 13: 1, 10: 1}
    assert result3 == expected3