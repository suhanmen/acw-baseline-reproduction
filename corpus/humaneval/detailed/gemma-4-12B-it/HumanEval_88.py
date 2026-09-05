from typing import List


def sort_array(array: List[int]) -> List[int]:
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    # 1. Validate input type
    if not isinstance(array, list):
        raise TypeError("Input must be a list of integers.")

    # 2. Handle the empty array edge case explicitly
    if len(array) == 0:
        return []

    # 3. Validate that all elements are non-negative integers
    for element in array:
        if not isinstance(element, int) or element < 0:
            raise ValueError("Array must contain only non-negative integers.")

    # 4. Create a deep copy of the array to satisfy the "don't change the given array" requirement
    # Using list() constructor for a shallow copy of integers (which are immutable)
    sorted_copy = list(array)

    # 5. Determine the sum of the first and last index values
    # For a single-element array, the first and last index are the same.
    first_element = sorted_copy[0]
    last_element = sorted_copy[-1]

    total_sum = first_element + last_element

    # 6. Determine the sorting order based on the parity of the sum
    # sum is odd -> ascending (True for reverse=False)
    # sum is even -> descending (True for reverse=True)
    is_sum_odd = (total_sum % 2 != 0)

    # Determine if we need to reverse. 
    # If sum is even, reverse is True. If sum is odd, reverse is False.
    should_reverse = not is_sum_odd

    # 7. Perform the sort
    # We use the built-in Timsort (sorted()), which is stable and efficient.
    # Since we want to return a new list, sorted() is ideal.
    if should_reverse:
        # Even sum case: Descending
        result = sorted(sorted_copy, reverse=True)
    else:
        # Odd sum case: Ascending
        result = sorted(sorted_copy, reverse=False)

    return result