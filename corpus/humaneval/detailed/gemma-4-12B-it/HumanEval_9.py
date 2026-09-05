from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Input Validation: Ensure the input is a list
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list of integers, but received {type(numbers).__name__}")

    # Input Validation: Ensure all elements in the list are integers
    for item in numbers:
        if not isinstance(item, int):
            raise TypeError(f"All elements in the list must be integers. Found: {type(item).__name__}")

    # Handle edge case: Empty input list
    if not numbers:
        return []

    # Initialize variables for the result list and the current running maximum
    rolling_maximums: List[int] = []

    # We initialize the current_max with the first element of the input list.
    # This is safe because we've already checked that the list is not empty.
    first_element: int = numbers[0]
    current_max: int = first_element

    # Process the first element explicitly to set the initial state
    rolling_maximums.append(current_max)

    # Iterate through the rest of the sequence starting from the second element
    # We use a range-based loop to keep indexing explicit
    for index in range(1, len(numbers)):
        current_value: int = numbers[index]

        # Determine if the current value is larger than our recorded max
        is_new_max: bool = current_value > current_max

        if is_new_max:
            # Update the current_max tracker
            current_max = current_value

        # Append the current state of the running maximum to our result list
        rolling_maximums.append(current_max)

    return rolling_maximums