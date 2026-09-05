def large_product(nums1, nums2, k):
    import heapq
    n = len(nums1)
    m = len(nums2)

    # Sort both lists in descending order
    nums1.sort(reverse=True)
    nums2.sort(reverse=True)

    # Use a max heap to find the top k products
    # Python's heapq is a min-heap, so we store negative values
    heap = []
    visited = set()

    def push_product(i, j):
        prod = nums1[i] * nums2[j]
        if (i, j) not in visited:
            visited.add((i, j))
            heapq.heappush(heap, -prod, (i, j))

    # Start with the largest product (first elements of both sorted lists)
    push_product(0, 0)

    result = []

    for _ in range(k):
        if not heap:
            break

        neg_prod, idx = heapq.heappop(heap)
        prod = -neg_prod
        result.append(prod)

        i, j = idx

        # Explore neighbors in the sorted grid
        if i + 1 < n:
            push_product(i + 1, j)
        if j + 1 < m:
            push_product(i, j + 1)

    return result