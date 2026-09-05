def remove_odd(numbers):
    """
    Removes all odd numbers from a given list of integers.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list containing only the even integers from the input.
    """
    return [num for num in numbers if num % 2 == 0]

if __name__ == "__main__":
    assert remove_odd([1, 2, 3]) == [2]
    assert remove_odd([2, 4, 6]) == [2, 4, 6]
    assert remove_odd([10, 20, 3]) == [10, 20]