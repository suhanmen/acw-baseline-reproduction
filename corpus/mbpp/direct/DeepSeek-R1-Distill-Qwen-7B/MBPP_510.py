def no_of_subsequences(arr, k):
    n = len(arr)
    count = 0
    for i in range(1, 1 << n):  # Iterate over all non-empty subsequences
        product = 1
        for j in range(n):
            if i & (1 << j):  # Check if j-th element is included
                product *= arr[j]
                if product >= k:
                    break
        if product < k:
            count += 1
    return count

# Example usage and assertions
assert no_of_subsequences([1, 2, 3, 4], 10) == 11
assert no_of_subsequences([4, 8, 7, 2], 50) == 9
assert no_of_subsequences([5, 6, 7, 8], 15) == 4