from typing import List

def move_one_ball(arr: List[int]) -> bool:
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.

    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:

    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.

    """
    # --- Input Validation and Edge Case Handling ---

    # Ensure the input is actually a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers.")

    # Handle empty list case as specified
    if len(arr) == 0:
        return True

    # Handle single element list (it is inherently sorted)
    if len(arr) == 1:
        return True

    # --- Logic ---

    # A right-shifted version of a sorted unique list will have a specific property:
    # There can be at most one place where the value decreases (where arr[i] > arr[i+1]).
    # If there is exactly one such "drop", the "drop" point represents the 
    # point where the original end of the sorted list was wrapped around to the start.

    # For example, in [3, 4, 5, 1, 2]:
    # 3 < 4 (True)
    # 4 < 5 (True)
    # 5 < 1 (False) -> Drop found here!
    # 1 < 2 (True)
    # There is exactly one drop.

    drop_count = 0
    drop_index = -1

    # Iterate through the list to find points where the non-decreasing order is violated.
    for i in range(len(arr) - 1):
        current_element = arr[i]
        next_element = arr[i + 1]

        if current_element > next_element:
            drop_count += 1
            drop_index = i

    # If there are no drops, the array is already sorted.
    if drop_count == 0:
        return True

    # If there is more than one drop, it is impossible to sort via rotation.
    if drop_count > 1:
        return False

    # If there is exactly one drop, we must check if the "wrap-around" logic holds.
    # The last element of the array must be smaller than the first element of the array
    # (because it was shifted from the end to the front).
    # And the element at the wrap-around point (index drop_index + 1) 
    # must be the smallest element, and the element at index 0 must be 
    # the "successor" of the end.

    # More simply: in a valid rotated sorted array with exactly one drop:
    # The last element must be less than or equal to the first element.
    # Because the array is unique, it must be strictly less than.
    first_element = arr[0]
    last_element = arr[-1]

    if last_element < first_element:
        # Final check: since we confirmed only one drop exists and the last
        # element is smaller than the first, we check if the segment from
        # the drop to the end, followed by the segment from the start to
        # the drop, is sorted.

        # However, the drop_count == 1 and last < first check is 
        # mathematically sufficient for unique elements.
        return True
    else:
        # This case handles if there's a drop but the wrap-around isn't valid.
        return False