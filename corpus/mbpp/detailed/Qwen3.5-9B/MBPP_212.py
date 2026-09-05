from typing import Union

# Type alias for better readability in function signatures
InputNumber = Union[int, float]

def _validate_input(n: InputNumber) -> int:
    """
    Validates the input 'n' for the fourth power sum calculation.

    Rules:
    1. The input must be a number (int or float).
    2. The input must represent a natural number (non-negative integer).
    3. For the context of "n natural numbers", n=0 results in an empty sum (0).
    4. Negative inputs are invalid.

    Returns:
        The validated integer n.

    Raises:
        TypeError: If the input is not a number.
        ValueError: If the input is negative or not a whole number.
    """
    # Check type
    if not isinstance(n, (int, float)):
        raise TypeError(f"Input must be a number, but got type '{type(n).__name__}'.")

    # Convert to float first to handle potential integer inputs cleanly, then check properties
    n_float = float(n)

    # Check for NaN (not a number)
    if n_float != n_float:
        raise ValueError("Input cannot be NaN (Not a Number).")

    # Check for Infinity
    if abs(n_float) == float('inf'):
        raise ValueError("Input cannot be infinite.")

    # Check for negativity
    if n_float < 0:
        raise ValueError(f"Input must be non-negative, but got {n_float}.")

    # Check for whole number (natural number requirement)
    if n_float != int(n_float):
        raise ValueError(f"Input must be a whole number, but got {n_float}.")

    # Return as integer for calculations
    return int(n_float)

def _compute_fourth_power(base: int) -> int:
    """
    Computes the fourth power of a given integer base.

    Args:
        base: An integer to be raised to the power of 4.

    Returns:
        The result of base ** 4.
    """
    return base ** 4

def _compute_sum_of_powers(n: int) -> int:
    """
    Computes the sum of the fourth powers of the first n natural numbers.
    Formula: Sum_{i=1}^{n} i^4

    This function uses an explicit loop rather than a mathematical closed-form formula
    to ensure clarity, explicit step visibility, and direct correspondence to the
    problem statement of "n natural numbers".

    Args:
        n: The count of natural numbers (starting from 1).

    Returns:
        The integer sum of the fourth powers.

    Raises:
        ValueError: If n is less than 0.
    """
    total_sum: int = 0

    # Edge case: if n is 0, the sum of an empty set is 0. The loop range handles this naturally,
    # but we document the logic explicitly.
    if n < 0:
        raise ValueError("Cannot compute sum for a negative count of numbers.")

    # Iterate from 1 to n inclusive
    for current_number in range(1, n + 1):
        # Calculate the fourth power of the current number
        fourth_power_value: int = _compute_fourth_power(current_number)

        # Add to the running total
        total_sum = total_sum + fourth_power_value

    return total_sum

def fourth_Power_Sum(n: InputNumber) -> int:
    """
    Calculates the sum of the fourth power of the first n natural numbers.

    Definition:
        The sum of the fourth powers of the first n natural numbers is given by:
        S = 1^4 + 2^4 + 3^4 + ... + n^4

    Parameters:
        n (InputNumber): A non-negative integer representing the count of natural numbers.
                         The series starts at 1 and ends at n.

    Returns:
        int: The calculated sum of the fourth powers.

    Raises:
        TypeError: If n is not a numeric type.
        ValueError: If n is negative or not a whole number.

    Examples:
        >>> fourth_Power_Sum(2)
        17  # (1^4 + 2^4) = 1 + 16 = 17
        >>> fourth_Power_Sum(0)
        0   # Sum of zero terms
        >>> fourth_Power_Sum(1)
        1   # 1^4 = 1
    """
    # Step 1: Validate and normalize the input
    validated_n: int = _validate_input(n)

    # Step 2: Compute the sum using the helper function
    result: int = _compute_sum_of_powers(validated_n)

    # Step 3: Return the result
    return result