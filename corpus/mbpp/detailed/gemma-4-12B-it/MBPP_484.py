from typing import List, Tuple, Any

def remove_matching_tuple(
    input_list: List[Tuple[Any, ...]], 
    removal_list: List[Tuple[Any, ...]]
) -> List[Tuple[Any, ...]]:
    """
    Removes tuples from input_list if they are present in removal_list.

    The comparison is strictly based on the exact equality of the tuples.
    The function preserves the order of elements in input_list.

    Args:
        input_list: A list of tuples to filter.
        removal_list: A list of tuples that should be removed if they exist
                       in the input_list.

    Returns:
        A list of tuples from input_list that do not match any tuple in 
        removal_list.

    Raises:
        TypeError: If input_list or removal_list are not lists.
        AttributeError: If elements within the lists are not tuples.
    """
    # Validate that input_list and removal_list are actually lists
    if not isinstance(input_list, list):
        raise TypeError(f"Expected input_list to be a list, got {type(input_list).__name__}")

    if not isinstance(removal_list, list):
        raise TypeError(f"Expected removal_list to be a list, got {type(removal_list).__name__}")

    # Validate that all items in input_list are tuples
    for item in input_list:
        if not isinstance(item, tuple):
            raise AttributeError(f"Expected all items in input_list to be tuples, found {type(item).__name__}")

    # Validate that all items in removal_list are tuples
    for item in removal_list:
        if not isinstance(item, tuple):
            raise AttributeError(f"Expected all items in removal_list to be tuples, found {type(item).__name__}")

    # Convert removal_list to a set for O(1) average time complexity lookups.
    # Note: Tuples are hashable in Python if all their elements are hashable.
    # Since the problem implies standard string/data tuples, this is the standard approach.
    # If we encounter unhashable elements (like lists inside tuples), we would fall back to a list check.
    try:
        removal_set = set(removal_list)
    except TypeError:
        # Fallback for unhashable tuple elements (e.g., a tuple containing a list)
        # This ensures production-grade robustness against complex data types.
        removal_set = None

    def is_tuple_in_removal_list(target_tuple: Tuple[Any, ...]) -> bool:
        """Helper to check if a specific tuple exists in the removal criteria."""
        if removal_set is not None:
            return target_tuple in removal_set
        else:
            # O(N) check if hashability failed
            for item in removal_list:
                if item == target_tuple:
                    return True
            return False

    # Build the result list by iterating through the input list.
    # This ensures we preserve the original order and handle duplicates correctly.
    result_list = []

    for current_item in input_list:
        should_remove = is_tuple_in_removal_list(current_item)

        if not should_remove:
            result_list.append(current_item)

    return result_list

if __name__ == "__main__":
    # Verification of requirements
    assert remove_matching_tuple(
        [('Hello', 'dude'), ('How', 'are'), ('you', '?')], 
        [('Hello', 'dude'), ('How', 'are')]
    ) == [('you', '?')]

    assert remove_matching_tuple(
        [('Part', 'of'), ('the', 'journey'), ('is ', 'end')], 
        [('Journey', 'the'), ('is', 'end')]
    ) == [('Part', 'of'), ('the', 'journey'), ('is ', 'end')]

    assert remove_matching_tuple(
        [('Its', 'been'), ('a', 'long'), ('day', 'without')], 
        [('a', 'long'), ('my', 'friend')]
    ) == [('Its', 'been'), ('day', 'without')]