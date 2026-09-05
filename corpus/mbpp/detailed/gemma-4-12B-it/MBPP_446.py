from typing import List, Tuple, Any, Dict

def count_Occurrence(input_tuple: Tuple[Any, ...], target_list: List[Any]) -> int:
    """
    Counts the total occurrences of all elements present in the target_list
    within the given input_tuple.

    Args:
        input_tuple: A tuple of elements to search through.
        target_list: A list of specific elements whose occurrences should be counted.

    Returns:
        int: The sum of occurrences of the elements from target_list found in input_tuple.

    Raises:
        TypeError: If input_tuple is not a tuple or target_list is not a list.
    """
    # Input Validation: Ensure input_tuple is actually a tuple
    if not isinstance(input_tuple, tuple):
        raise TypeError(f"Expected input_tuple to be of type tuple, got {type(input_tuple).__name__}")

    # Input Validation: Ensure target_list is actually a list
    if not isinstance(target_list, list):
        raise TypeError(f"Expected target_list to be of type list, got {type(target_list).__name__}")

    # Edge Case: If the tuple is empty, the count is always 0
    if len(input_tuple) == 0:
        return 0

    # Edge Case: If the target_list is empty, the count is always 0
    if len(target_list) == 0:
        return 0

    # Step 1: Convert the target_list into a set for O(1) lookup efficiency.
    # Using a set also handles cases where the target_list might have duplicates,
    # ensuring we only count occurrences of unique items requested.
    unique_targets = set(target_list)

    # Step 2: Create a frequency map for all elements in the input_tuple.
    # This avoids nested loops (O(N*M)) and achieves O(N+M) complexity.
    occurrence_map: Dict[Any, int] = {}
    for item in input_tuple:
        if item in occurrence_map:
            occurrence_map[item] = occurrence_map[item] + 1
        else:
            occurrence_map[item] = 1

    # Step 3: Accumulate the counts of elements that are present in the unique_targets set.
    total_count = 0
    for target_item in unique_targets:
        # Check if the target exists in our frequency map
        if target_item in occurrence_map:
            count_for_item = occurrence_map[target_item]
            total_count += count_for_item

    return total_count

if __name__ == "__main__":
    # These assertions verify the requirements provided in the prompt.
    assert count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b']) == 3
    assert count_Occurrence((1, 2, 3, 1, 4, 6, 7, 1, 4), [1, 4, 7]) == 6
    assert count_Occurrence((1, 2, 3, 4, 5, 6), [1, 2]) == 2