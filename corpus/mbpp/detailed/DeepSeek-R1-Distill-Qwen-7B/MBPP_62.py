def smallest_num(lst):
    """
    Finds the smallest number in a list, handling various edge cases.

    Args:
        lst: The list of numbers to find the smallest number from.

    Returns:
        The smallest number in the list if valid input is provided.
        None if input is invalid or the list is empty.
    """
    # Input validation
    if not isinstance(lst, list):
        return None
    # Handle empty list
    if not lst:
        return None
    # Handle single element
    if len(lst) == 1:
        return lst[0]
    # Initialize smallest_num with the first element
    current_smallest = lst[0]
    # Iterate through each element starting from the second
    for num in lst[1:]:
        # Update current_smallest if a smaller number is found
        if num < current_smallest:
            current_smallest = num
    # Return the smallest number found
    return current_smallest

# Test cases
assert smallest_num([10, 20, 1, 45, 99]) == 1, "Test case 1 failed"
assert smallest_num([1, 2, 3]) == 1, "Test case 2 failed"
assert smallest_num([45, 46, 50, 60]) == 45, "Test case 3 failed"
print("All test cases passed")