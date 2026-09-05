from typing import List, Any

def count_element_in_list(list_of_lists: List[List[Any]], target_element: Any) -> int:
    """
    Counts the number of sublists within the given list that contain the target element.

    Parameters:
    list_of_lists (List[List[Any]]): A list containing other lists as elements.
    target_element (Any): The element to search for within the sublists.

    Returns:
    int: The count of sublists that contain the target element.

    Raises:
    TypeError: If list_of_lists is not a list or if any element in list_of_lists is not a list.
    ValueError: If list_of_lists is None.
    """
    # Validate the main input is not None
    if list_of_lists is None:
        raise ValueError("The input list_of_lists cannot be None.")

    # Validate the main input is a list
    if not isinstance(list_of_lists, list):
        raise TypeError(f"Expected list_of_lists to be a list, but got {type(list_of_lists).__name__}.")

    # Initialize the counter for sublists containing the target element
    count = 0

    # Validate each element in the main list is itself a list
    for item in list_of_lists:
        if not isinstance(item, list):
            raise TypeError(f"Expected all elements in list_of_lists to be lists, but found {type(item).__name__} at index of current iteration.")

        # Check if the current sublist contains the target element
        contains_target = False
        for element in item:
            if element == target_element:
                contains_target = True
                break

        # Increment the counter if the target was found in this sublist
        if contains_target:
            count += 1

    return count