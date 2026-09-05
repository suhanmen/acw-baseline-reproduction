def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    If two items have the same sum, they are ordered based on their original index.

    Args:
        nums: List of integers to be sorted.

    Returns:
        A new list sorted according to the specified criteria.

    Raises:
        TypeError: If any element in nums is not an integer.

    Examples:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not all(isinstance(n, int) for n in nums):
        raise TypeError("All elements must be integers.")

    # Helper function to calculate the sum of digits of a number
    def digit_sum(n):
        return sum(int(d) for d in str(abs(n)))

    # Create a list of tuples containing (original index, digit sum, original number)
    indexed_nums = [(i, digit_sum(n), n) for i, n in enumerate(nums)]

    # Sort the list based on digit sum, then original index
    sorted_indexed = sorted(indexed_nums, key=lambda x: (x[1], x[0]))

    # Extract the sorted numbers
    sorted_nums = [item[2] for item in sorted_indexed]

    return sorted_nums