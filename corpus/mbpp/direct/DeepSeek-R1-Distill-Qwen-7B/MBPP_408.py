import heapq

def k_smallest_pairs(arr1, arr2, k):
    # Initialize a min-heap with the smallest pair
    heap = []
    heapq.heappush(heap, (arr1[0] + arr2[0], 0, 0))

    # Set to keep track of visited indices
    visited = set()
    visited.add((0, 0))

    result = []

    while k > 0 and heap:
        current_sum, i, j = heapq.heappop(heap)
        result.append([arr1[i], arr2[j]])
        k -= 1

        # Add next element from arr1 if not beyond bounds
        if i + 1 < len(arr1) and (i + 1, j) not in visited:
            heapq.heappush(heap, (arr1[i+1] + arr2[j], i + 1, j))
            visited.add((i + 1, j))

        # Add next element from arr2 if not beyond bounds
        if j + 1 < len(arr2) and (i, j + 1) not in visited:
            heapq.heappush(heap, (arr1[i] + arr2[j+1], i, j + 1))
            visited.add((i, j + 1))

    return result