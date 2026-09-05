import heapq

def heap_replace(heap: list, item: int) -> list:
    """
    Replaces the smallest element in a min-heap with a new item
    and maintains the heap property.
    """
    # First, ensure the input list is a valid heap.
    # The problem inputs are presented as heaps in a loose sense, 
    # but heapify ensures the structure.
    heapq.heapify(heap)

    # heapq.heapreplace pops the smallest element and pushes the new item.
    # This is more efficient than a pop followed by a push.
    heapq.heapreplace(heap, item)

    return heap

if __name__ == "__main__":
    assert heap_replace([25, 44, 68, 21, 39, 23, 89], 21) == [21, 25, 23, 44, 39, 68, 89]
    assert heap_replace([25, 44, 68, 21, 39, 23, 89], 110) == [23, 25, 68, 44, 39, 110, 89]
    assert heap_replace([25, 44, 68, 21, 39, 23, 89], 500) == [23, 25, 68, 44, 39, 500, 89]