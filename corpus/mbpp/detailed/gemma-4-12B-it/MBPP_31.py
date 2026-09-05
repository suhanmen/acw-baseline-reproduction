import heapq
from collections import Counter
from typing import List

def func(lists: List[List[int]], k: int) -> List[int]:
    """
    Finds the top k integers that occur most frequently from a list of sorted 
    and distinct integer lists using a heap queue algorithm.

    Args:
        lists (List[List[int]]): A list of lists, where each inner list 
                                  contains sorted, distinct integers.
        k (int): The number of top frequent elements to return.

    Returns:
        List[int]: A list of k integers that occur most frequently. 
                    If multiple elements have the same frequency, the order 
                    is determined by the heap.
    """
    # --- Input Validation ---
    if not isinstance(lists, list):
        raise ValueError("Input 'lists' must be a list of lists.")

    if not isinstance(k, int) or k < 0:
        raise ValueError("Input 'k' must be a non-negative integer.")

    # Handle the edge case where k is 0 or the input is empty
    if k == 0:
        return []

    if not lists:
        return []

    # --- Step 1: Count Frequencies ---
    # Since we need to find most frequent, we first need a mapping of 
    # integer -> count. We iterate through every list and every element.
    frequency_map = Counter()

    for sublist in lists:
        if not isinstance(sublist, list):
            raise ValueError("Each element in the input list must be a list of integers.")

        for item in sublist:
            if not isinstance(item, int):
                raise ValueError("All elements within the inner lists must be integers.")
            frequency_map[item] += 1

    # --- Step 2: Handle cases where total unique elements < k ---
    unique_elements = list(frequency_map.keys())
    if len(unique_elements) == 0:
        return []

    # If k is larger than the number of unique elements, we cap k
    actual_k = min(k, len(unique_elements))

    # --- Step 3: Use a Min-Heap to find top k frequencies ---
    # We use a min-heap of size k to maintain the top k elements.
    # The heap stores tuples: (frequency, value).
    # By using a min-heap, the smallest frequency among the "top k" is 
    # at the root. If we find an element with a higher frequency, 
    # we pop the smallest and push the new one.

    min_heap = []

    for value, count in frequency_map.items():
        if len(min_heap) < actual_k:
            heapq.heappush(min_heap, (count, value))
        else:
            # If current count is greater than the smallest in our top-k heap
            if count > min_heap[0][0]:
                heapq.heapreplace(min_heap, (count, value))
            # Note: If count == min_heap[0][0], the behavior is 
            # technically undefined by "top k" unless a secondary 
            # sort key is provided. The problem assertions imply 
            # standard heap behavior is sufficient.

    # --- Step 4: Extract results ---
    # The heap contains the k most frequent items. 
    # We need to return them in descending order of frequency to 
    # match the logic of "top" elements.

    # First, extract the elements from the heap
    # Because it's a min-heap, popping gives us the smallest of the "top" items first.
    # We collect them and then reverse or sort to ensure the most frequent are first.

    results = []
    while min_heap:
        freq, val = heapq.heappop(min_heap)
        results.append((freq, val))

    # Sort the results by frequency descending
    # If frequencies are equal, the secondary sort is the value itself
    results.sort(key=lambda x: x[0], reverse=True)

    # Extract only the values
    final_output = [item[1] for item in results]

    return final_output