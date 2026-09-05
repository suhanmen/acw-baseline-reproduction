def heap_replace(heap, item):
    import heapq
    if not heap:
        return [item]
    # Find the smallest element
    smallest = heap[0]
    # Remove it
    heap.remove(smallest)
    # Insert the new item
    heapq.heappush(heap, item)
    return heap