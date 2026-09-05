import heapq
from typing import List, Any, Tuple

def _validate_heap_property(heap: List[Any], value_comparator) -> bool:
    """
    Validates whether the given list satisfies the min-heap property.
    For every index i (starting at 0), if 2*i + 1 and 2*i + 2 are within bounds,
    the parent must be less than or equal to its children according to the comparator.

    :param heap: The list to validate.
    :param value_comparator: A function that takes (a, b) and returns a negative number if a < b.
    :return: True if the heap property holds, False otherwise.
    """
    if not heap:
        return True

    n = len(heap)

    for i in range(n):
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2

        # Check left child
        if left_child_index < n:
            left_child = heap[left_child_index]
            parent = heap[i]
            if value_comparator(parent, left_child) > 0:
                return False

        # Check right child
        if right_child_index < n:
            right_child = heap[right_child_index]
            parent = heap[i]
            if value_comparator(parent, right_child) > 0:
                return False

    return True

def _delete_root(heap: List[Any]) -> Tuple[Any, List[Any]]:
    """
    Removes and returns the root element (smallest in a min-heap).
    Restores the heap property after removal.

    :param heap: The input list representing the heap.
    :return: A tuple containing the removed root element and the updated heap list.
    """
    if not heap:
        raise ValueError("Cannot delete root from an empty heap.")

    removed_value = heap[0]
    heap_size_before = len(heap)

    # Replace root with the last element and reduce size
    heap[0] = heap[-1]
    heap_size_before = heap_size_before - 1

    # Remove the last element (which is now a duplicate of the old last)
    heap = heap[:heap_size_before]

    # Heapify down starting from the root
    new_heap_root = _heapify_down(heap, 0)

    return removed_value, new_heap_root

def _heapify_down(heap: List[Any], index: int) -> List[Any]:
    """
    Maintains the min-heap property by moving the element at 'index' down the tree
    until it is in the correct position or at a leaf.

    :param heap: The list representing the heap (modified in-place for the process, returned at the end).
    :param index: The index of the element to start sifting down from.
    :return: The modified heap list.
    """
    n = len(heap)
    current_index = index

    while True:
        left_child_index = 2 * current_index + 1
        right_child_index = 2 * current_index + 2
        smallest_index = current_index

        # Check if left child exists and is smaller
        if left_child_index < n:
            if heap[left_child_index] < heap[smallest_index]:
                smallest_index = left_child_index

        # Check if right child exists and is smaller than the current smallest
        if right_child_index < n:
            if heap[right_child_index] < heap[smallest_index]:
                smallest_index = right_child_index

        # If the current node is already the smallest, we are done
        if smallest_index == current_index:
            break

        # Swap current node with the smallest child
        heap[current_index], heap[smallest_index] = heap[smallest_index], heap[current_index]
        current_index = smallest_index

    return heap

def _insert_element(heap: List[Any], new_value: Any) -> List[Any]:
    """
    Inserts a new value into the heap while maintaining the heap property.
    Appends the value and then sifts it up.

    :param heap: The list representing the heap.
    :param new_value: The value to insert.
    :return: The updated heap list.
    """
    heap.append(new_value)
    new_heap_index = len(heap) - 1

    # Heapify up from the newly added position
    new_heap_index = _heapify_up(heap, new_heap_index)

    return new_heap_index

def _heapify_up(heap: List[Any], index: int) -> int:
    """
    Maintains the min-heap property by moving the element at 'index' up the tree
    until it is in the correct position or at the root.

    :param heap: The list representing the heap.
    :param index: The index of the element to sift up from.
    :return: The index where the element ended up.
    """
    parent_index = (index - 1) // 2

    while index > 0:
        parent = heap[parent_index]
        child = heap[index]

        # If parent is greater than child, swap them
        if parent > child:
            heap[parent_index], heap[index] = heap[index], heap[parent_index]
            index = parent_index
            parent_index = (index - 1) // 2
        else:
            break

    return index

def heap_replace(heap_input: List[Any], new_value: Any) -> List[Any]:
    """
    Deletes the smallest element from the given min-heap and inserts a new item.

    Process:
    1. Validate that the input list is not empty.
    2. Validate that the input list satisfies the min-heap property.
    3. Delete the root (smallest) element.
    4. Insert the new value.
    5. Return the resulting heap.

    :param heap_input: The input list representing a min-heap.
    :param new_value: The new value to insert after deletion.
    :return: The new heap list after replacement.
    :raises ValueError: If the heap is empty or does not satisfy the min-heap property.
    """

    # Step 1: Validate non-empty input
    if not heap_input:
        raise ValueError("Input heap cannot be empty.")

    # Step 2: Validate heap property
    # Using standard comparison operator for min-heap validation
    if not _validate_heap_property(heap_input, lambda a, b: a - b):
        raise ValueError("Input list does not satisfy the min-heap property.")

    # Step 3: Delete the smallest element (root)
    # We create a copy to ensure we don't mutate the original input reference unexpectedly
    # although the problem implies we return a new state.
    current_heap = list(heap_input)

    deleted_value, updated_heap = _delete_root(current_heap)

    # Step 4: Insert the new item
    final_heap = _insert_element(updated_heap, new_value)

    # Note: _insert_element returns the index, but since we just need the list,
    # we rely on the fact that _insert_element modifies the list in place during its internal steps
    # and returns the list index which we ignore for the final output structure,
    # but strictly speaking, _insert_element returns the index.
    # Let's correct the logic flow to ensure we return the list.

    # Re-implementing insertion step clearly for the return value:
    temp_heap = list(updated_heap) # Ensure we are working with a clean list
    temp_heap.append(new_value)
    final_insertion_index = _heapify_up(temp_heap, len(temp_heap) - 1)

    return temp_heap