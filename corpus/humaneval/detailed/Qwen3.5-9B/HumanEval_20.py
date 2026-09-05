from typing import List, Tuple, Optional


def _validate_input(numbers: List[float]) -> List[float]:
    """
    Validates that the input list is not empty and contains at least two elements.
    Returns a copy of the valid list to ensure the caller's list is not mutated.

    :param numbers: The list of numbers to validate.
    :return: A copy of the input list.
    :raises ValueError: If the list is empty or has fewer than two elements.
    :raises TypeError: If the input is not a list.
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list of numbers, got {type(numbers).__name__}")

    if len(numbers) < 2:
        raise ValueError(
            f"List must contain at least two numbers to find the closest pair, "
            f"but received only {len(numbers)}."
        )

    return list(numbers)


def _find_closest_pair_in_sorted_list(sorted_numbers: List[float]) -> Tuple[float, float]:
    """
    Iterates through a sorted list of numbers to find the pair with the minimum difference.
    Since the list is sorted, the closest pair must be adjacent elements.

    :param sorted_numbers: A sorted list of floats.
    :return: A tuple (smaller, larger) representing the closest pair.
    """
    closest_diff: float = float('inf')
    closest_pair: Tuple[float, float] = (float('nan'), float('nan'))

    # Iterate up to the second-to-last element
    for i in range(len(sorted_numbers) - 1):
        current_number = sorted_numbers[i]
        next_number = sorted_numbers[i + 1]

        # Calculate difference. Since list is sorted, next_number >= current_number.
        difference: float = next_number - current_number

        # Check if this is the smallest difference found so far
        if difference < closest_diff:
            closest_diff = difference
            closest_pair = (current_number, next_number)

    return closest_pair


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the 
    closest to each other and return them in order (smaller number, larger number).

    :param numbers: A list of floating point numbers.
    :return: A tuple containing the two closest numbers (smaller, larger).
    :raises ValueError: If the list has fewer than 2 elements.
    :raises TypeError: If the input is not a list.
    """
    # Step 1: Validate the input
    valid_numbers = _validate_input(numbers)

    # Step 2: Sort the numbers to easily find adjacent pairs
    sorted_numbers: List[float] = sorted(valid_numbers)

    # Step 3: Find the closest pair in the sorted list
    result_pair: Tuple[float, float] = _find_closest_pair_in_sorted_list(sorted_numbers)

    return result_pair