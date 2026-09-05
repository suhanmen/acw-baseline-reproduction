def _normalize_tuple_order(a_tuple):
    """
    Returns a sorted tuple version of the input tuple to handle order-insensitivity.
    Tuples in the input are guaranteed to be 2-element based on the problem context,
    but this function works for any tuple length.

    Example:
        Input: (5, 4)
        Output: (4, 5)
        Input: (3, 4)
        Output: (3, 4)
    """
    # Convert the input tuple to a list to make it sortable
    sorted_elements = sorted(list(a_tuple))
    # Convert the sorted list back into a tuple
    return tuple(sorted_elements)


def _is_exact_tuple_match(first_tuple, second_tuple):
    """
    Performs a strict equality check between two normalized tuples.

    This is required because two tuples might contain the same elements
    but in different orders (e.g., (4, 5) vs (5, 4)).
    After normalization, we can use standard equality.
    """
    return first_tuple == second_tuple


def _build_normalized_set(tuple_list):
    """
    Takes a list of tuples and returns a set of their normalized (sorted) versions.

    This allows us to easily find the intersection regardless of the original
    order of elements within the tuples.

    Args:
        tuple_list: A list of tuples (e.g., [(3, 4), (5, 6)])

    Returns:
        A set containing the normalized versions of the input tuples.
        Example: {(4, 3), (5, 6)} for input [(3, 4), (6, 5)]
    """
    normalized_set = set()

    # Validate that we are iterating over a list
    if not isinstance(tuple_list, list):
        raise TypeError(f"Expected a list of tuples, but got {type(tuple_list).__name__}")

    for item in tuple_list:
        # Validate that each item is a tuple
        if not isinstance(item, tuple):
            raise TypeError(f"Expected a tuple inside the list, but got {type(item).__name__} at index {tuple_list.index(item)}")

        # Normalize the tuple (sort its elements)
        normalized_item = _normalize_tuple_order(item)

        # Add to the set
        normalized_set.add(normalized_item)

    return normalized_set


def tuple_intersection(tuple_list_1, tuple_list_2):
    """
    Computes the intersection of two lists of tuples, where the order of elements 
    within each tuple is irrelevant.

    The problem states: "find the tuple intersection ... irrespective of their order".
    This implies that (4, 5) and (5, 4) are considered the same tuple.

    Args:
        tuple_list_1: First list of tuples.
        tuple_list_2: Second list of tuples.

    Returns:
        A set containing the unique tuples that exist in both input lists,
        where each tuple in the result is sorted.

    Raises:
        TypeError: If either argument is not a list, or if any element inside is not a tuple.

    Example:
        Input: 
            list1 = [(3, 4), (5, 6)]
            list2 = [(4, 3), (6, 5)]
        Output:
            {(3, 4), (5, 6)} 
            (Note: (4, 3) matches (3, 4) and (6, 5) matches (5, 6))
    """

    # Validate inputs are lists
    if not isinstance(tuple_list_1, list):
        raise TypeError(f"First argument must be a list of tuples, got {type(tuple_list_1).__name__}")

    if not isinstance(tuple_list_2, list):
        raise TypeError(f"Second argument must be a list of tuples, got {type(tuple_list_2).__name__}")

    # Handle empty input lists explicitly
    # An empty list cannot have a non-empty intersection
    if len(tuple_list_1) == 0 or len(tuple_list_2) == 0:
        return set()

    # Build normalized sets from both lists
    # Helper function call for clarity
    normalized_set_1 = _build_normalized_set(tuple_list_1)
    normalized_set_2 = _build_normalized_set(tuple_list_2)

    # Compute intersection
    # The intersection operation on sets is efficient and handles uniqueness automatically
    result_intersection = normalized_set_1.intersection(normalized_set_2)

    # Verify the result is a set (optional defensive check)
    if not isinstance(result_intersection, set):
        raise RuntimeError("Internal error: intersection result is not a set")

    return result_intersection