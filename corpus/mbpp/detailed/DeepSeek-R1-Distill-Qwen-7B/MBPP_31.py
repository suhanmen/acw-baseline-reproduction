import heapq

def func(lists, k):
    if k == 0:
        return []
    if len(lists) == 0 or len(lists[0]) == 0:
        return []

    # Count the frequency of each number
    freq = {}
    for lst in lists:
        for num in lst:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

    # If there are no elements, return an empty list
    if not freq:
        return []

    # Create a max-heap based on frequency and value
    heap = []
    for num, count in freq.items():
        heapq.heappush(heap, (-count, -num))

    # Extract the top k elements
    top_k = []
    for _ in range(k):
        if not heap:
            break
        neg_count, neg_num = heapq.heappop(heap)
        top_k.append((-neg_count, neg_num))

    # If there are fewer than k elements, return what we have
    if len(top_k) < k:
        return [x[1] for x in top_k]

    # Sort the result in ascending order
    top_k.sort()
    return [x[1] for x in top_k]

# Test cases
assert func([[1, 2, 6], [1, 3, 4, 5, 7, 8], [1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12]],3) == [5, 7, 1]
assert func([[1, 2, 6], [1, 3, 4, 5, 7, 8], [1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12]],1) == [1]
assert func([[1, 2, 6], [1, 3, 4, 5, 7, 8], [1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12]],5) == [6, 5, 7, 8, 1]