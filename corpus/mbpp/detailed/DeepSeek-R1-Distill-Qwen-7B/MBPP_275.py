def get_Position(arr, start_index, target):
    # Check if the starting index is valid
    if start_index < 0 or start_index >= len(arr):
        # If start index is out of bounds, return it as if the element was removed from the end
        return start_index

    # Iterate through the array starting from start_index to find the target
    for i in range(start_index, len(arr)):
        if arr[i] == target:
            # Return the index of the first occurrence from start_index
            return i

    # If the target is not found, return the original start_index
    return start_index

# Test cases
assert get_Position([2,5,4], 3, 2) == 2
assert get_Position([4,3], 2, 2) == 2
assert get_Position([1,2,3,4], 4, 1) == 4