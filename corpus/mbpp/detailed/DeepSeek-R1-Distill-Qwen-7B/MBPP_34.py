def find_missing(arr):
    if not arr:
        return 1  # Handle empty array by returning 1

    start = arr[0]
    end = arr[-1]
    n = len(arr) + 1  # Since one number is missing

    # Calculate the expected sum of a complete sorted array
    expected_sum = (n * (start + end)) // 2

    # Calculate the actual sum of the given array
    actual_sum = sum(arr)

    # The missing number is the difference between expected and actual sums
    missing = expected_sum - actual_sum

    return missing

# Test cases
assert find_missing([1, 2, 3, 5]) == 4
assert find_missing([1, 3, 4, 5]) == 2
assert find_missing([1, 2, 3, 5, 6, 7]) == 4