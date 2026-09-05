def smallest_num(numbers):
    """
    Finds the smallest number in a list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        The smallest number in the list.
    """
    if not numbers:
        return None

    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

if __name__ == "__main__":
    assert smallest_num([10, 20, 1, 45, 99]) == 1
    assert smallest_num([1, 2, 3]) == 1
    assert smallest_num([45, 46, 50, 60]) == 45