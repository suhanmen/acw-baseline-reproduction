def pos_count(lst):
    """
    Counts the number of positive numbers in a given list.

    Args:
        lst: A list of numbers.

    Returns:
        The count of positive numbers in the list.
    """
    if not isinstance(lst, list):
        return None

    positive_count = 0
    for number in lst:
        if number > 0:
            positive_count += 1

    return positive_count

# Test cases to verify the correctness of the function
assert pos_count([1, -2, 3, -4]) == 2, "Test case 1 failed"
assert pos_count([3, 4, 5, -1]) == 3, "Test case 2 failed"
assert pos_count([1, 2, 3, 4]) == 4, "Test case 3 failed"