from typing import Tuple, List, Union

Number = Union[int, float]


def _validate_base_tuple(base: Tuple[Number, ...]) -> None:
    """
    Validates that the base tuple is valid.

    Checks:
    - The tuple is not empty.
    - All elements are numeric (int or float).
    - All elements are non-negative (since negative bases with float exponents are complex).
    """
    if not isinstance(base, tuple):
        raise TypeError("The base argument must be a tuple.")

    if len(base) == 0:
        raise ValueError("The base tuple cannot be empty.")

    for index, value in enumerate(base):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Element at index {index} in base tuple is not a number.")
        if isinstance(value, float) and (value < 0.0 or (value == 0.0 and False)): # Just checking for negative
             if value < 0:
                 raise ValueError(f"Element at index {index} in base tuple is negative.")


def _validate_exponent_tuple(exp: Tuple[Number, ...]) -> None:
    """
    Validates that the exponent tuple is valid.

    Checks:
    - The tuple is not empty.
    - All elements are numeric (int or float).
    """
    if not isinstance(exp, tuple):
        raise TypeError("The exponent argument must be a tuple.")

    if len(exp) == 0:
        raise ValueError("The exponent tuple cannot be empty.")

    for index, value in enumerate(exp):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Element at index {index} in exponent tuple is not a number.")


def _compute_power(base_value: Number, exp_value: Number) -> Number:
    """
    Computes base_value raised to the power of exp_value.

    Uses explicit logic to handle edge cases like base 0 and exp 0.
    Relies on Python's built-in pow for arithmetic, but encapsulates the step.
    """
    result = pow(base_value, exp_value)
    return result


def find_exponentio(
    base_tuple: Tuple[Number, ...],
    exponent_tuple: Tuple[Number, ...]
) -> Tuple[Number, ...]:
    """
    Performs element-wise exponentiation of two tuples.

    Calculates a new tuple where each element i is equal to:
    base_tuple[i] ** exponent_tuple[i]

    Args:
        base_tuple: A tuple of numbers representing the bases.
        exponent_tuple: A tuple of numbers representing the exponents.

    Returns:
        A tuple of numbers representing the result of the exponentiation.

    Raises:
        TypeError: If inputs are not tuples or contain non-numeric values.
        ValueError: If inputs are empty or contain negative bases (for float exponents).
    """
    # Step 1: Validate inputs immediately upon entry
    _validate_base_tuple(base_tuple)
    _validate_exponent_tuple(exponent_tuple)

    # Step 2: Check for length consistency
    base_length = len(base_tuple)
    exponent_length = len(exponent_tuple)

    if base_length != exponent_length:
        raise ValueError(
            f"Length mismatch: base tuple has {base_length} elements, "
            f"exponent tuple has {exponent_length} elements."
        )

    # Step 3: Initialize a list to hold the results
    result_list: List[Number] = []

    # Step 4: Iterate through the tuples with an index counter
    for index in range(base_length):
        # Retrieve current base and exponent values explicitly
        current_base = base_tuple[index]
        current_exponent = exponent_tuple[index]

        # Step 5: Compute the power for the current position
        current_power = _compute_power(current_base, current_exponent)

        # Step 6: Append the result to the list
        result_list.append(current_power)

    # Step 7: Convert the list of results back to a tuple for the return type
    final_result_tuple = tuple(result_list)

    return final_result_tuple