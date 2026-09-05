from typing import List, Tuple, Optional


def _find_min_value(numbers: List[float]) -> Optional[float]:
    """
    Helper function to find the minimum value in the list.

    Returns:
        The minimum value if the list is non-empty.
        None if the list is empty.
    """
    if not numbers:
        return None

    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val


def _find_max_value(numbers: List[float]) -> Optional[float]:
    """
    Helper function to find the maximum value in the list.

    Returns:
        The maximum value if the list is non-empty.
        None if the list is empty.
    """
    if not numbers:
        return None

    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def _perform_rescale(
    numbers: List[float], 
    min_val: float, 
    max_val: float
) -> List[float]:
    """
    Helper function to perform the actual linear transformation.

    The transformation formula is: rescaled = (num - min_val) / (max_val - min_val)

    Args:
        numbers: The list of numbers to rescale.
        min_val: The minimum value found in the list.
        max_val: The maximum value found in the list.

    Returns:
        A new list with rescaled values.

    Raises:
        ValueError: If min_val equals max_val (division by zero scenario).
    """
    range_val = max_val - min_val

    if range_val == 0.0:
        # All elements are equal; result should be all zeros based on linear transform logic
        # where (x - min) / 0 is undefined, but mathematically in normalization
        # with equal values, everything maps to 0.
        return [0.0 for _ in numbers]

    rescaled_list: List[float] = []

    for num in numbers:
        shifted = num - min_val
        rescaled_value = shifted / range_val
        rescaled_list.append(rescaled_value)

    return rescaled_list


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    >>> rescale_to_unit([])
    Traceback (most recent call last):
        ...
    ValueError: Input list must contain at least two elements.
    >>> rescale_to_unit([5.0])
    Traceback (most recent call last):
        ...
    ValueError: Input list must contain at least two elements.
    >>> rescale_to_unit([3.0, 3.0, 3.0])
    [0.0, 0.0, 0.0]
    >>> rescale_to_unit([-10.0, 0.0, 10.0])
    [0.0, 0.5, 1.0]
    """

    # Explicit check for empty list
    if len(numbers) == 0:
        raise ValueError("Input list must contain at least two elements.")

    # Explicit check for single element list
    if len(numbers) == 1:
        raise ValueError("Input list must contain at least two elements.")

    # Find minimum and maximum values using helper functions
    min_val: float = _find_min_value(numbers)  # Type narrowing: not None due to checks above
    max_val: float = _find_max_value(numbers)  # Type narrowing: not None due to checks above

    # Perform the rescaling operation
    return _perform_rescale(numbers, min_val, max_val)