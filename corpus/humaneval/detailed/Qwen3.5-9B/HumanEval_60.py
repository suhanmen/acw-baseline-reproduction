from typing import Union

# Define a type alias for clarity in type checking, although the function signature uses int.
# This allows us to be explicit about the expected domain.
Number = int

def _validate_input_argument(value: Union[int, float, str, list, tuple, dict, None]) -> Number:
    """
    Validates that the provided value is a non-negative integer.

    This function explicitly checks the type and the value constraints.
    It raises a ValueError if the input does not meet the requirements.

    Args:
        value: The value to validate.

    Returns:
        The validated integer value.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the integer is negative.
    """
    # Check if the value is an instance of the expected type.
    # We explicitly check for int to ensure booleans (which are subclasses of int)
    # are handled correctly if necessary, though typically bools should be rejected
    # for mathematical sequences unless specified otherwise.
    if type(value) is not int:
        raise TypeError(
            f"Invalid type provided: {type(value).__name__}. "
            "Expected an integer (int)."
        )

    # Check for boolean type explicitly, as bool is a subclass of int in Python.
    if isinstance(value, bool):
        raise TypeError(
            "Invalid value provided: boolean values are not accepted. "
            "Expected an integer."
        )

    # Check the numeric value constraint (must be non-negative for the 1 to n sequence).
    # The problem implies summing from 1 to n. If n is less than 1, the sum is 0.
    if value < 0:
        raise ValueError(
            f"Invalid value provided: {value}. "
            "The input must be a non-negative integer (>= 0)."
        )

    return value

def _compute_summation(start: Number, end: Number) -> Number:
    """
    Computes the sum of integers from 'start' to 'end' inclusive using an iterative loop.

    This function implements the summation logic explicitly with named variables
    and separate steps to ensure clarity and maintainability.

    Args:
        start: The starting integer of the sequence (inclusive).
        end: The ending integer of the sequence (inclusive).

    Returns:
        The sum of integers from start to end. If start > end, returns 0.
    """
    # Initialize the accumulator variable to hold the running total.
    total_sum = 0

    # Check the boundary condition where the start is greater than the end.
    # This handles cases where validation passed but logical bounds are inverted,
    # or if the function is called with start > end for other purposes.
    if start > end:
        return 0

    # Iterate through the range from 'start' to 'end'.
    # We use a while loop to explicitly demonstrate control flow rather than relying
    # solely on a single-line sum(range(...)) which, while efficient, hides the steps.
    current_number = start

    while current_number <= end:
        # Add the current number to the total.
        total_sum += current_number

        # Increment the current number for the next iteration.
        current_number += 1

    return total_sum

def sum_to_n(n: int) -> int:
    """
    Calculates the sum of all integers from 1 to n (inclusive).

    This function includes robust input validation and uses helper functions
    to decompose the logic into explicit, readable steps. It adheres to the
    problem description which defines the summation range as 1 to n.

    Edge cases handled:
    - n = 0: Returns 0 (empty sum).
    - n < 0: Raises ValueError.
    - Non-integer types: Raises TypeError.

    Args:
        n: The upper bound of the summation sequence. Must be a non-negative integer.

    Returns:
        The sum of integers from 1 to n.

    Raises:
        TypeError: If 'n' is not an integer (or is a boolean).
        ValueError: If 'n' is a negative number.

    Examples:
        >>> sum_to_n(30)
        465
        >>> sum_to_n(100)
        5050
        >>> sum_to_n(5)
        15
        >>> sum_to_n(10)
        55
        >>> sum_to_n(1)
        1
        >>> sum_to_n(0)
        0
    """
    # Step 1: Validate the input argument.
    # This ensures we have a valid, non-negative integer before proceeding.
    validated_n = _validate_input_argument(n)

    # Step 2: Determine the effective range.
    # The mathematical definition is sum from 1 to n.
    start_of_range = 1
    end_of_range = validated_n

    # Step 3: Compute the summation using the explicit helper function.
    result = _compute_summation(start_of_range, end_of_range)

    return result