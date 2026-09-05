from typing import List, Any

def heap_replace(heap: List[Any], new_item: Any) -> List[Any]:
    """
    Replaces the smallest element in a min-heap with a new item.

    A min-heap is a complete binary tree where the parent is always
    less than or equal to its children. In a list representation:
    - The root is at index 0.
    - For an element at index i:
        - Left child is at index 2*i + 1.
        - Right child is at index 2*i + 2.
        - Parent is at index (i - 1) // 2.

    Args:
        heap: A list representing a min-heap.
        new_item: The value to insert into the heap after removing the minimum.

    Returns:
        List[Any]: The updated heap.
    """
    # Input Validation
    if not isinstance(heap, list):
        raise TypeError("The heap input must be a list.")

    if not isinstance(new_item, (int, float)):
        # While the problem implies numbers, we should ensure 
        # types are comparable for a standard heap.
        pass 

    # Edge Case: Empty Heap
    # The problem implies we delete the smallest element first.
    # If empty, we simply return a heap containing only the new item.
    if not heap:
        return [new_item]

    # Edge Case: Single element
    # Removing the only element leaves an empty heap, then we add new_item.
    if len(heap) == 1:
        return [new_item]

    # Step 1: Identify the smallest element (root of the min-heap)
    # In a min-heap, the root at index 0 is always the smallest.
    # We replace it immediately with the new_item.
    heap[0] = new_item

    # Step 2: Restore the heap property (Sift Down / Heapify Down)
    # Since we replaced the root, we need to push the new value down
    # until it is smaller than its children.
    _sift_down(heap, 0)

    return heap

def _sift_down(heap: List[Any], index: int) -> None:
    """
    Standard min-heap sift-down operation to restore heap property.
    """
    heap_size = len(heap)
    current_idx = index

    while True:
        left_child_idx = 2 * current_idx + 1
        right_child_idx = 2 * current_idx + 2
        smallest_idx = current_idx

        # Check if left child exists and is smaller than current smallest
        if left_child_idx < heap_size:
            if heap[left_child_idx] < heap[smallest_idx]:
                smallest_idx = left_child_idx

        # Check if right child exists and is smaller than current smallest
        if right_child_idx < heap_size:
            if heap[right_child_idx] < heap[smallest_idx]:
                smallest_idx = right_child_idx

        # If the smallest is still the current index, the heap property is restored
        if smallest_idx == current_idx:
            break

        # Otherwise, swap and continue sifting down
        _swap(heap, current_idx, smallest_idx)
        current_idx = smallest_idx

def _swap(heap: List[Any], i: int, j: int) -> None:
    """
    Helper to swap two elements in a list.
    """
    temp = heap[i]
    heap[i] = heap[j]
    heap[j] = temp

# Verification with provided assertions
if __name__ == "__main__":
    # Test 1
    # Input: [25, 44, 68, 21, 39, 23, 89]
    # Min is 21 at index 3? Wait, the provided assertion implies the input 
    # list is treated as a heap, but let's look at the numbers:
    # The smallest number in [25, 44, 68, 21, 39, 23, 89] is 21.
    # However, in a standard heap structure, the root (index 0) is 25.
    # Let's re-examine the assertion: 
    # heap_replace([25, 44, 68, 21, 39, 23, 89], 21) == [21, 25, 23, 44, 39, 68, 89]
    # In the output [21, 25, 23, 44, 39, 68, 89], the root is 21.
    # The original heap had 25 at index 0. 
    # This means the function is expected to remove the actual minimum value 
    # from the list (which is 21) and insert a new value.
    # BUT, the assertion shows that 21 was the smallest, it was removed, 
    # and a NEW 21 was inserted? No, it's replacing the smallest 
    # element of the collection.

    # Wait, looking closely at the assertion:
    # heap_replace([25, 44, 68, 21, 39, 23, 89], 21)
    # Smallest value in list is 21.
    # If we remove 21 and add 21, and heapify:
    # The resulting heap should have 21 at index 0.
    # The output [21, 25, 23, 44, 39, 68, 89] is a valid min-heap.
    # The smallest value in the input [25, 44, 68, 21, 39, 23, 89] is 21.
    # It seems the heap is not strictly initialized in the input.

    # Re-evaluating logic: The problem asks to delete the smallest element 
    # and insert a new item. 
    # Since the inputs provided are not valid heaps (e.g. 25 at index 0 
    # while 21 is at index 3), we must first identify the minimum 
    # value, remove it, and insert the new item into a heap structure.
    # However, standard "heap_replace" in libraries (like Python's heapq) 
    # assumes the input IS a heap and replaces the root (index 0).

    # Let's look at the provided assertions again:
    # Input: [25, 44, 68, 21, 39, 23, 89], New: 21. Min is 21.
    # Output: [21, 25, 23, 44, 39, 68, 89]
    # Input: [25, 44, 68, 21, 39, 23, 89], New: 110. Min is 21.
    # Output: [23, 25, 68, 44, 39, 110, 89]
    # This confirms:
    # 1. Find the minimum value in the list regardless of position.
    # 2. Remove that minimum value.
    # 3. Insert the new_item.
    # 4. Return the resulting list as a valid min-heap.

    # Revised logic for the specific assertions:
    def heap_replace_fixed(h: List[Any], new_val: Any) -> List[Any]:
        if not h:
            return [new_val]

        # Find index of the minimum element
        min_val = h[0]
        min_idx = 0
        for i in range(1, len(h)):
            if h[i] < min_val:
                min_val = h[i]
                min_idx = i

        # Remove the minimum element
        # We use pop(min_idx) which shifts everything.
        # But we need to maintain the list size/structure for the replacement.
        # Actually, the simplest way to satisfy the assertions is:
        # 1. Remove the minimum value.
        # 2. Append the new value.
        # 3. Perform heapify on the whole list.

        temp_list = list(h)
        temp_list.pop(min_idx)
        temp_list.append(new_val)

        # Heapify the list
        n = len(temp_list)
        for i in range(n // 2 - 1, -1, -1):
            _sift_down_internal(temp_list, i)
        return temp_list

    def _sift_down_internal(lst, i):
        n = len(lst)
        while True:
            smallest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and lst[l] < lst[smallest]:
                smallest = l
            if r < n and lst[r] < lst[smallest]:
                smallest = r
            if smallest == i:
                break
            lst[i], lst[smallest] = lst[smallest], lst[i]
            i = smallest

    # The logic in the assertions follows this "Find Min -> Remove -> Insert -> Heapify"
    # But wait, the assertions are very specific. Let's check:
    # [25, 44, 68, 21, 39, 23, 89] -> min is 21. Remove 21 -> [25, 44, 68, 39, 23, 89]
    # Insert 110 -> [25, 44, 68, 39, 23, 89, 110]
    # Heapify -> [23, 25, 68, 44, 39, 89, 110] ... No, that doesn't match [23, 25, 68, 44, 39, 110, 89].

    # Let's try another interpretation:
    # The input list IS the heap, but the items are just arranged such that 
    # 21 is the minimum? No, 21 is at index 3. 
    # What if we replace the minimum value found anywhere, then heapify?
    # What if we just replace the minimum value with the new_item in place,
    # then heapify?

    # Let's try:
    # Input: [25, 44, 68, 21, 39, 23, 89], New: 110
    # Minimum is 21 at index 3.
    # Replace index 3 with 110: [25, 44, 68, 110, 39, 23, 89]
    # Heapify:
    # Root 25 has children 44, 68.
    # Index 1 (44) has children 110, 39.
    # Index 2 (68) has child 23.
    # Index 3 (110) has child 89.
    # Sift down 68 (index 2) with child 23: Swap -> [25, 44, 23, 110, 39, 68, 89]
    # Sift down 25 (index 0): Child 44 (idx 1) vs 23 (idx 2). 23 is smaller.
    # Swap 25 and 23: [23, 44, 25, 110, 39, 68, 89]
    # Sift down 44 (idx 1): Child 110 (idx 3) vs 39 (idx 4). 39 is smaller.
    # Swap 44 and 39: [23, 39, 25, 110, 44, 68, 89]
    # Still not matching [23, 25, 68, 44, 39, 110, 89].

    # Let's look at the output [23, 25, 68, 44, 39, 110, 89] again.
    # If we replace 21 with 110 AND then perform a standard heapify:
    # The output [23, 25, 68, 44, 39, 110,