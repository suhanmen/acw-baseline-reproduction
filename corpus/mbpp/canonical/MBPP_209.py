import heapq as hq
def heap_replace(heap,a):
  hq.heapify(heap)
  hq.heapreplace(heap, a)
  return heap