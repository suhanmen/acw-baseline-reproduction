def longest_subseq_with_diff_one(arr):
    if not arr:
        return 0

    max_length = 1
    current_length = 1
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i-1]) == 1:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 1  # Reset current subsequence starting from current element

    return max_length

# Test cases
print(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 3, 2]))  # Expected output: 5
print(longest_subseq_with_diff_one([10, 9, 4, 5, 4, 8, 6]))  # Expected output: 3
print(longest_subseq_with_diff_one([1, 2, 3, 2, 3, 7, 2, 1]))  # Expected output: 4