def find_Min(arr, left, right):
    if not arr:
        return None  # Assuming this handles invalid input gracefully

    n = len(arr)

    # Handle edge cases
    if n == 0:
        return None
    if n == 1:
        return arr[left]

    # Check if the array is not rotated
    if arr[left] <= arr[right]:
        return arr[left]

    # Find the minimum by checking each element
    current_min = arr[left]
    for i in range(left, right + 1):
        if arr[i] < current_min:
            current_min = arr[i]
    return current_min

# Example usage
assert find_Min([1,2,3,4,5], 0, 4) == 1
assert find_Min([4,6,8], 0, 2) == 4
assert find_Min([2,3,5,7,9], 0, 4) == 2

# Test case where all elements are the same
assert find_Min([5,5,5], 0, 2) == 5

# Test case where the array is rotated
assert find_Min([3,4,5,1,2], 0, 4) == 1