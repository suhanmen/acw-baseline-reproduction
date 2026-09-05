import heapq

def heap_queue_smallest(numbers, k):
    if k == 0:
        return []
    # Convert the list into a heap
    heapq.heapify(numbers)
    # Extract the smallest k elements
    smallest = []
    for _ in range(k):
        smallest.append(heapq.heappop(numbers))
    return smallest

# Test cases
assert heap_queue_smallest([25, 35, 22, 85, 14, 65, 75, 25, 58], 3) == [14, 22, 25]
assert heap_queue_smallest([25, 35, 22, 85, 14, 65, 75, 25, 58], 2) == [14, 22]
assert heap_queue_smallest([25, 35, 22, 85, 14, 65, 75, 22, 58], 5) == [14, 22, 22, 25, 35]