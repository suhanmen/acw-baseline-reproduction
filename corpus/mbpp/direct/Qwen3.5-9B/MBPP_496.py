import heapq

def heap_queue_smallest(numbers, k):
    if k <= 0:
        return []
    if k >= len(numbers):
        return sorted(numbers)

    heapq.heapify(numbers)
    return [heapq.heappop(numbers) for _ in range(k)]