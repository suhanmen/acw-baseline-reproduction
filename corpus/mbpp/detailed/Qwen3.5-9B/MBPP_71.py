from typing import List, Any, Tuple


def _calculate_gap(n: int) -> int:
    """
    Calculate the initial gap for Comb Sort.

    The initial gap is set to n * 1.25.
    For the very first step, we take the floor of this value.
    If the resulting gap is less than 1, it defaults to 1.

    :param n: The current length of the list (or array) being sorted.
    :return: The gap value, which must be at least 1.
    """
    gap = n
    shrink_factor = 1.25

    while gap > 1:
        gap = int(gap / shrink_factor)

    return max(gap, 1)


def _swap_if_needed(arr: List[Any], index_a: int, index_b: int, 
                    arr_is_mutable: bool) -> bool:
    """
    Compare elements at two indices and swap them if they are in the wrong order.
    Returns True if a swap occurred, False otherwise.

    :param arr: The list being sorted.
    :param index_a: The first index to compare.
    :param index_b: The second index to compare.
    :param arr_is_mutable: A flag indicating if the list should be swapped.
                           (Used internally to support immutable-style views if needed, 
                            though we will modify in-place for standard Comb Sort).
    :return: Boolean indicating if a swap was performed.
    """
    if not arr:
        return False

    element_a = arr[index_a]
    element_b = arr[index_b]

    if element_a > element_b:
        # Perform the swap
        arr[index_a] = element_b
        arr[index_b] = element_a
        return True
    else:
        return False


def comb_sort(input_list: List[Any]) -> List[Any]:
    """
    Sorts a list of elements using the Comb Sort algorithm.

    Comb Sort is an improvement over Bubble Sort. It works by comparing elements
    separated by a large "gap", which is reduced in each iteration until it becomes 1.
    This helps to eliminate "turtles" (small values near the end of the list).

    Algorithm Steps:
    1. Initialize the gap to the length of the list.
    2. While the gap is greater than 1 or a swap occurred in the last pass:
       a. Reduce the gap by a factor of 1.25 (unless it's already 1).
       b. Traverse the list by indices separated by the current gap.
       c. Compare elements at these indices.
       d. Swap them if they are out of order.
       e. Keep track if any swap occurred.
    3. When the gap is 1, the algorithm behaves like Bubble Sort for the final refinement.

    :param input_list: A list of comparable elements to be sorted.
    :return: A new sorted list.

    :raises TypeError: If the input is not a list.
    :raises ValueError: If the input list is None (handled via type check) or contains incomparable items.
    """
    # Step 1: Input Validation

    # Check if input is None
    if input_list is None:
        raise TypeError("Input must be a list, but received None.")

    # Check if input is actually a list (or at least list-like, but we enforce strict list type per signature requirements usually)
    # The prompt asks for a function to sort a 'list'. We will enforce strict list typing.
    if not isinstance(input_list, list):
        raise TypeError(f"Input must be a list, but received {type(input_list).__name__}.")

    # We perform the sort in-place on a copy to return a new list, 
    # preserving the original if the caller does not want to mutate it.
    # However, standard comb sort implementations often sort in-place.
    # Given the requirement "Return ONLY one fenced code block" and standard functional expectations:
    # If the problem implies returning a sorted version, we return a new list.
    # If it implies sorting in-place, we would modify the input.
    # Let's create a copy to ensure immutability of the caller's list, which is safer.
    list_to_sort = list(input_list)

    n = len(list_to_sort)

    # Edge Case: Empty list
    if n == 0:
        return []

    # Edge Case: Single element
    if n == 1:
        return list_to_sort

    # Step 2: Initialize variables
    gap = _calculate_gap(n)
    swap_occurred = True

    # Step 3: Main Sorting Loop
    while swap_occurred or gap > 1:
        swap_occurred = False

        # Reduce gap if it is greater than 1
        if gap > 1:
            gap = int(gap / 1.25)
            # Ensure gap does not drop below 1 in the middle of the loop logic, 
            # though _calculate_gap usually ensures the start is >= 1.
            if gap < 1:
                gap = 1

        # Step 4: Traverse the list with the current gap
        i = 0
        # The loop runs while i + gap is within the bounds of the list
        while i + gap < n:
            index_a = i
            index_b = i + gap

            # Step 5: Compare and Swap
            # We use a temporary flag to see if this specific pass caused a swap
            # If element at index_a is greater than element at index_b, swap them.
            element_at_a = list_to_sort[index_a]
            element_at_b = list_to_sort[index_b]

            if element_at_a > element_at_b:
                # Swap
                list_to_sort[index_a] = element_at_b
                list_to_sort[index_b] = element_at_a
                swap_occurred = True

            # Move to the next pair
            i += 1

    # Step 6: Return the sorted list
    return list_to_sort