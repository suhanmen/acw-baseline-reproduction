from typing import List, Any


def remove_empty(input_list: List[Any]) -> List[Any]:
    """
    Removes all empty list objects from a given list of items.

    This function iterates through the input list and preserves all elements 
    that are either not lists, or are lists containing at least one element.

    Args:
        input_list (List[Any]): A list containing various items, including empty lists.

    Returns:
        List[Any]: A new list with empty lists removed.

    Raises:
        TypeError: If the input provided is not a list.
    """
    # Defensive check: Validate that the input is indeed a list.
    if not isinstance(input_list, list):
        raise TypeError(f"Expected input of type 'list', but received '{type(input_list).__name__}'.")

    # Handle the edge case of an empty input list immediately.
    if len(input_list) == 0:
        return []

    # We will build a new list to store the filtered results.
    # This avoids mutating the original list during iteration.
    filtered_result: List[Any] = []

    for item in input_list:
        # We need to identify if an item is an empty list [].
        # A common pitfall is using 'if not item:', which would also remove:
        # 0 (integer), False (boolean), or "" (empty string).
        # We must explicitly check for the type 'list' AND the length.

        is_list_type = isinstance(item, list)

        if is_list_type:
            # Check the length of the list.
            list_length = len(item)

            if list_length > 0:
                # The list is not empty, so we keep it.
                filtered_result.append(item)
            else:
                # The list is empty [], so we ignore it (do not append).
                pass
        else:
            # The item is not a list at all (e.g., a string, integer, etc.).
            # According to the requirements, these should be preserved.
            filtered_result.append(item)

    return filtered_result


# Test cases to verify the implementation
if __name__ == "__main__":
    # Test Case 1: Standard mix of empty lists and strings/populated lists
    case_1 = [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
    expected_1 = ['Red', 'Green', [1, 2], 'Blue']
    assert remove_empty(case_1) == expected_1

    # Test Case 2: Multiple empty lists at the start
    case_2 = [[], [], [], [], [], 'Green', [1, 2], 'Blue', [], []]
    expected_2 = ['Green', [1, 2], 'Blue']
    assert remove_empty(case_2) == expected_2

    # Test Case 3: Longer sequence with mixed types
    case_3 = [[], [], [], 'Python', [], [], 'programming', 'language', [], [], [], [], []]
    expected_3 = ['Python', 'programming', 'language']
    assert remove_empty(case_3) == expected_3

    # Edge Case: Empty input
    assert remove_empty([]) == []

    # Edge Case: All empty lists
    assert remove_empty([[], [], []]) == []

    # Edge Case: No empty lists
    assert remove_empty(['A', 'B', [1]]) == ['A', 'B', [1]]

    # Edge Case: Falsy values that are NOT empty lists (should be kept)
    # This ensures the logic doesn't accidentally remove 0, False, or ""
    case_4 = [[], 0, False, "", [1], None]
    expected_4 = [0, False, "", [1], None]
    assert remove_empty(case_4) == expected_4