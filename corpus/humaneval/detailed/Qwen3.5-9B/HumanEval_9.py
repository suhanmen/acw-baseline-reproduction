from typing import List


def _validate_input(numbers: List[int]) -> None:
    """
    Validates that the input is a list of integers.

    Raises:
        TypeError: If numbers is not a list or contains non-integer elements.
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list of integers, but received {type(numbers).__name__}.")

    for index, value in enumerate(numbers):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(
                f"Expected an integer at index {index}, but received {type(value).__name__} ({value})."
            )


def _compute_rolling_max(numbers: List[int]) -> List[int]:
    """
    Computes the rolling maximum for a list of integers.

    The rolling maximum at any position is the maximum value encountered
    from the start of the list up to and including the current position.

    Args:
        numbers: A non-empty list of integers.

    Returns:
        A list of integers where each element is the maximum of the input
        list up to that index.
    """
    if not numbers:
        return []

    # Initialize the result list with the same length as input
    result: List[int] = [0] * len(numbers)

    # Initialize the current maximum tracker with the first element
    current_max: int = numbers[0]

    # Set the first element of the result to the first element of input
    result[0] = current_max

    # Iterate through the rest of the elements starting from index 1
    for current_index in range(1, len(numbers)):
        current_value: int = numbers[current_index]

        # Update the current maximum if the current value is greater
        if current_value > current_max:
            current_max = current_value

        # Store the current maximum in the result list at the current index
        result[current_index] = current_max

    return result


def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element 
    found until given moment in the sequence.

    For each position in the list, the result contains the maximum value 
    observed in the input list from the beginning up to and including that position.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers representing the rolling maximums.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.

    Examples:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
        >>> rolling_max([])
        []
        >>> rolling_max([5])
        [5]
        >>> rolling_max([-1, -5, -3])
        [-1, -1, -1]
        >>> rolling_max([0, 0, 0])
        [0, 0, 0]
    """
    # Step 1: Validate the input to ensure type safety and data integrity
    _validate_input(numbers)

    # Step 2: Delegate the computation logic to the helper function
    # This ensures the core logic is isolated and reusable
    return _compute_rolling_max(numbers)