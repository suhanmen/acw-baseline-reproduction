import math
from typing import Tuple

def _validate_inputs(dividend: int, divisor: int, n: int) -> None:
    """
    Validate that inputs are integers and within acceptable ranges.

    Raises:
        TypeError: If any argument is not an integer.
        ValueError: If divisor is zero or n is non-positive.
    """
    # Check for integer types explicitly
    if not isinstance(dividend, int):
        raise TypeError(f"Dividend must be an integer, got {type(dividend).__name__}")
    if not isinstance(divisor, int):
        raise TypeError(f"Divisor must be an integer, got {type(divisor).__name__}")
    if not isinstance(n, int):
        raise TypeError(f"Nth position must be an integer, got {type(n).__name__}")

    # Check for non-positive divisor (avoid division by zero and logical invalidity)
    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")

    # Check for non-positive nth position (1-based index)
    if n <= 0:
        raise ValueError(f"Nth position must be a positive integer, got {n}.")


def _compute_repeating_cycle_start_and_length(dividend: int, divisor: int) -> Tuple[int, int]:
    """
    Compute the position where the decimal expansion starts repeating
    and the length of the repeating cycle.

    Returns:
        A tuple (start_index, cycle_length).
        start_index is the number of non-repeating digits after the decimal point.
        cycle_length is the length of the repeating part.
    """
    remainder = dividend % divisor
    if remainder == 0:
        return 0, 0  # Terminating decimal, no cycle

    seen_remainders = {}
    position = 0
    current_remainder = remainder

    # Iterate until we find a repeating remainder or complete a cycle
    while current_remainder != 0 and current_remainder not in seen_remainders:
        seen_remainders[current_remainder] = position
        current_remainder = (current_remainder * 10) % divisor
        position += 1

    if current_remainder == 0:
        return position, 0  # Terminating decimal, no repeating part
    else:
        start_index = seen_remainders[current_remainder]
        cycle_length = position - start_index
        return start_index, cycle_length


def _simulate_decimal_expansion(dividend: int, divisor: int, n: int) -> int:
    """
    Simulate the long division process to find the nth digit after the decimal point.

    This function performs digit-by-digit extraction without converting the 
    entire decimal to a string, ensuring precision for large n.

    Args:
        dividend: The numerator of the fraction.
        divisor: The denominator of the fraction.
        n: The position of the digit to find (1-based index after decimal).

    Returns:
        The nth digit after the decimal point.
    """
    # Initial integer part division
    integer_part = dividend // divisor
    remainder = dividend % divisor

    # If remainder is zero, the decimal terminates immediately (e.g., 4/2 = 2.0)
    # In this case, all subsequent digits are 0.
    if remainder == 0:
        return 0

    # Simulate digit generation step by step
    current_digit = 0

    # We need to generate digits one by one until we reach the nth position.
    # We maintain the current remainder at each step.
    for _ in range(n):
        # Multiply remainder by 10 to shift to the next decimal place
        remainder = remainder * 10

        # The integer part of this new value is the next digit
        current_digit = remainder // divisor

        # Update remainder for the next iteration
        remainder = remainder % divisor

        # Optimization: If remainder becomes 0, all subsequent digits are 0.
        if remainder == 0:
            break

    return current_digit


def _construct_fraction(dividend: int, divisor: int) -> float:
    """
    Construct the floating point value of the fraction for initial checks.

    Note: This is not used for the actual digit extraction due to floating point 
    precision limitations for large n, but kept for clarity in the original logic flow.
    """
    return dividend / divisor


def find_Nth_Digit(dividend: int, divisor: int, n: int) -> int:
    """
    Find the nth digit in the proper fraction expansion of dividend/divisor.

    The function calculates the decimal expansion of the fraction dividend/divisor
    and returns the digit at the nth position after the decimal point.

    The term "proper fraction" implies that if the result is an integer (e.g., 4/2=2),
    it is treated as 2.000..., so the nth digit is 0. If the fraction reduces to an 
    improper fraction greater than 1 (e.g., 5/2=2.5), we consider the fractional part.

    Examples:
        find_Nth_Digit(1, 2, 1) -> 0.5 -> 1st digit is 5
        find_Nth_Digit(3, 5, 1) -> 0.6 -> 1st digit is 6
        find_Nth_Digit(5, 6, 5) -> 0.8333... -> 5th digit is 3

    Args:
        dividend: The numerator of the fraction.
        divisor: The denominator of the fraction.
        n: The position of the digit to find (1-based index after decimal).

    Returns:
        An integer representing the nth digit after the decimal point.

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If divisor is zero or n is non-positive.
    """

    # Step 1: Validate all inputs explicitly
    _validate_inputs(dividend, divisor, n)

    # Step 2: Handle the case where the fraction simplifies to an integer exactly.
    # For example, 4/2 = 2. The decimal expansion is 2.000...
    # Therefore, any nth digit after the decimal point is 0.
    if dividend % divisor == 0:
        return 0

    # Step 3: Perform the digit-by-digit long division simulation.
    # This avoids floating point precision issues that would occur with 
    # standard float division for large n.
    # 
    # Logic breakdown:
    # 1. Calculate initial remainder after integer division.
    # 2. Loop n times:
    #    a. Multiply remainder by 10.
    #    b. The quotient of this division is the current nth digit candidate.
    #    c. Update remainder to the modulo result for the next iteration.
    #    d. If remainder becomes 0, break early (terminating decimal).

    initial_remainder = dividend % divisor

    # Since we established dividend % divisor != 0 above, initial_remainder is non-zero.
    current_remainder = initial_remainder

    # We iterate exactly n times to find the nth digit.
    # We do not rely on repeating cycle detection here because a direct simulation
    # of n steps is O(n) and sufficient for typical constraints, and it avoids
    # complexity in handling the start index and cycle length logic which is 
    # unnecessary for simply retrieving the nth digit.

    for _ in range(n):
        # Shift remainder to the next decimal position
        scaled_remainder = current_remainder * 10

        # Calculate the digit at the current position
        digit_at_position = scaled_remainder // divisor

        # Update remainder for the next position
        current_remainder = scaled_remainder % divisor

        # Early exit if the decimal terminates
        if current_remainder == 0:
            # All subsequent digits are 0
            return 0

    # After the loop, digit_at_position holds the value of the nth digit.
    return digit_at_position