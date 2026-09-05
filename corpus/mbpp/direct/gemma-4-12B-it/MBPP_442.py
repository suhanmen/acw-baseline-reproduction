def positive_count(numbers: list[int]) -> float:
    """
    Calculates the ratio of positive numbers to the total number of integers 
    in a given list.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        float: The ratio of positive numbers to the total count of elements.
    """
    if not numbers:
        return 0.0

    positive_count = sum(1 for x in numbers if x > 0)
    return round(positive_count / len(numbers), 2)

if __name__ == "__main__":
    assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.54
    assert positive_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]) == 0.69
    assert positive_count([2, 4, -6, -9, 11, -12, 14, -5, 17]) == 0.56