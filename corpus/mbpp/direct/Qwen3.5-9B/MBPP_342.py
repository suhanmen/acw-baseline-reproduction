import heapq
from typing import List, Tuple

def find_minimum_range(arrays: List[List[int]]) -> Tuple[int, int]:
    if not arrays:
        return (0, 0)

    # Min-heap to store (value, array_index, element_index)
    heap = []
    current_max = float('-inf')

    # Initialize heap with the first element from each array
    for i, arr in enumerate(arrays):
        val = arr[0]
        heapq.heappush(heap, (val, i, 0))
        current_max = max(current_max, val)

    min_range = (float('inf'), float('-inf'))

    while len(heap) == len(arrays):
        current_min, arr_idx, elem_idx = heapq.heappop(heap)

        # Check if this forms a smaller range
        current_range = current_max - current_min
        if current_range < (min_range[1] - min_range[0]):
            min_range = (current_min, current_max)

        # Move to next element in the same array
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))
            current_max = max(current_max, next_val)
        else:
            # One array is exhausted, can't form a valid range anymore
            break

    return min_range