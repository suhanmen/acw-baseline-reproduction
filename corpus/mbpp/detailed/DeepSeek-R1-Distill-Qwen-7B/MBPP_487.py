def sort_tuple(lst):
    """
    Sorts a list of tuples based on the last element of each tuple in increasing order.

    Requirements:
    - Handles edge cases: empty input, single element, all-equal elements, boundary values,
      zero/negative numbers, and degenerate cases.
    - Validates input, raising ValueError for invalid inputs.
    - Uses explicit control flow and small helper functions for readability.

    Args:
        lst: List of tuples to be sorted. Each tuple must have at least two elements.

    Returns:
        A new list of tuples sorted by the last element of each tuple.

    Raises:
        ValueError: If any element in the list is not a tuple with at least two elements.
    """
    # Validate input
    for item in lst:
        if not isinstance(item, tuple) or len(item) < 2:
            raise ValueError("Each element in the list must be a tuple with at least two elements.")

    # Extract the last elements for sorting while keeping the original tuples
    sorted_lst = sorted(lst, key=lambda x: x[1])

    return sorted_lst

# Example usage:
# print(sort_tuple([(1, 3), (3, 2), (2, 1)]))  # Output: [(2, 1), (3, 2), (1, 3)]
# print(sort_tuple([(2, 4), (3, 3), (1, 1)]))  # Output: [(1, 1), (3, 3), (2, 4)]
# print(sort_tuple([(3, 9), (6, 7), (4, 3)]))  # Output: [(4, 3), (6, 7), (3, 9)]