from typing import List, Any, Tuple

def flip_prefix(sublist: List[Any]) -> None:
    """
    Reverses the elements of the given list in-place from the start to the end.

    Args:
        sublist (List[Any]): The list to be reversed in-place.

    Raises:
        ValueError: If the input is not a list.
        TypeError: If the input is empty or None.
    """
    if sublist is None:
        raise ValueError("Input must be a list, but None was provided.")

    if not isinstance(sublist, list):
        raise TypeError(f"Input must be a list, but got {type(sublist).__name__}")

    if len(sublist) == 0:
        raise ValueError("Cannot flip an empty list.")

    left_index = 0
    right_index = len(sublist) - 1

    while left_index < right_index:
        temp_value = sublist[left_index]
        sublist[left_index] = sublist[right_index]
        sublist[right_index] = temp_value
        left_index += 1
        right_index -= 1


def find_max_index(sublist: List[Any], limit_index: int) -> int:
    """
    Finds the index of the maximum value within the sublist up to a specific index.

    This function searches the slice from index 0 to limit_index (inclusive).

    Args:
        sublist (List[Any]): The list to search within.
        limit_index (int): The index up to which to search for the maximum value.

    Returns:
        int: The index of the maximum value found.

    Raises:
        ValueError: If the limit_index is out of bounds or if the list is empty.
        TypeError: If the list is not valid.
    """
    if sublist is None:
        raise ValueError("Input must be a list, but None was provided.")

    if not isinstance(sublist, list):
        raise TypeError(f"Input must be a list, but got {type(sublist).__name__}")

    if limit_index < 0 or limit_index >= len(sublist):
        raise ValueError(f"Limit index {limit_index} is out of bounds for list of length {len(sublist)}.")

    if len(sublist) == 0:
        raise ValueError("Cannot find max in an empty list.")

    if limit_index == 0:
        return 0

    max_value = sublist[0]
    max_index = 0

    current_index = 1
    while current_index <= limit_index:
        if sublist[current_index] > max_value:
            max_value = sublist[current_index]
            max_index = current_index
        current_index += 1

    return max_index


def perform_pancake_flip_at_index(target_index: int, full_list: List[Any]) -> None:
    """
    Performs a pancake flip to bring the element at target_index to the front (index 0).
    Then performs a second flip to move the element at index 0 to the end of the current sublist.
    Effectively, this moves the element currently at 'target_index' to the position 'len(sublist)-1'.

    In standard pancake sort, we usually:
    1. Find max at 'target_index'.
    2. Flip(0 to target_index) -> max moves to 0.
    3. Flip(0 to limit) -> max moves to limit.

    However, this function is designed to take a list, flip the prefix ending at target_index,
    and then flip the prefix ending at the full length of the list provided.
    Wait, the helper logic in the main loop is clearer if separated.
    Let's redefine this helper to just perform the specific flip operation needed for sorting.

    Actually, to keep it modular and clear, let's just implement the two-step logic inside the sort loop
    or create a specific helper for the "move to end" operation.

    Let's adjust: This function will flip the prefix [0..target_index] and then flip [0..len-1].
    But passing the whole list and indices is tricky for clarity.

    Let's revert to a simpler structure: We will find the max, flip it to 0, then flip it to the end.
    We will pass the current limit to the sort function or manage indices carefully.

    Revised Plan for this specific helper:
    It takes the list, the index of the max element, and the total length of the sublist we are considering.
    Step 1: Flip the prefix containing the max element (from index 0 to index_of_max).
    Step 2: Flip the prefix containing the max element (from index 0 to total_length-1).

    However, the problem requires explicit steps. Let's create a helper that does ONE flip.
    """
    if not isinstance(full_list, list):
        raise TypeError(f"Input must be a list, but got {type(full_list).__name__}")

    if len(full_list) == 0:
        raise ValueError("Cannot flip an empty list.")

    if target_index < 0 or target_index >= len(full_list):
        raise ValueError(f"Target index {target_index} is out of bounds.")

    # Flip 1: Bring max to index 0
    if target_index != 0:
        # We need to flip the prefix up to target_index.
        # The function 'flip_prefix' works on the whole list passed to it, but we can 
        # simulate slicing or pass the list and let the function handle internal indexing?
        # No, flip_prefix reverses the WHOLE list passed to it.
        # We need a more specific helper: reverse_list_from_index(start, end).
        # But flip_prefix currently reverses from 0 to len-1.
        # Let's change the approach: I will write a helper that reverses a specific range [start, end].
        pass

# Redefining helpers for precise range manipulation as per requirements.

def reverse_range(data: List[Any], start: int, end: int) -> None:
    """
    Reverses the sublist data[start:end+1] in-place.

    Args:
        data (List[Any]): The list to modify.
        start (int): The start index of the range (inclusive).
        end (int): The end index of the range (inclusive).
    """
    if not isinstance(data, list):
        raise TypeError(f"Input must be a list, but got {type(data).__name__}")

    if start < 0 or end < 0 or start > end or end >= len(data):
        raise ValueError("Invalid start or end index for the range.")

    left = start
    right = end

    while left < right:
        temp = data[left]
        data[left] = data[right]
        data[right] = temp
        left += 1
        right -= 1


def pancake_sort(array: List[Any]) -> List[Any]:
    """
    Sorts a list of elements using the pancake sorting algorithm.

    The algorithm works by repeatedly finding the largest unsorted element 
    and moving it to its correct position at the end of the unsorted portion
    using at most two flips:
    1. Flip the element to the front.
    2. Flip the element to the back of the unsorted portion.

    Args:
        array (List[Any]): A list of comparable elements to be sorted.

    Returns:
        List[Any]: A new list containing the sorted elements.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    """
    # Input Validation
    if array is None:
        raise ValueError("Input cannot be None.")

    if not isinstance(array, list):
        raise TypeError(f"Input must be a list, but got {type(array).__name__}")

    if len(array) == 0:
        raise ValueError("Input list cannot be empty.")

    # We work on a copy to ensure we don't modify the original list in-place
    # unless specified otherwise, but the return signature implies a new sorted list.
    # The problem asks for the result, so creating a copy is the safest and most functional approach.
    sorted_list = list(array)
    length = len(sorted_list)

    current_end_index = length - 1

    # Iterate from the end of the list down to the beginning
    while current_end_index > 0:
        # Step 1: Find the index of the maximum value in the unsorted portion (0 to current_end_index)
        max_index = 0
        max_value = sorted_list[0]

        search_index = 1
        while search_index <= current_end_index:
            if sorted_list[search_index] > max_value:
                max_value = sorted_list[search_index]
                max_index = search_index
            search_index += 1

        # Step 2: If the maximum element is already at the position we want (current_end_index), continue
        if max_index == current_end_index:
            current_end_index -= 1
            continue

        # Step 3: Flip the maximum element to the front of the list (index 0)
        # This requires reversing the range from 0 to max_index.
        # Only needed if max_index is not already 0.
        if max_index != 0:
            reverse_range(sorted_list, 0, max_index)

        # Step 4: Flip the maximum element to the correct position at the end (current_end_index)
        # This requires reversing the range from 0 to current_end_index.
        # Now the max element is at index 0, so we flip the entire unsorted section.
        reverse_range(sorted_list, 0, current_end_index)

        # Step 5: Move to the next unsorted element
        current_end_index -= 1

    return sorted_list