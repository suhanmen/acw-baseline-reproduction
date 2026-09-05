import sys

def _validate_input_sequence(sequence):
    """
    Validates that the input is a non-empty sequence of numbers.

    Returns:
        The input sequence if valid.

    Raises:
        TypeError: If the input is not a sequence or contains non-numeric elements.
        ValueError: If the input sequence is empty.
    """
    if sequence is None:
        raise TypeError("Input cannot be None")

    # Check if the object is iterable but not a string (to allow list, tuple, etc.)
    try:
        iter(sequence)
    except TypeError:
        raise TypeError("Input must be an iterable sequence of numbers, not a single value")

    # We do not want to treat strings as sequences of numbers
    if isinstance(sequence, str):
        raise TypeError("Input must be a sequence of numbers, not a string")

    # Check for empty sequence
    try:
        next(iter(sequence))
    except StopIteration:
        raise ValueError("Input sequence cannot be empty")

    # Validate that every element is a number (int or float)
    for index, element in enumerate(sequence):
        if isinstance(element, bool):
            raise TypeError(f"Element at index {index} is a boolean, which is not a valid number.")
        if not isinstance(element, (int, float)):
            raise TypeError(f"Element at index {index} is not a number: {element!r} (type: {type(element).__name__})")

    return sequence

def _find_min_value(sequence):
    """
    Finds and returns the minimum value in the given sequence.

    Args:
        sequence (list or tuple): A validated sequence of numbers.

    Returns:
        float or int: The smallest number in the sequence.
    """
    current_min_value = None

    for element in sequence:
        if current_min_value is None:
            # Initialize with the first element
            current_min_value = element
        else:
            # Explicit comparison to update minimum
            if element < current_min_value:
                current_min_value = element

    return current_min_value

def _find_max_value(sequence):
    """
    Finds and returns the maximum value in the given sequence.

    Args:
        sequence (list or tuple): A validated sequence of numbers.

    Returns:
        float or int: The largest number in the sequence.
    """
    current_max_value = None

    for element in sequence:
        if current_max_value is None:
            # Initialize with the first element
            current_max_value = element
        else:
            # Explicit comparison to update maximum
            if element > current_max_value:
                current_max_value = element

    return current_max_value

def big_sum(array):
    """
    Calculates the sum of the largest and smallest values in a given array.

    This function performs rigorous input validation and handles edge cases
    explicitly without relying on built-in min/max functions that might obscure
    the algorithmic steps required for this specific defensive programming exercise.

    Args:
        array (list or tuple): A sequence of numerical values.

    Returns:
        float or int: The sum of the maximum and minimum values found in the array.

    Raises:
        TypeError: If the input is not a sequence of numbers.
        ValueError: If the input sequence is empty.
    """
    # Step 1: Validate the input data structure and types
    validated_data = _validate_input_sequence(array)

    # Step 2: Find the smallest value in the validated data
    smallest_value = _find_min_value(validated_data)

    # Step 3: Find the largest value in the validated data
    largest_value = _find_max_value(validated_data)

    # Step 4: Calculate the sum of the largest and smallest values
    result_sum = smallest_value + largest_value

    return result_sum