def positive_count(numbers):
    """
    Calculate the ratio of positive numbers in an array of integers.

    Args:
        numbers (list[int]): The list of integers to process.

    Returns:
        float: The ratio of positive numbers as a float.

    Raises:
        TypeError: If the input is not a list of integers.

    Examples:
        >>> positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
        0.54
        >>> positive_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
        0.69
        >>> positive_count([2, 4, -6, -9, 11, -12, 14, -5, 17])
        0.56
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All elements in the list must be integers.")

    # Count the total number of elements
    total_elements = len(numbers)

    # Handle edge case of empty list
    if total_elements == 0:
        return 0.0

    # Count positive numbers
    positive_count = 0
    for num in numbers:
        if num > 0:
            positive_count += 1

    # Calculate ratio
    ratio = positive_count / total_elements

    return ratio