from typing import List, Tuple


def _sum_of_digits(n: int) -> int:
    """
    Calculate the sum of the absolute digits of a given integer.

    Args:
        n (int): The integer to process.

    Returns:
        int: The sum of the digits of the absolute value of n.

    Raises:
        TypeError: If the input is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected an integer, got {type(n).__name__}")

    # Use abs to ensure negative signs don't affect the sum calculation
    # e.g., sum_digits(-12) should be 1+2 = 3
    abs_n = abs(n)

    total_sum = 0
    temp_n = abs_n

    # Handle zero explicitly to avoid infinite loops if logic were different
    if temp_n == 0:
        return 0

    # Extract digits and sum them up
    while temp_n > 0:
        digit = temp_n % 10
        total_sum += digit
        temp_n = temp_n // 10

    return total_sum


def _get_sort_key(item_index: int, value: int) -> Tuple[int, int]:
    """
    Generate a tuple key for sorting items.

    The primary sort criterion is the sum of digits (ascending).
    The secondary sort criterion is the original index (ascending)
    to maintain stability for elements with equal digit sums.

    Args:
        item_index (int): The original index of the item in the list.
        value (int): The integer value of the item.

    Returns:
        Tuple[int, int]: A tuple containing (digit_sum, original_index).
    """
    digit_sum = _sum_of_digits(value)
    return (digit_sum, item_index)


def order_by_points(nums: List[int]) -> List[int]:
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.

    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []

    Args:
        nums (List[int]): A list of integers to be sorted.

    Returns:
        List[int]: A new list containing the integers sorted by digit sum,
                   then by original index.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
        ValueError: If the list contains None values or non-finite numbers (though 
                    Python ints are always finite, this check ensures strict int type).
    """
    # Validate that the input is indeed a list
    if not isinstance(nums, list):
        raise TypeError(f"Expected a list, got {type(nums).__name__}")

    # Validate that all elements are integers
    for index, item in enumerate(nums):
        if not isinstance(item, int):
            raise TypeError(f"Element at index {index} is not an integer: {type(item).__name__}")
        # Explicitly check for non-integer types that might subclass int or be tricky
        # (Though in standard Python, this is sufficient for most use cases)
        if item != item: # NaN check, though not possible for standard int, good practice if type checking was looser
            raise ValueError(f"Element at index {index} is not a valid integer")

    # Create a list of tuples containing (original_index, value)
    # This allows us to sort based on multiple criteria easily
    indexed_items: List[Tuple[int, int]] = []

    for index, value in enumerate(nums):
        indexed_items.append((index, value))

    # Sort the indexed items
    # Key function:
    # 1. Calculate digit sum for the value
    # 2. Return tuple (digit_sum, original_index)
    # Python's sort is stable, but we explicitly include original_index in the key
    # to guarantee deterministic ordering for equal digit sums as per requirements.

    sorted_indexed_items = sorted(
        indexed_items, 
        key=lambda item_tuple: _get_sort_key(item_tuple[0], item_tuple[1])
    )

    # Extract the values from the sorted tuples into a new list
    sorted_values: List[int] = []
    for _, value in sorted_indexed_items:
        sorted_values.append(value)

    return sorted_values