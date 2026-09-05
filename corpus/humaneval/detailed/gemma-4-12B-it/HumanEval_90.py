from typing import List, Optional, Set

def next_smallest(lst: List[int]) -> Optional[int]:
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.

    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    # 1. Validate input type
    if not isinstance(lst, list):
        raise TypeError("Input must be a list of integers.")

    # 2. Check for empty list or single-element list
    # While we can't have a 2nd smallest with < 2 elements, 
    # the logic below handles this, but explicit checking is safer.
    if len(lst) < 2:
        return None

    # 3. Verify all elements are integers
    for item in lst:
        if not isinstance(item, int):
            raise ValueError("All elements in the list must be integers.")

    # 4. Extract unique elements to handle cases like [1, 1, 2] 
    # or [1, 1]. The problem implies the "2nd smallest" refers to 
    # the value, not the index (as shown by the [1, 1] -> None example).
    unique_elements: Set[int] = set()
    for value in lst:
        unique_elements.add(value)

    # 5. Convert to a sorted list of unique values
    sorted_unique_values: List[int] = sorted(list(unique_elements))

    # 6. Check if we have at least two distinct values
    num_unique_elements = len(sorted_unique_values)

    if num_unique_elements < 2:
        # This handles the case where all elements are the same (e.g., [1, 1])
        # or where there is only one unique element.
        return None
    else:
        # The smallest is at index 0, the 2nd smallest is at index 1.
        second_smallest = sorted_unique_values[1]
        return second_smallest