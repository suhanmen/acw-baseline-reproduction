from typing import Union

Number = Union[int, float]

def _validate_single_value(value: Number) -> None:
    """
    Validates that the provided value is a numeric type (int or float).
    Raises a TypeError with a descriptive message if validation fails.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(
            f"Invalid input type. Expected int or float, but got {type(value).__name__}."
        )

def _validate_arguments(a: Number, b: Number, c: Number) -> None:
    """
    Validates that all three arguments are valid numeric types.
    This centralizes validation logic to ensure consistency and provides
    clear error messages for the caller.
    """
    _validate_single_value(a)
    _validate_single_value(b)
    _validate_single_value(c)

def _compare_and_select_min(a: Number, b: Number, c: Number) -> Number:
    """
    Determines the minimum of three numbers using explicit comparison steps.

    Logic:
    1. Compare 'a' and 'b'. Let the smaller be 'temp_min'.
    2. Compare 'temp_min' and 'c'. The smaller is the final result.

    This approach avoids nested ternary operators and makes the flow clear.
    """
    # Step 1: Find the minimum of the first two numbers
    if a <= b:
        temp_min = a
    else:
        temp_min = b

    # Step 2: Compare the intermediate minimum with the third number
    if temp_min <= c:
        final_minimum = temp_min
    else:
        final_minimum = c

    return final_minimum

def min_of_three(a: Number, b: Number, c: Number) -> Number:
    """
    Finds the minimum of three numbers.

    This function accepts exactly three arguments, validates them strictly,
    and returns the smallest value among them. It handles negative numbers,
    zero, positive numbers, floating-point numbers, and cases where numbers
    are equal without issue.

    Parameters:
        a (Number): The first number.
        b (Number): The second number.
        c (Number): The third number.

    Returns:
        Number: The minimum value among a, b, and c.

    Raises:
        TypeError: If any argument is not an int or float.

    Examples:
        >>> min_of_three(10, 20, 0)
        0
        >>> min_of_three(19, 15, 18)
        15
        >>> min_of_three(-10, -20, -30)
        -30
        >>> min_of_three(5, 5, 5)
        5
    """
    # Explicit validation step
    _validate_arguments(a, b, c)

    # Execute the core logic
    result = _compare_and_select_min(a, b, c)

    return result