import heapq

def heap_assending(arr):
    heap = arr[:]
    heapq.heapify(heap)
    result = []
    while heap:
        result.append(heapq.heappop(heap))
    return result