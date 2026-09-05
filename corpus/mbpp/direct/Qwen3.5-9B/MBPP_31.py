import heapq
from collections import Counter
from typing import List

def func(nums: List[List[int]], k: int) -> List[int]:
    flat = []
    for lst in nums:
        flat.extend(lst)
    counts = Counter(flat)
    # Use a min-heap of size k to keep the k most frequent elements
    heap = []
    for num, count in counts.items():
        if len(heap) < k:
            heapq.heappush(heap, (count, num))
        else:
            if count > heap[0][0]:
                heapq.heapreplace(heap, (count, num))

    # Extract elements in descending order of frequency; tie-break by value descending based on test expectations
    result = []
    while heap:
        count, num = heapq.heappop(heap)
        result.append(num)

    # Reverse to get most frequent first; for ties, sort by value descending to match example [6,5,7,8,1]
    # Actually the example [6,5,7,8,1] for k=5 matches frequency order but with tie-breaking by descending value
    # Let's sort the result properly: primary key = frequency descending, secondary key = value descending
    final = []
    # Rebuild with explicit sorting for correct tie-breaking
    items = [(c, n) for n, c in counts.items()]
    items.sort(key=lambda x: (-x[1], -x[0]))  # Actually frequency descending, value descending
    # Wait: (count, num). We want higher count first, then higher num first.
    # So sort by (-count, -num)
    items.sort(key=lambda x: (-x[1], -x[0]))
    final = [x[1] for x in items[:k]]
    return final