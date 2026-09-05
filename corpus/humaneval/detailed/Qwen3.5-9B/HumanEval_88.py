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

    # --- Input Validation ---

    # Validate that the input is a list (or tuple, converted to list)
    if not isinstance(array, (list, tuple)):
        raise TypeError(f"Expected a list or tuple, got {type(array).__name__}")

    # Validate that all elements are integers
    for index, element in enumerate(array):
        if not isinstance(element, int):
            raise TypeError(f"Expected integer at index {index}, got {type(element).__name__}")
        if element < 0:
            raise ValueError(f"Expected non-negative integer at index {index}, got {element}")

    # --- Helper Function: Get Boundary Sum ---

    def calculate_boundary_sum(sorted_elements: List[int]) -> int:
        """
        Calculates the sum of the first and last elements of the sorted array.
        For empty arrays or single element arrays, this is conceptually undefined
        by the problem statement's phrasing ("first index value, last index value"),
        but we must handle these edge cases where the array has fewer than 2 elements.
        In such cases, the sort order does not matter as there is only one unique order.
        """
        length = len(sorted_elements)
        if length == 0:
            return 0
        if length == 1:
            return 0  # No pair exists, sort order is trivial.

        first_value = sorted_elements[0]
        last_value = sorted_elements[-1]
        return first_value + last_value

    # --- Core Logic ---

    # 1. Create a copy of the input array to ensure we do not mutate the original.
    working_copy = list(array)

    # 2. Handle the edge case of an empty array immediately.
    if len(working_copy) == 0:
        return []

    # 3. Handle the edge case of a single-element array.
    # Sorting a single element list has no effect, but we proceed through the logic
    # to determine direction just in case, though the result is identical.
    if len(working_copy) == 1:
        return [working_copy[0]]

    # 4. Sort the array in ascending order first to establish the "first" and "last" values.
    # This is necessary because the problem implies looking at the boundaries of the set.
    working_copy.sort()

    # 5. Calculate the sum of the first and last values of this sorted sequence.
    boundary_sum_value = calculate_boundary_sum(working_copy)

    # 6. Determine the sort direction based on the parity of the sum.
    is_sum_odd = (boundary_sum_value % 2) != 0

    # 7. Perform the final sort.
    # Note: Since we already sorted ascending, we can simply reverse if descending is needed.
    # However, to be explicit and defensive, we will re-sort with the specified key.
    if is_sum_odd:
        # Sort Ascending
        final_sorted_array = sorted(working_copy)
    else:
        # Sort Descending
        final_sorted_array = sorted(working_copy, reverse=True)

    return final_sorted_array