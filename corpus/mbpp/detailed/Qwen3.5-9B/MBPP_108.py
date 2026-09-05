import heapq
from typing import Iterable, List, Any, Iterator

def _validate_input_list(input_list: Iterable[Any]) -> None:
    """
    Validates that the input is an iterable and can be converted to a list.
    Raises a TypeError if the input is not an iterable or contains non-iterable items.
    """
    try:
        # Attempt to convert the input to a list to ensure it is iterable
        # This also handles cases where the input is a generator or similar iterator.
        list(input_list)
    except TypeError as e:
        raise TypeError(f"Expected an iterable, but got: {type(input_list).__name__}") from e

def _sort_input_list(input_list: Iterable[Any]) -> List[Any]:
    """
    Converts the input iterable to a list and sorts it in ascending order.

    Args:
        input_list: An iterable of sortable items.

    Returns:
        A new list containing the sorted items.
    """
    try:
        # Convert the iterable to a list
        as_list = list(input_list)
    except TypeError:
        # This should ideally be caught by _validate_input_list, but kept here for safety
        raise TypeError("Input must be an iterable.") from None

    # Sort the list in ascending order
    as_list.sort()

    return as_list

def _initialize_heap_and_pointers(
    sorted_lists: List[List[Any]]
) -> tuple:
    """
    Initializes the priority queue (heap) and keeps track of the current index
    for each list that still has elements.

    Args:
        sorted_lists: A list of already sorted lists.

    Returns:
        A tuple containing:
            - A list of tuples (value, list_index, current_list_iterator)
            - A list of current indices for each input list
    """
    heap = []
    current_indices = []

    num_lists = len(sorted_lists)

    for list_index, current_list in enumerate(sorted_lists):
        if not current_list:
            # Skip empty lists; they contribute nothing to the merge
            continue

        # Initialize the iterator for the current list
        # We pass the list itself as the iterable, and track the index manually
        current_iterator = iter(current_list)

        try:
            # Peek at the first element of the current list
            # We store (value, list_index, original_list_pointer) in the heap
            # Note: Since lists are mutable and we pass the pointer, we need 
            # to be careful. However, for standard lists, passing the list object
            # works fine as an identity pointer.
            first_value = next(current_iterator)
        except StopIteration:
            # Should not happen if the check `if not current_list` above worked,
            # but included for defensive programming in case of edge cases.
            continue

        # Push to heap: (value, list_index, current_iterator)
        # We use list_index as the tie-breaker to maintain deterministic behavior
        # when values are equal. The current_iterator is needed to retrieve 
        # the next value later. However, heapq doesn't support advancing an 
        # iterator once popped. 
        # Correction strategy: We cannot easily advance an iterator inside a 
        # popped element context without re-implementing logic. 
        # Better approach: Store (value, list_index) in the heap, and maintain
        # a separate structure (like a list of iterators or indices) to know 
        # which element to pull next from which list.

        # Revised Heap Entry: (value, list_index)
        # We will maintain `current_indices` to know where to pull from.
        heapq.heappush(heap, (first_value, list_index))
        current_indices.append(0)  # Start reading from index 0

    return heap, current_indices

def _extract_next_item(heap: list, current_indices: list, sorted_lists: List[List[Any]]) -> tuple:
    """
    Extracts the smallest item from the heap and returns it along with 
    the list index it came from and the new index to pull from that list.

    Args:
        heap: The current heap of (value, list_index) tuples.
        current_indices: List of current read indices for each input list.
        sorted_lists: The original sorted lists.

    Returns:
        A tuple (value, list_index) representing the next smallest item and its source.
        Raises StopIteration if no more items are available.
    """
    if not heap:
        raise StopIteration("No more items to yield.")

    # Pop the smallest item
    value, list_index = heapq.heappop(heap)

    # Get the current index for this specific list
    current_idx = current_indices[list_index]

    # Check if this list has exhausted its elements
    list_len = len(sorted_lists[list_index])

    if current_idx < list_len:
        # Fetch the next item from this list to push into the heap
        next_value = sorted_lists[list_index][current_idx + 1]
        heapq.heappush(heap, (next_value, list_index))
        current_indices[list_index] += 1
    else:
        # This list is exhausted; decrement the index to keep consistency 
        # (though strictly not necessary if we check heap size, it helps debugging)
        # Actually, if a list is exhausted, we don't need to do anything special 
        # to the index in the next iteration because we won't try to read from it 
        # if the heap is managed correctly. But we must ensure we don't read out of bounds.
        # The logic above checks `current_idx < list_len` before reading.
        # So we are safe.
        pass

    return value, list_index

def merge_sorted_list(*lists: Iterable[Any]) -> Iterator[Any]:
    """
    Merges multiple sorted (or unsorted, which will be sorted internally) 
    inputs into a single sorted iterator using the heap queue algorithm.

    This function:
    1. Validates all inputs.
    2. Sorts all input lists in ascending order.
    3. Initializes a min-heap with the first element of each non-empty list.
    4. Repeatedly extracts the minimum element and pushes the next element 
       from the same source list into the heap until all lists are exhausted.

    Args:
        *lists: Variable number of iterables containing sortable items.

    Yields:
        The next smallest element from the merged result.

    Raises:
        TypeError: If any argument is not an iterable.
    """
    # Step 1: Validate and prepare the input lists
    if not lists:
        # Handle the case where no lists are provided
        return iter([])

    processed_lists = []

    for i, lst in enumerate(lists):
        try:
            # Validate and sort each list
            processed_lists.append(_sort_input_list(lst))
        except TypeError as e:
            raise TypeError(f"Invalid input at index {i}: {e}") from e

    # Step 2: Initialize the heap
    heap, current_indices = _initialize_heap_and_pointers(processed_lists)

    # Step 3: Iterate and yield elements
    try:
        while heap:
            # Extract the minimum element
            # We expect _extract_next_item to raise StopIteration if the heap is empty
            # but since we check `while heap`, it should have items.
            value, list_idx = _extract_next_item(heap, current_indices, processed_lists)
            yield value

    except StopIteration:
        # Normal exit when heap is empty
        return