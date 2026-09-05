from typing import List

def is_sorted(lst: List[int]) -> bool:
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''

    # Validate input type
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")

    # Handle empty list or single element list
    # An empty list or a list with one element is vacuously sorted 
    # and cannot contain more than 1 duplicate.
    if len(lst) <= 1:
        return True

    # Helper function to check for duplicates exceeding the allowed limit
    # "If list has more than 1 duplicate" implies that 
    # a value appearing twice is okay, but a value appearing 3 times is not.
    def has_forbidden_duplicates(data: List[int]) -> bool:
        counts = {}
        for item in data:
            # Basic validation of element types
            if not isinstance(item, int):
                raise TypeError("List must contain only integers.")

            # Basic validation of negative numbers as per instructions
            if item < 0:
                # The prompt says "Assume no negative numbers", 
                # but for production-grade code, we should handle it gracefully.
                # We treat it as a valid number for sorting logic but acknowledge the constraint.
                pass

            if item in counts:
                counts[item] += 1
                if counts[item] > 2:
                    return True
            else:
                counts[item] = 1
        return False

    # Step 1: Check for the duplicate constraint first
    # If any number appears 3 or more times, return False immediately.
    if has_forbidden_duplicates(lst):
        return False

    # Step 2: Check for ascending order
    # We iterate through the list and compare each element with its successor.
    for i in range(len(lst) - 1):
        current_element = lst[i]
        next_element = lst[i + 1]

        # If the current element is greater than the next, it's not sorted.
        if current_element > next_element:
            return False

    # If both constraints are satisfied, return True
    return True