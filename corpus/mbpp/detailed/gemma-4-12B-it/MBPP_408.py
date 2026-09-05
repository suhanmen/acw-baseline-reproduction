import heapq
from typing import List

def k_smallest_pairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    """
    Finds the k smallest pairs (u, v) where u is from nums1 and v is from nums2,
    sorted by their sum (u + v). In case of equal sums, the ordering is determined 
    by the order of discovery in the priority queue.

    Args:
        nums1: List of integers.
        nums2: List of integers.
        k: The number of smallest pairs to return.

    Returns:
        A list of lists, where each inner list is a pair [u, v].
    """
    # Input Validation
    if not isinstance(nums1, list) or not isinstance(nums2, list):
        raise ValueError("Inputs nums1 and nums2 must be lists.")
    if not isinstance(k, int) or k < 0:
        raise ValueError("k must be a non-negative integer.")

    # Handle degenerate cases: empty arrays or k=0
    if not nums1 or not nums2 or k == 0:
        return []

    # Sort the input lists to ensure we can process elements in increasing order.
    # This allows us to use a min-heap efficiently to find the smallest sums.
    sorted_nums1 = sorted(nums1)
    sorted_nums2 = sorted(nums2)

    # The heap will store tuples: (sum, index_in_nums1, index_in_nums2)
    # We use a min-heap to always extract the pair with the smallest sum.
    min_heap = []

    # Initial population of the heap.
    # To avoid adding all possible pairs (which could be O(N*M)), 
    # we only start with the first element of nums1 paired with every element 
    # of nums2 is not efficient. Instead, we pair every element of nums1
    # with the first element of nums2.
    # This ensures that for any pair (i, j), the pair (i, j-1) was already
    # available or considered.

    # Optimization: Only need to put up to k elements initially to ensure 
    # we don't exceed k if the lists are very large.
    limit_nums1 = min(len(sorted_nums1), k)
    for i in range(limit_nums1):
        # Sum, index in sorted_nums1, index in sorted_nums2
        pair_sum = sorted_nums1[i] + sorted_nums2[0]
        heapq.heappush(min_heap, (pair_sum, i, 0))

    result = []

    # Extract the smallest sum from the heap k times.
    while min_heap and len(result) < k:
        current_sum, idx1, idx2 = heapq.heappop(min_heap)

        # Add the pair to our result list
        result.append([sorted_nums1[idx1], sorted_nums2[idx2]])

        # If there is a next element in sorted_nums2, push the pair 
        # (sorted_nums1[idx1], sorted_nums2[idx2 + 1]) into the heap.
        next_idx2 = idx2 + 1
        if next_idx2 < len(sorted_nums2):
            next_sum = sorted_nums1[idx1] + sorted_nums2[next_idx2]
            heapq.heappush(min_heap, (next_sum, idx1, next_idx2))

    return result

# The problem logic is encapsulated in the k_smallest_pairs function above.
# The logic handles:
# 1. Empty inputs -> returns empty list.
# 2. k=0 -> returns empty list.
# 3. k larger than total pairs -> returns all possible pairs.
# 4. Negative numbers -> handled correctly by the sum logic.
# 5. Duplicate numbers -> handled correctly by the heap and sorting.