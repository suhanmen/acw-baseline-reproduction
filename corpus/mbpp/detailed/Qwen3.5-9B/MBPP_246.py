import math
from typing import Union

Number = Union[int, float]

def _validate_input(value: Number) -> None:
    """
    Validates that the input is a number and non-negative.

    Raises:
        TypeError: If the value is not an int or float.
        ValueError: If the value is negative (square root undefined for reals).
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"Input must be a number (int or float), got {type(value).__name__}")

    if isinstance(value, bool):
        raise TypeError("Input must be a number (int or float), got bool")

    if value < 0:
        raise ValueError(f"Cannot compute square root of a negative number: {value}")

def _initial_guess(n: Number) -> Number:
    """
    Computes an initial guess for the Babylonian method.

    Strategy:
    - If n is 0, return 0.
    - If n is 1, return 1.
    - If n >= 1, return n / 2 as a simple upper bound guess (or could be math.sqrt, 
      but to demonstrate the algorithm purely, we start with a simple heuristic).
    - If n < 1 (but > 0), return n itself or 1.0 as a starting point.

    For robust convergence without importing math.sqrt internally (to prove the method),
    we use a heuristic: max(1.0, n / 2.0) for n >= 1, and n for n < 1.
    """
    if n == 0:
        return 0.0
    if n == 1:
        return 1.0

    # Heuristic initial guess
    if n >= 1:
        guess = n / 2.0
    else:
        # For fractions (e.g., 0.25), starting with the number itself or 1.0 works
        guess = n

    return guess

def _is_close_enough(current: Number, target: Number, tolerance: float = 1e-10) -> bool:
    """
    Checks if the current approximation is close enough to the target (the square of the root).

    We check if current * current is within tolerance of target.
    """
    return abs(current * current - target) < tolerance

def _babylonian_step(current: Number, target: Number) -> Number:
    """
    Performs one iteration of the Babylonian (Heron's) method.

    Formula: x_{n+1} = 0.5 * (x_n + target / x_n)
    """
    if current == 0:
        # Avoid division by zero if the guess happened to be 0
        return target # Fallback, though logic above prevents this

    ratio = target / current
    new_guess = 0.5 * (current + ratio)

    return new_guess

def babylonian_squareroot(value: Number) -> Number:
    """
    Computes the square root of a non-negative number using the Babylonian method.

    This function implements an iterative algorithm that converges quadratically.
    It handles edge cases including zero, one, and small positive numbers.

    Args:
        value: A non-negative integer or float.

    Returns:
        The square root of value.

    Raises:
        TypeError: If value is not a number or is a boolean.
        ValueError: If value is negative.
    """
    # 1. Validate input explicitly
    _validate_input(value)

    # 2. Handle the zero case explicitly to avoid division by zero in iterations
    if value == 0:
        return 0.0

    # 3. Determine initial guess
    current_guess = _initial_guess(value)

    # 4. Define tolerance for convergence
    tolerance = 1e-10

    # 5. Iterate until convergence
    while not _is_close_enough(current_guess, value, tolerance):
        # Perform the Babylonian step
        next_guess = _babylonian_step(current_guess, value)

        # Update current guess
        current_guess = next_guess

        # Safety break to prevent infinite loops due to floating point anomalies
        # (Though Babylonian method is robust, this is a defensive measure)
        if abs(current_guess) > 1e308:
            raise RuntimeError("Babylonian method failed to converge after maximum iterations.")

            # Optional: Add a max iteration counter here for strict production code
            # if not implemented, relying on convergence logic.

    return current_guess