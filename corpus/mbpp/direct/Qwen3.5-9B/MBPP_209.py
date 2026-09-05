import heapq

def heap_replace(heap, value):
    heapq.heapify(heap)
    heapq.heappop(heap)
    heapq.heappush(heap, value)
    return list(heap)