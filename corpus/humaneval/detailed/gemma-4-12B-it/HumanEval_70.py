from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    # Step 1: Validate input type
    if not isinstance(lst, list):
        raise TypeError(f"Input must be a list, but got {type(lst).__name__}")

    # Step 2: Handle the empty list edge case
    if len(lst) == 0:
        return []

    # Step 3: Validate that all elements in the list are integers
    for index, item in enumerate(lst):
        if not isinstance(item, int):
            raise ValueError(f"All elements must be integers. Found {type(item).__name__} at index {index}.")

    # Step 4: Create a sorted copy of the list to manage elements easily.
    # We use a sorted list so that we can consistently pick the smallest 
    # available and largest available elements.
    sorted_elements = sorted(lst)

    # Step 5: Initialize the result list and pointers.
    # We use a two-pointer approach to pick elements from the sorted list.
    # 'left' points to the smallest remaining element.
    # 'right' points to the largest remaining element.
    result = []
    left_pointer = 0
    right_pointer = len(sorted_elements) - 1

    # We alternate between picking the minimum and the maximum.
    # The logic starts with the minimum.
    turn_is_minimum = True

    # Step 6: Populate the result list until pointers cross.
    while left_pointer <= right_pointer:
        if turn_is_minimum:
            # Pick the smallest available element
            result.append(sorted_elements[left_pointer])
            left_pointer += 1
        else:
            # Pick the largest available element
            result.append(sorted_elements[right_pointer])
            right_pointer -= 1

        # Toggle the turn for the next iteration
        turn_is_minimum = not turn_is_minimum

    return result