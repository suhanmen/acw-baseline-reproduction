def find_length(binary_str):
    # Convert binary string to a list of integers (0 for '0', -1 for '1')
    diff = []
    for c in binary_str:
        if c == '0':
            diff.append(1)
        else:
            diff.append(-1)

    # Function to find the maximum subarray difference using Kadane's algorithm
    def max_subarray_diff(arr):
        max_current = max_global = arr[0]
        for i in range(1, len(arr)):
            max_current = max(arr[i], max_current + arr[i])
            max_global = max(max_global, max_current)
        return max_global

    # Edge case: empty string
    if not diff:
        return 0

    max_diff = max_subarray_diff(diff)

    # The maximum difference is the absolute value of max_diff, but considering subarrays of length at least 1
    return max(max_diff, -max_diff) if max_diff != 0 else 0

# Test the function with the provided assertions
assert find_length("11000010001", 11) == 6
assert find_length("10111", 5) == 1
assert find_length("11011101100101", 14) == 2