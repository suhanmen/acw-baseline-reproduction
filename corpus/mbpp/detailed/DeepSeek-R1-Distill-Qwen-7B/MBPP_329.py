def neg_count(numbers):
    """
    Counts the number of negative numbers in a given list.

    Args:
        numbers (list): A list of numbers to be checked for negativity.

    Returns:
        int: The count of negative numbers in the list.

    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    negative_count = 0
    for num in numbers:
        if num < 0:
            negative_count += 1
    return negative_count

# Test cases
assert neg_count([-1, -2, 3, -4, -5]) == 4, "Test case 1 failed"
assert neg_count([1, 2, 3]) == 0, "Test case 2 failed"
assert neg_count([1, 2, -3, -10, 20]) == 2, "Test case 3 failed"
print("All test cases passed successfully")