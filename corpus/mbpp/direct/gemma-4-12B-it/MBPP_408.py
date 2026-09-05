import heapq

def k_smallest_pairs(nums1, nums2, k):
    """
    Finds k smallest pairs (one from nums1, one from nums2) sorted by their sum.
    Uses a min-heap to efficiently find the smallest pairs.
    """
    if not nums1 or not nums2 or k <= 0:
        return []

    # Ensure arrays are sorted for the algorithm to work correctly
    nums1.sort()
    nums2.sort()

    min_heap = []
    # Initial heap: (sum, index_in_nums1, index_in_nums2)
    # We push (nums1[i] + nums2[0], i, 0) for all i up to k
    for i in range(min(len(nums1), k)):
        heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

    result = []
    while min_heap and len(result) < k:
        current_sum, i, j = heapq.heappop(min_heap)
        result.append([nums1[i], nums2[j]])

        # If there is a next element in nums2 for the current nums1[i]
        if j + 1 < len(nums2):
            heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

    return result