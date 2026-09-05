import heapq

def func(lists, k):
    # Merge all the lists and count frequencies
    merged = []
    heap = []
    for num in zip(*lists):
        for x in num:
            if x not in heap:
                heapq.heappush(heap, x)

    # Extract elements from heap based on frequency
    result = []
    while heap and k > 0:
        count = 0
        current = heapq.heappop(heap)
        # Count how many times the current number appears across lists
        for lst in lists:
            if current in lst:
                count += 1
        if count > 0:
            result.append(current)
            k -= 1
    # Handle case where k is larger than available unique elements
    return result[:k]