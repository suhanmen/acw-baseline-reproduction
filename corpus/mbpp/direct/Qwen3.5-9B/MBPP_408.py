import heapq
from typing import List, Tuple, Any

def k_smallest_pairs(arr1: List[int], arr2: List[int], k: int) -> List[List[int]]:
    if not arr1 or not arr2 or k <= 0:
        return []

    min_heap = []
    # Push the pair (sum, i, 0) -> smallest sum of arr1[i] + arr2[0]
    for i in range(min(k, len(arr1))):
        heapq.heappush(min_heap, (arr1[i] + arr2[0], i, 0))

    result = []
    while k > 0 and min_heap:
        total, i, j = heapq.heappop(min_heap)
        result.append([arr1[i], arr2[j]])
        k -= 1

        # If we can move to the next element in arr2
        if j + 1 < len(arr2):
            next_total = arr1[i] + arr2[j + 1]
            heapq.heappush(min_heap, (next_total, i, j + 1))

    return result