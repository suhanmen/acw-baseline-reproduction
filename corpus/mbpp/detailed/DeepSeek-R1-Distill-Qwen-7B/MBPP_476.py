def big_sum(arr):
    # Validate the input: check if arr is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")

    # Check if the list is empty
    if len(arr) == 0:
        raise ValueError("List cannot be empty.")

    # Check if the list contains at least one element
    if len(arr) == 1:
        # Handle the case where there's only one element
        return arr[0] + arr[0]  # sum is twice the element

    # Find the smallest and largest values in the array
    smallest = min(arr)
    largest = max(arr)

    # Return the sum of the smallest and largest values
    return smallest + largest

# Test cases to verify the function works as expected
assert big_sum([1, 2, 3]) == 4, "Test case 1 failed"
assert big_sum([-1, 2, 3, 4]) == 3, "Test case 2 failed"
assert big_sum([2, 3, 6]) == 8, "Test case 3 failed"
print("All test cases passed successfully!")