import heapq
from typing import List, Any, Iterable

def merge_sorted_list(*iterables: List[Any]) -> List[Any]:
    """
    Merges multiple sorted lists into a single sorted list using a min-heap.

    The algorithm maintains a heap of the smallest available element from each 
    non-empty input list. In each step, the smallest element is popped from 
    the heap and added to the result. The next element from the list that 
    provided the popped element is then pushed into the heap.

    Time Complexity: O(N log K), where N is the total number of elements 
    and K is the number of input lists.
    Space Complexity: O(K) for the heap.
    """
    # --- Input Validation ---
    # Ensure all inputs are lists or iterables. 
    # If any input is not iterable, we should raise a TypeError.
    for i, item in enumerate(iterables):
        if not hasattr(item, "__iter__"):
            raise TypeError(f"Input at index {i} is not an iterable object.")

    # If no inputs are provided, return an empty list.
    if not iterables:
        return []

    # If all inputs are empty, return an empty list.
    # We filter out empty lists immediately to avoid processing overhead.
    valid_iterables = []
    for item in iterables:
        # Convert to a list or iterator to ensure we can traverse it.
        # We check if it's non-empty.
        if hasattr(item, "__len__") and len(item) == 0:
            continue
        # For general iterables that don't have __len__, we will handle 
        # them inside the heap logic.
        valid_iterables.append(list(item))

    # If after filtering, no valid data exists, return empty.
    if not valid_iterables:
        return []

    # Note on Sorting: The problem description implies the inputs are 
    # "sorted", but the provided test cases contain inputs that are NOT sorted 
    # (e.g., [25, 24, 15...]). 
    # However, the expected output is the sorted merge of ALL elements.
    # If the inputs are not pre-sorted, we must sort them first to adhere
    # to the "merge sorted inputs" logic, or treat the inputs as unsorted 
    # collections and perform a K-way merge after ensuring each is sorted.
    # Given the assertions, we must ensure every input is sorted first.

    sorted_inputs = []
    for sub_list in valid_iterables:
        sorted_inputs.append(sorted(sub_list))

    # --- Heap Initialization ---
    # The heap will store tuples: (value, list_index, element_index)
    # list_index: which list in sorted_inputs the value came from.
    # element_index: the position of the value in that list.
    # We include list_index to handle cases where multiple lists have the 
    # same value (ensuring stability and avoiding comparison errors between lists).
    min_heap = []

    for list_idx, current_list in enumerate(sorted_inputs):
        if len(current_list) > 0:
            # Push the first element of each list into the heap
            value = current_list[0]
            heapq.heappush(min_heap, (value, list_idx, 0))

    result = []

    # --- Main Merge Loop ---
    while min_heap:
        # Pop the smallest element across all current heads of the lists
        smallest_value, list_idx, element_idx = heapq.heappop(min_heap)

        # Append to result
        result.append(smallest_value)

        # Calculate the index of the next element in the same source list
        next_element_idx = element_idx + 1

        # If there are more elements in that specific list, push the next one
        if next_element_idx < len(sorted_inputs[list_idx]):
            next_value = sorted_inputs[list_idx][next_element_idx]
            heapq.heappush(min_heap, (next_value, list_idx, next_element_idx))

    return result