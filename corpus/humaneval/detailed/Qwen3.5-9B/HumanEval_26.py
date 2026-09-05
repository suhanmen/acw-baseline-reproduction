from typing import List

from collections import Counter


def _validate_input(values: List[int]) -> None:
    """
    Validate that the input is a list of integers.
    Raises a TypeError if the input type is incorrect.
    """
    if not isinstance(values, list):
        raise TypeError(f"Expected a list of integers, got {type(values).__name__} instead.")

    if not all(isinstance(item, int) for item in values):
        non_int_items = [item for item in values if not isinstance(item, int)]
        raise TypeError(f"All items must be integers. Found non-integer items: {non_int_items}")


def _count_occurrences(values: List[int]) -> dict[int, int]:
    """
    Count the frequency of each integer in the input list.
    Returns a dictionary mapping each number to its count.
    """
    frequency_map = {}
    for number in values:
        if number in frequency_map:
            frequency_map[number] += 1
        else:
            frequency_map[number] = 1
    return frequency_map


def _filter_unique_numbers(values: List[int], frequency_map: dict[int, int]) -> List[int]:
    """
    Filter the input list to keep only numbers that appear exactly once.
    Preserves the original order of the elements.
    Returns a new list containing only the unique numbers.
    """
    result = []
    for number in values:
        count = frequency_map[number]
        if count == 1:
            result.append(number)
    return result


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Step 1: Validate the input to ensure it is a list of integers.
    _validate_input(numbers)

    # Step 2: Calculate the frequency of each number in the list.
    frequency_map = _count_occurrences(numbers)

    # Step 3: Filter the original list, keeping only numbers with a frequency of exactly 1.
    unique_numbers = _filter_unique_numbers(numbers, frequency_map)

    return unique_numbers