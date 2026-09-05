from typing import Tuple, Union

Number = Union[int, float]
TupleOfNumbers = Tuple[Number, ...]

def validate_tuple(input_name: str, data: TupleOfNumbers) -> TupleOfNumbers:
    """
    Validates that the input is a non-empty tuple of numbers.
    Raises a ValueError if the input is invalid.
    """
    if not isinstance(data, tuple):
        raise ValueError(f"Input for '{input_name}' must be a tuple, but got {type(data).__name__}.")

    if len(data) == 0:
        raise ValueError(f"Input for '{input_name}' cannot be an empty tuple.")

    for index, item in enumerate(data):
        if not isinstance(item, (int, float)):
            raise ValueError(
                f"Input for '{input_name}' at index {index} is not a number. "
                f"Expected int or float, but got {type(item).__name__}."
            )

    return data

def calculate_division_resultator(
    numerator: Number, 
    denominator: Number
) -> Number:
    """
    Calculates the division of the numerator by the denominator.
    Explicitly checks for division by zero.
    """
    if denominator == 0:
        raise ZeroDivisionError(
            f"Division by zero attempted: {numerator} / {denominator}."
        )

    # Perform the division
    result = numerator / denominator
    return result

def division_elements(
    tuples_of_numbers: Tuple[TupleOfNumbers, TupleOfNumbers]
) -> TupleOfNumbers:
    """
    Performs mathematical division operation across the given tuples.

    The function divides corresponding elements from the first tuple (numerator)
    by the corresponding elements from the second tuple (denominator).

    Args:
        tuples_of_numbers: A tuple containing exactly two tuples of numbers.
                           The first tuple is the dividend, the second is the divisor.

    Returns:
        A tuple of numbers resulting from the division of corresponding elements.

    Raises:
        ValueError: If the input structure or types are invalid.
        ZeroDivisionError: If any division by zero is attempted.
        AssertionError: If the two tuples have different lengths.
    """
    # Unpack the input tuple into numerator_tuple and denominator_tuple for clarity
    numerator_tuple, denominator_tuple = tuples_of_numbers

    # Validate both input tuples
    validate_tuple("numerator_tuple", numerator_tuple)
    validate_tuple("denominator_tuple", denominator_tuple)

    # Check that both tuples have the same length
    num_length = len(numerator_tuple)
    den_length = len(denominator_tuple)

    if num_length != den_length:
        raise ValueError(
            f"Both tuples must have the same length. "
            f"Numerator has {num_length} elements, denominator has {den_length} elements."
        )

    # Initialize an empty list to collect the results
    results: list[Number] = []

    # Iterate through the indices of the tuples
    for index in range(num_length):
        current_numerator = numerator_tuple[index]
        current_denominator = denominator_tuple[index]

        # Calculate the division for the current pair of numbers
        current_result = calculate_division_resultator(current_numerator, current_denominator)

        # Append the result to the results list
        results.append(current_result)

    # Convert the list of results back to a tuple to match the return type annotation
    return tuple(results)