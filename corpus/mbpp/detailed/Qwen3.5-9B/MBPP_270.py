from typing import List, Any

def sum_even_and_even_index(numbers: List[Any], length_hint: int) -> int:
    """
    Calculates the sum of even numbers that are located at even positions (indices 0, 2, 4, ...)
    in the provided list.

    Args:
        numbers: A list of numbers to be processed.
        length_hint: An optional hint for the length of the list. If provided, it must match
                     the actual length of the list. If not provided or if it matches, it is validated.
                     This function primarily uses the actual length of the 'numbers' list for iteration,
                     but validates against 'length_hint' if present to catch inconsistencies early.

    Returns:
        The sum of elements that are both even in value and at an even index.

    Raises:
        TypeError: If 'numbers' is not a list or if any element in 'numbers' is not an integer.
        ValueError: If 'numbers' is empty, or if 'length_hint' is provided and does not match the
                    actual length of 'numbers'.

    Note:
        - "Even positions" refers to indices 0, 2, 4, 6, etc. (0-based indexing).
        - The function considers 0 to be an even number.
    """

    # --- Input Validation Phase ---

    # Check if the input is a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input 'numbers' must be a list, got {type(numbers).__name__}.")

    # Check if the list is empty
    if len(numbers) == 0:
        raise ValueError("Input list 'numbers' cannot be empty.")

    # Validate elements within the list
    for index, value in enumerate(numbers):
        if not isinstance(value, int) or isinstance(value, bool):
            # Explicitly exclude booleans since they are a subclass of int in Python
            raise TypeError(f"Element at index {index} is not an integer (got {type(value).__name__}).")

    # Validate the length_hint if provided
    actual_length = len(numbers)
    if length_hint is not None:
        if length_hint != actual_length:
            raise ValueError(
                f"Length hint ({length_hint}) does not match the actual length of the list ({actual_length})."
            )

    # --- Calculation Phase ---

    # Initialize the accumulator variable for the sum
    total_sum = 0

    # Iterate through the list.
    # We only need to visit even indices: 0, 2, 4, ...
    # Using a while loop allows explicit control flow without relying on slicing which copies data.
    current_index = 0
    list_length = actual_length

    while current_index < list_length:
        # Retrieve the current number at the even index
        current_number = numbers[current_index]

        # Check if the current number is even
        # Modulo operator (%) returns 0 for even numbers
        is_even_value = (current_number % 2) == 0

        if is_even_value:
            # Add the number to the running total
            total_sum += current_number

        # Move to the next even index (increment by 2)
        current_index += 2

    return total_sum