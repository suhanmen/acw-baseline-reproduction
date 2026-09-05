from typing import Tuple, Any, Union

Number = Union[int, float]

def _validate_input_sequence(input_sequence: Any) -> Tuple[bool, str]:
    """
    Validates that the input is a sequence (but not a string) containing numbers.

    Returns:
        A tuple of (is_valid, error_message).
        is_valid is True if the input is valid, False otherwise.
        error_message is an empty string if valid, or a descriptive error string if invalid.
    """
    if not isinstance(input_sequence, (list, tuple)):
        return False, f"Input must be a tuple or list, but got {type(input_sequence).__name__}"

    # Explicitly exclude strings to prevent treating strings as sequences of characters
    if isinstance(input_sequence, str):
        return False, "Input must not be a string"

    for i, element in enumerate(input_sequence):
        if not isinstance(element, (int, float)):
            return False, f"Element at index {i} is not a number: {type(element).__name__}"

        # Check for NaN and Infinity which are technically floats but often invalid for arithmetic summing
        import math
        if isinstance(element, float):
            if math.isnan(element):
                return False, f"Element at index {i} is NaN"
            if math.isinf(element):
                return False, f"Element at index {i} is infinite"

    return True, ""

def _add_pairwise_core(elements: Tuple[Number, ...]) -> Tuple[Number, ...]:
    """
    Core logic to compute pairwise sums.
    Assumes input has already been validated.

    Calculates: elements[i] + elements[i+1] for all valid i.
    For a sequence of length n, produces n-1 results.
    """
    n = len(elements)

    # Handle edge case where input has fewer than 2 elements
    # Based on problem constraints and assertions, we expect at least 2 elements,
    # but this handles degenerate cases explicitly.
    if n < 2:
        # Returning an empty tuple is the most logical result for < 2 elements
        # as no pairs can be formed.
        return ()

    results = []

    # Explicit loop to avoid any list comprehension ambiguity for clarity
    for index in range(n - 1):
        current_element = elements[index]
        next_element = elements[index + 1]
        pairwise_sum = current_element + next_element
        results.append(pairwise_sum)

    return tuple(results)

def add_pairwise(tuples: Tuple) -> Tuple:
    """
    Finds the pairwise addition of the elements of the given tuples.

    This function takes a single tuple (or list) of numbers and returns a new tuple
    where each element is the sum of consecutive elements from the input.
    For an input (a, b, c, d), the output is (a+b, b+c, c+d).

    Args:
        tuples: A tuple containing numeric elements (int or float).

    Returns:
        A tuple of numbers representing the pairwise sums.

    Raises:
        TypeError: If the input is not a tuple/list or contains non-numeric elements.
    """
    is_valid, error_message = _validate_input_sequence(tuples)

    if not is_valid:
        raise TypeError(error_message)

    return _add_pairwise_core(tuple(tuples))