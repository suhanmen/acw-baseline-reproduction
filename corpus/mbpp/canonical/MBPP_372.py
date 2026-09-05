import heapq as hq
def heap_assending(nums):
  hq.heapify(nums)
  s_result = [hq.heappop(nums) for i in range(len(nums))]
  return s_result