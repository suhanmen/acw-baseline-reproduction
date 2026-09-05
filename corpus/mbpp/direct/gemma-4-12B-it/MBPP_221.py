def first_even(numbers):
    """
    Finds the first even number in a given list of numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The first even integer found, or None if no even integer exists.
    """
    for num in numbers:
        if num % 2 == 0:
            return num
    return None

if __name__ == "__main__":
    assert first_even([1, 3, 5, 7, 4, 1, 6, 8]) == 4
    assert first_even([2, 3, 4]) == 2
    assert first_even([5, 6, 7]) == 6