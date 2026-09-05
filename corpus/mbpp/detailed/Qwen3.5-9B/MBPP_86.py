from typing import Tuple, Union

# Define a custom type for the input to enforce that it is an integer.
# The return type is an integer, or None if the input is invalid.
InputType = Union[int, str, float, bool, None, object]


def _validate_input_index(index: InputType) -> Tuple[bool, int | None]:
    """
    Validates the provided index against strict rules for this problem.

    Rules:
    1. The input must be effectively an integer.
    2. The input must be greater than zero (positive integers only).

    Returns:
        A tuple of (is_valid, processed_value).
        is_valid is True if the input is valid.
        processed_value is the integer index if valid, otherwise None.
    """

    # Handle None explicitly
    if index is None:
        return False, None

    # Handle Boolean explicitly (since bool is a subclass of int in Python)
    # We want to reject booleans as inputs for clarity and type safety.
    if isinstance(index, bool):
        return False, None

    # Handle String inputs
    if isinstance(index, str):
        try:
            # Attempt to convert string to integer
            candidate_int = int(index)
        except ValueError:
            # Invalid string format
            return False, None

        # If conversion succeeds, we proceed to other checks on candidate_int
        return _validate_integer(candidate_int)

    # Handle Float inputs
    if isinstance(index, float):
        # Check if the float is actually a whole number (no fractional part)
        if not index.is_integer():
            return False, None

        # Convert to integer
        candidate_int = int(index)
        return _validate_integer(candidate_int)

    # Handle Integer inputs
    if isinstance(index, int):
        return _validate_integer(index)

    # Handle any other unexpected types
    return False, None


def _validate_integer(value: int) -> Tuple[bool, int | None]:
    """
    Helper to validate that an integer is positive (> 0).
    """
    if value <= 0:
        return False, None

    return True, value


def _calculate_centered_hexagonal_number(n: int) -> int:
    """
    Calculates the nth centered hexagonal number.

    Formula: H_n = 3 * n * (n - 1) + 1

    Steps:
    1. Multiply the input n by itself.
    2. Subtract 1 from the result.
    3. Multiply the input n by the result of step 2.
    4. Multiply the result of step 3 by 3.
    5. Add 1 to the final result.
    """

    # Step 1: Calculate n * n
    n_squared = n * n

    # Step 2: Subtract 1 from the square
    n_squared_minus_one = n_squared - 1

    # Step 3: Multiply n by (n - 1) using the calculated value
    n_times_n_minus_one = n * n_squared_minus_one

    # Step 4: Multiply by 3
    tripled_value = 3 * n_times_n_minus_one

    # Step 5: Add 1 to complete the formula
    result = tripled_value + 1

    return result


def centered_hexagonal_number(index: InputType) -> int:
    """
    Computes the nth centered hexagonal number for a given positive integer n.

    The centered hexagonal numbers are a sequence of figurate numbers that represent
    points in the shape of a hexagon with a center point and successive layers.

    The mathematical formula is:
        H_n = 3 * n * (n - 1) + 1

    Arguments:
        index: The position in the sequence (must be a positive integer, 1, 2, 3...).

    Returns:
        The nth centered hexagonal number as an integer.

    Raises:
        TypeError: If the input cannot be interpreted as a valid positive integer.
        ValueError: If the input is a valid integer but not positive (e.g., 0 or negative).

    Note:
        If validation fails, a TypeError or ValueError is raised with a descriptive message
        rather than returning None or raising a generic exception, ensuring the caller
        knows exactly what went wrong.
    """

    # Step 1: Validate the input
    is_valid, processed_n = _validate_input_index(index)

    # Step 2: Check validation result
    if not is_valid:
        if processed_n is None:
            raise TypeError(
                f"Invalid input '{index}'. The input must be a positive integer."
            )
        else:
            # This branch theoretically shouldn't be reached due to tuple logic above,
            # but serves as a safety net if the validation logic changes.
            raise TypeError(
                f"Invalid input type '{type(index).__name__}'. The input must be a positive integer."
            )

    # Step 3: Perform the calculation using the validated integer
    result = _calculate_centered_hexagonal_number(processed_n)

    # Step 4: Return the result
    return result