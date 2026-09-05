from typing import List, Any

def remove_elements(main_list: List[Any], to_remove_list: List[Any]) -> List[Any]:
    """
    Removes all elements from the first list that are present in the second list.

    The function preserves the original order of elements in the main_list 
    that are not in the to_remove_list. It handles duplicates in the main_list 
    by removing every instance of an element found in the to_remove_list.

    Args:
        main_list: The original list of elements.
        to_remove_list: A list of elements to be excluded from the result.

    Returns:
        A new list containing only the elements from main_list that were 
        not present in to_remove_list.

    Raises:
        TypeError: If either input is not a list.
    """
    # Validate input types
    if not isinstance(main_list, list):
        raise TypeError(f"Expected main_list to be a list, got {type(main_list).__name__}")
    if not isinstance(to_remove_list, list):
        raise TypeError(f"Expected to_remove_list to be a list, got {type(to_remove_list).__name__}")

    # Handle degenerate cases: if main_list is empty, return empty list
    if not main_list:
        return []

    # Handle degenerate cases: if to_remove_list is empty, return a copy of main_list
    if not to_remove_list:
        return list(main_list)

    # Optimization: Convert to_remove_list to a set for O(1) average time complexity lookups.
    # This ensures that the removal operation is efficient even for large input lists.
    # We use a set because duplicates in to_remove_list do not change the logic.
    elements_to_exclude = set()
    for item in to_remove_list:
        elements_to_exclude.add(item)

    # Initialize the result list
    result_list = []

    # Iterate through the main list and filter out excluded elements
    # We use a standard loop to ensure the original order is preserved
    # and to make the logic explicit.
    for current_element in main_list:
        # Check if the current element exists in the exclusion set
        is_excluded = current_element in elements_to_exclude

        if not is_excluded:
            # If not excluded, append it to our result collection
            result_list.append(current_element)

    return result_list

if __name__ == "__main__":
    # Assertions provided in the problem description
    assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
    assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7]) == [2, 4, 6, 8, 9, 10]
    assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 7]) == [1, 2, 3, 4, 6, 8, 9, 10]