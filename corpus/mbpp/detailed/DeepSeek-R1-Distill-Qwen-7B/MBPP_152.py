def merge_sort(arr):
    # Base case: if the array has 0 or 1 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Divide step: split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Conquer step: recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combine step: merge the sorted halves
    merged = []
    i = j = 0

    # Merge the two sorted arrays
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            j += 1

    # Add any remaining elements from either half
    merged += left_sorted[i:]
    merged += right_sorted[j:]

    return merged

# Test cases
assert merge_sort([3, 4, 2, 6, 5, 7, 1, 9]) == [1, 2, 3, 4, 5, 6, 7, 9], "Test case 1 failed"
assert merge_sort([7, 25, 45, 78, 11, 33, 19]) == [7, 11, 19, 25, 33, 45, 78], "Test case 2 failed"
assert merge_sort([3, 1, 4, 9, 8]) == [1, 3, 4, 8, 9], "Test case 3 failed"

print("All test cases passed!")