def max_Abs_Diff(arr):
    if not isinstance(arr, tuple):
        return None  # Assuming the function expects a tuple as input

    if len(arr) < 2:
        if len(arr) == 0:
            return None  # Or handle empty array as needed
        else:  # len(arr) == 1
            return 0

    # Find the maximum and minimum values in the array
    max_val = max(arr)
    min_val = min(arr)

    # Calculate the absolute difference
    max_diff = abs(max_val - min_val)

    return max_diff

# Test cases
print(max_Abs_Diff((2, 1, 5, 3)))  # Should return 4
print(max_Abs_Diff((9, 3, 2, 5, 1)))  # Should return 8
print(max_Abs_Diff((3, 2, 1)))  # Should return 2