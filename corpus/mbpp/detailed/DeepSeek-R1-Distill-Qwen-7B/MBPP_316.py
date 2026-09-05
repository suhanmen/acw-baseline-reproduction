def find_last_occurrence(arr, target):
    def validate_input(arr, target):
        """Validate the input and handle edge cases."""
        if not isinstance(arr, list):
            raise ValueError("Input array must be a list.")
        if len(arr) == 0:
            raise ValueError("Array is empty.")
        if not isinstance(target, int):
            raise ValueError("Target must be an integer.")
        return True

    if not validate_input(arr, target):
        return -1  # Or handle as needed based on requirements

    # Initialize variables to track the last occurrence
    last_occurrence = -1
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            last_occurrence = mid
            # Search the right half to find the last occurrence
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last_occurrence

# Test cases to validate the function
assert find_last_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 3
assert find_last_occurrence([2, 3, 5, 8, 6, 6, 8, 9, 9, 9], 9) == 9
assert find_last_occurrence([2, 2, 1, 5, 6, 6, 6, 9, 9, 9], 6) == 6