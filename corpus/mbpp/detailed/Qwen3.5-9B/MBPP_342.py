from typing import List, Tuple, Optional
import heapq

def _validate_inputs(arrays: List[List[int]]) -> None:
    """
    Validate the input list of arrays.

    Rules:
    - Must not be None.
    - Must not be an empty list (no arrays at all).
    - Each element must be a list.
    - Each inner list must not be empty.
    - Each inner list must contain only integers.
    - No duplicate references to the same list object (optional strictness, 
      though typically not an issue for immutable data, we check type safety).

    Raises:
        TypeError: If types are incorrect.
        ValueError: If structural constraints are violated.
    """
    if arrays is None:
        raise TypeError("Input 'arrays' must be a list, not None.")

    if not isinstance(arrays, list):
        raise TypeError(f"Expected 'arrays' to be a list, got {type(arrays).__name__}.")

    if len(arrays) == 0:
        raise ValueError("Input list 'arrays' cannot be empty; it must contain at least one non-empty array.")

    for index, sub_array in enumerate(arrays):
        if sub_array is None:
            raise TypeError(f"Element at index {index} is None, expected a list of integers.")

        if not isinstance(sub_array, list):
            raise TypeError(f"Element at index {index} is not a list: {type(sub_array).__name__}.")

        if len(sub_array) == 0:
            raise ValueError(f"Array at index {index} is empty. It must contain at least one integer.")

        for value_idx, value in enumerate(sub_array):
            if not isinstance(value, int):
                raise TypeError(
                    f"Array at index {index}, element at sub-index {value_idx} is not an integer: {type(value).__name__}. "
                    f"Expected int, found {type(value).__name__}."
                )


def _merge_and_heapify(arrays: List[List[int]]) -> Optional[heapq._HeapItem]:
    """
    Merge the first element of each array into a min-heap.

    The heap will store tuples of the form: (value, array_index, element_index).
    This allows us to efficiently retrieve the smallest current value across all arrays.

    Returns:
        A tuple containing (min_value, array_index, element_index) for the smallest element,
        or None if no elements exist (should not happen if validation passes).
    """
    min_heap: List[Tuple[int, int, int]] = []

    # We expect 'arrays' to be non-empty and validated, so this loop will run at least once.
    for array_idx, sub_array in enumerate(arrays):
        # Since validation ensures non-empty lists, we can safely access index 0.
        first_value = sub_array[0]
        element_idx = 0

        # Push (value, array_index, element_index) onto the heap
        # We use array_index and element_index to reconstruct the next element.
        heapq.heappush(min_heap, (first_value, array_idx, element_idx))

    # Since all arrays were validated to be non-empty, min_heap cannot be empty here.
    if len(min_heap) == 0:
        return None

    # Return the root of the heap
    return min_heap[0]


def _find_next_element(
    arrays: List[List[int]], 
    current_array_idx: int, 
    current_element_idx: int
) -> Optional[int]:
    """
    Retrieve the next element from the specified array after the current index.

    Args:
        arrays: The list of input arrays.
        current_array_idx: The index of the array in the 'arrays' list.
        current_element_idx: The index of the current element in that array.

    Returns:
        The next integer value in the array, or None if the end of the array is reached.
    """
    sub_array = arrays[current_array_idx]
    next_idx = current_element_idx + 1

    if next_idx < len(sub_array):
        return sub_array[next_idx]
    else:
        return None


def find_minimum_range(arrays: List[List[int]]) -> Tuple[int, int]:
    """
    Find the smallest range that includes at least one element from each of the given arrays.

    The function uses a min-heap to maintain the current smallest element from each array.
    It expands the range by moving the pointer of the array that contributes the minimum
    element to the next element in that array, effectively shrinking the window from the
    left while expanding to the right implicitly by including larger values.

    Algorithm Steps:
    1. Validate inputs to ensure correctness and safety.
    2. Initialize a min-heap with the first element of each array.
    3. Track the current maximum value among the elements in the heap.
    4. Iterate while the heap is not empty:
       a. Extract the minimum element from the heap.
       b. Calculate the current range (max_value - min_value).
       c. Update the best range found so far if the current one is smaller.
       d. Retrieve the next element from the same array.
       e. If no next element exists, the range is exhausted for this path (since we need 
          one element from each array, and one array is finished), so break.
       f. Push the new element into the heap and update the current maximum if necessary.

    Returns:
        A tuple (start, end) representing the smallest range found.
    """
    # Step 1: Validate inputs explicitly
    _validate_inputs(arrays)

    # Step 2: Initialize the min-heap with the first element of each array
    initial_root = _merge_and_heapify(arrays)
    if initial_root is None:
        # This case should theoretically be unreachable due to validation
        raise RuntimeError("Internal error: Min-heap was empty after initialization.")

    min_value, current_array_idx, current_element_idx = initial_root

    # Step 3: Determine the initial maximum value across all arrays in the heap
    # We need to traverse the heap to find the max of the initial set.
    current_max_value = min_value
    # Re-populate logic to find max efficiently or just re-evaluate heap contents.
    # Since N is small compared to total elements, re-evaluating or maintaining max is fine.
    # Here, we will maintain 'current_max' as a variable.

    # To be thorough, let's rebuild the max calculation by looking at the heap content
    # or simply re-pushing if we remove. But standard approach:
    # We need the max of the *current* elements in the heap.

    # Let's implement a helper to get current max from the heap contents, 
    # or maintain it incrementally. Maintaining incrementally is tricky with removals.
    # Given constraints, scanning the heap is O(N) where N is number of arrays. 
    # Total complexity becomes O(N * M) where M is total elements, which is acceptable.

    # Actually, a cleaner way: 
    # We know the heap contains one element per array. 
    # We can't easily peek the max without scanning or a max-heap.
    # We will scan the heap to find the current max of the active window.

    def _get_current_max(heap_elements: List[Tuple[int, int, int]]) -> int:
        max_val = -float('inf')
        for item in heap_elements:
            value, _, _ = item
            if value > max_val:
                max_val = value
        return max_val

    # Calculate initial max
    current_max_value = _get_current_max(min_heap := _merge_and_heapify(arrays))

    best_range_start: Optional[int] = None
    best_range_end: Optional[int] = None
    min_range_size: Optional[int] = None

    # Current state tracker
    # We need to access the heap contents frequently.
    # Let's restart the heap construction cleanly for the loop variable scope.

    final_heap: List[Tuple[int, int, int]] = _merge_and_heapify(arrays)
    if not final_heap:
        raise RuntimeError("Heap is empty inside loop logic.")

    # Current max needs to be updated dynamically.
    # Since we remove one element and add another, the max might change.
    # We will recalculate the max after every modification to ensure correctness.
    # Optimization: We can try to optimize, but explicit clarity is required.

    while True:
        # Get the smallest element
        smallest_val, array_idx, element_idx = heapq.heappop(final_heap)

        # Calculate current range size
        current_range_size = current_max_value - smallest_val

        # Check if this is a new best range
        # First best is always valid
        if best_range_start is None or current_range_size < min_range_size:
            best_range_start = smallest_val
            best_range_end = current_max_value
            min_range_size = current_range_size

        # Prepare the next element from the same array
        next_val = _find_next_element(arrays, array_idx, element_idx)

        if next_val is None:
            # One array is exhausted. We cannot form a valid range with all arrays anymore.
            # Since we process elements in increasing order, the window is closed.
            break

        # Push the new element into the heap
        heapq.heappush(final_heap, (next_val, array_idx, element_idx + 1))

        # Update the current maximum value
        # We must re-scan the heap to find the new maximum because we added a new value
        # and the previous maximum might still be the largest, or the new value might be larger.
        current_max_value = _get_current_max(final_heap)

    # Final validation before returning
    if best_range_start is None:
        # This implies no valid range was found, which contradicts the problem statement 
        # (assuming inputs are valid and non-empty).
        raise RuntimeError("No valid range was found despite valid inputs.")

    return (best_range_start, best_range_end)