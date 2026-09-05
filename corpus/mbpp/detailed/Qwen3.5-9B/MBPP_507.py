from typing import List, Any, Optional, Set

def _normalize_input_list(sequence: Any) -> Optional[List[Any]]:
    """
    Validates and normalizes the input list.

    - If the input is None, returns None (indicating invalid input).
    - If the input is not a list, returns None.
    - If the input is an empty list, returns an empty list.
    - Otherwise, returns a shallow copy of the list to avoid mutating the original.
    """
    if sequence is None:
        return None

    if not isinstance(sequence, list):
        return None

    # Return a copy to preserve immutability of the original input
    return list(sequence)

def _normalize_remove_set(words_to_remove: Any) -> Optional[Set[Any]]:
    """
    Validates and normalizes the list of words to remove.

    - If the input is None, returns None (indicating invalid input).
    - If the input is not a list, returns None.
    - If the input is an empty list, returns an empty set (which is safe for filtering).
    - Otherwise, returns a set containing the elements of the list for O(1) lookup.
    """
    if words_to_remove is None:
        return None

    if not isinstance(words_to_remove, list):
        return None

    # Convert to a set for efficient membership testing
    return set(words_to_remove)

def _filter_elements(source: List[Any], elements_to_remove: Set[Any]) -> List[Any]:
    """
    Filters out elements from the source list that exist in the elements_to_remove set.

    - Preserves the original order of elements.
    - Handles duplicate values in the source list correctly (removes all instances of matching values).
    """
    result: List[Any] = []

    # Explicitly iterate through the source list
    for current_element in source:
        # Check if the current element is NOT in the removal set
        if current_element not in elements_to_remove:
            # Append to the result list if the condition is met
            result.append(current_element)

    return result

def remove_words(list_of_words: Any, words_to_remove: Any) -> Optional[List[Any]]:
    """
    Removes specific words from a given list.

    Parameters:
        list_of_words: The original list of words to filter.
        words_to_remove: The list of words to remove from the original list.

    Returns:
        A new list with the specified words removed.
        Returns None if either input is invalid.

    Edge Cases Handled:
        - None inputs: Returns None.
        - Non-list inputs: Returns None.
        - Empty list_of_words: Returns an empty list.
        - Empty words_to_remove: Returns a copy of the original list (no removal).
        - Single element lists: Correctly handles presence or absence of the element.
        - Duplicate words in source or removal list: Handles correctly.
        - Mixed types: Uses equality comparison, preserving types as long as they match.
    """

    # Step 1: Validate and normalize the input list
    normalized_source: Optional[List[Any]] = _normalize_input_list(list_of_words)
    if normalized_source is None:
        return None

    # Step 2: Validate and normalize the list of words to remove
    normalized_removal_set: Optional[Set[Any]] = _normalize_remove_set(words_to_remove)
    if normalized_removal_set is None:
        return None

    # Step 3: Perform the filtering operation
    filtered_result: List[Any] = _filter_elements(normalized_source, normalized_removal_set)

    # Step 4: Return the final result
    return filtered_result