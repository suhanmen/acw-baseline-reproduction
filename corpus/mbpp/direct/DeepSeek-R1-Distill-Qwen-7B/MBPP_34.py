def find_missing(arr):
    # Calculate the expected sum if the array had no missing numbers
    expected_sum = arr[0] + (len(arr) - 1) * (arr[-1] + arr[0]) // 2
    # Calculate the actual sum of the array
    actual_sum = sum(arr)
    # The missing number is the difference between the expected and actual sums
    return expected_sum - actual_sum

# Test the function with the provided examples
print(find_missing([1,2,3,5]))    # Should output 4
print(find_missing([1,3,4,5]))    # Should output 2
print(find_missing([1,2,3,5,6,7]))# Should output 4