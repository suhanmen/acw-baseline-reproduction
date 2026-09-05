def counting_sort(arr):
    # Find the maximum value to determine the range of the count array
    if not arr:
        return []
    max_val = max(arr)
    # Initialize count array with size max_val + 1 (to handle 0 index)
    count = [0] * (max_val + 1)

    # Fill the count array
    for num in arr:
        count[num] += 1

    # Reconstruct the sorted array
    result = []
    for i in range(len(count)):
        result.extend([i] * count[i])

    return result

# Test cases
assert counting_sort([1,23,4,5,6,7,8]) == [1, 4, 5, 6, 7, 8, 23]
assert counting_sort([12, 9, 28, 33, 69, 45]) == [9, 12, 28, 33, 45, 69]
assert counting_sort([8, 4, 14, 3, 2, 1]) == [1, 2, 3, 4, 8, 14]