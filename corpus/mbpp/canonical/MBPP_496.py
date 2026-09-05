import heapq as hq
def heap_queue_smallest(nums,n):
  smallest_nums = hq.nsmallest(n, nums)
  return smallest_nums