import heapq
from typing import List, Tuple

def find_minimum_range(nums: List[List[int]]) -> Tuple[int, int]:
    """
    Finds the smallest range [start, end] that includes at least one 
    element from each of the provided lists of sorted integers.

    The "smallest" range is defined first by the difference (end - start),
    and then by the starting value if there is a tie in difference.
    """
    # --- Input Validation ---
    if not isinstance(nums, list) or not nums:
        raise ValueError("Input must be a non-empty list of lists.")

    for sublist in nums:
        if not isinstance(sublist, list):
            raise ValueError("Each element in the outer list must be a list.")
        if len(sublist) == 0:
            raise ValueError("Each inner list must contain at least one integer.")
        for item in sublist:
            if not isinstance(item, int):
                raise ValueError("All elements must be integers.")

    # Ensure the input lists are sorted (as per typical problem constraints)
    # We make a copy to avoid mutating the input lists.
    sorted_lists = [sorted(sublist) for sublist in nums]

    num_lists = len(sorted_lists)

    # --- Initialization ---
    # min_heap will store tuples of (value, list_index, element_index)
    # It helps us track the smallest value currently being considered across all lists.
    min_heap = []

    # current_max tracks the largest value among the elements 
    # currently pointed to in each list.
    current_max = float('-inf')

    # pointers[i] will store the current index we are looking at in sorted_lists[i]
    pointers = [0] * num_lists

    # Populate the heap with the first element of each list
    for i in range(num_lists):
        first_val = sorted_lists[i][0]
        heapq.heappush(min_heap, (first_val, i, 0))

        if first_val > current_max:
            current_max = first_val

    # Initialize the result with a very large range
    # (infinity, infinity) acts as the placeholder for the best range found.
    best_range_start = float('inf')
    best_range_end = float('inf')
    min_diff = float('inf')

    # --- Sliding Window Logic using Min-Heap ---
    # We keep track of a window where we have one element from each list.
    # The heap gives us the minimum value in our current "selection".
    # The current_max gives us the maximum value in our current "selection".
    while True:
        # Get the smallest value currently in our selection
        current_min, list_idx, element_idx = heapq.heappop(min_heap)

        # Calculate the difference of the current range
        current_diff = current_max - current_min

        # Update the best range if the current one is smaller
        if current_diff < min_diff:
            min_diff = current_diff
            best_range_start = current_min
            best_range_end = current_max
        elif current_diff == min_diff:
            # If differences are equal, the problem usually implies 
            # keeping the one with the smaller start value.
            if current_min < best_range_start:
                best_range_start = current_min
                best_range_end = current_max

        # Try to move the pointer of the list that had the minimum value
        # to the next element in that list.
        next_element_idx = element_idx + 1

        # If we reached the end of one list, we cannot form a range 
        # containing an element from every list anymore.
        if next_element_idx >= len(sorted_lists[list_idx]):
            break

        # Get the next value to add to the selection
        next_val = sorted_lists[list_idx][next_element_idx]

        # Push the new value into the heap
        heapq.heappush(min_heap, (next_val, list_idx, next_element_idx))

        # Update the current_max if the new value is larger
        if next_val > current_max:
            current_max = next_val

    return (int(best_range_start), int(best_range_end))