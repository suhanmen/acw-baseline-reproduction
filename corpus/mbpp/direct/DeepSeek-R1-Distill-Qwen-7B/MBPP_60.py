def max_len_sub(arr, k):
    if not arr:
        return 0
    max_length = 1
    current_length = 1
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i-1]) <= k:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 1  # Reset current_length when the condition fails
    return max_length

# Example test cases
assert max_len_sub([2, 5, 6, 3, 7, 6, 5, 8], 8) == 5
assert max_len_sub([-2, -1, 5, -1, 4, 0, 3], 7) == 4
assert max_len_sub([9, 11, 13, 15, 18], 5) == 1