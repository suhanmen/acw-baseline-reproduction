from typing import List, Any


def is_sublist(main_list: List[Any], sublist: List[Any]) -> bool:
    """
    Determines whether 'sublist' exists as a contiguous sequence within 'main_list'.

    Args:
        main_list: The list to be searched.
        sublist: The sequence to look for.

    Returns:
        bool: True if the sublist is found as a contiguous block, False otherwise.

    Raises:
        TypeError: If inputs are not lists.
    """
    # Validate inputs are of type list
    if not isinstance(main_list, list):
        raise TypeError(f"Expected main_list to be of type list, got {type(main_list).__name__}")
    if not isinstance(sublist, list):
        raise TypeError(f"Expected sublist to be of type list, got {type(sublist).__name__}")

    # Handle edge case: An empty sublist is technically a subset of any list.
    # In most standard definitions (like string find), an empty sequence is found at index 0.
    if len(sublist) == 0:
        return True

    # Handle edge case: If the sublist is longer than the main_list, 
    # it cannot be contained within it.
    main_length = len(main_list)
    sub_length = len(sublist)

    if sub_length > main_length:
        return False

    # Iterate through the main_list.
    # We only need to check up to the point where the remaining 
    # elements are at least as long as the sublist.
    # Range limit is: (total length) - (sublist length) + 1
    max_search_index = main_length - sub_length + 1

    for i in range(max_search_index):
        # Define the slice of the main_list to compare against the sublist.
        # We extract a segment of length 'sub_length' starting at index 'i'.
        current_slice = main_list[i : i + sub_length]

        # Check if the current slice matches the target sublist.
        # Since we are comparing lists, this checks for equality of elements 
        # and their order.
        if current_slice == sublist:
            # Match found, return True immediately.
            return True

    # If we have exhausted all possible starting positions and found no match.
    return False


if __name__ == "__main__":
    # Testing provided assertions
    assert is_sublist([2, 4, 3, 5, 7], [3, 7]) == False
    assert is_sublist([2, 4, 3, 5, 7], [4, 3]) == True
    assert is_sublist([2, 4, 3, 5, 7], [1, 6]) == False

    # Additional edge cases
    assert is_sublist([1, 2, 3], []) == True          # Empty sublist
    assert is_sublist([], [1]) == False               # Empty main list
    assert is_sublist([1, 1, 1], [1, 1]) == True      # Overlapping duplicates
    assert is_sublist([1, 2, 3], [1, 2, 3]) == True   # Exact match
    assert is_sublist([1, 2, 3], [4]) == False         # Non-existent element
    assert is_sublist([1, 2, 3], [1, 2, 3, 4]) == False # Sublist larger than main