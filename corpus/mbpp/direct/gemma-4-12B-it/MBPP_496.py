import heapq

def heap_queue_smallest(numbers, k):
    """
    Finds the k smallest integers from a given list of numbers using a heap queue.
    """
    # Create a min-heap from the list of numbers
    heapq.heapify(numbers)

    smallest_elements = []
    # Pop the smallest element k times
    for _ in range(k):
        if numbers:
            smallest_elements.append(heapq.heappop(numbers))

    return smallest_elements