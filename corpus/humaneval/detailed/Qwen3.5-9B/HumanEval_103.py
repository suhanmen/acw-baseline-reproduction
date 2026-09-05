import math

def _validate_inputs(n, m):
    """
    Validates that n and m are positive integers and that n is not greater than m.

    Raises:
        TypeError: If either n or m is not an integer.
        ValueError: If either n or m is not positive, or if n > m.
    """
    if not isinstance(n, int) or not isinstance(m, int):
        raise TypeError("Both n and m must be integers.")

    if n <= 0 or m <= 0:
        raise ValueError("Both n and m must be positive integers.")

    if n > m:
        return True  # Signal that the degenerate case (n > m) is handled here

    return False

def _compute_sum_range(n, m):
    """
    Computes the sum of integers from n to m inclusive.
    Uses the arithmetic series formula: Sum = (number_of_terms * (first_term + last_term)) // 2
    """
    count = m - n + 1
    total_sum = (count * (n + m)) // 2
    return total_sum

def _compute_average(total_sum, count):
    """
    Computes the exact average as a float.
    """
    exact_average = total_sum / count
    return exact_average

def _round_to_nearest_integer(value):
    """
    Rounds a float to the nearest integer using standard rounding rules.
    Uses Python's math.floor or round behavior appropriately for .5 cases.
    Note: Python's built-in round() rounds .5 to the nearest even number (Banker's rounding).
    The problem statement example suggests standard rounding (e.g., 2.5 -> 3, 3.5 -> 4).
    We will use the standard mathematical rule: add 0.5 and floor.
    """
    if value >= 0:
        return math.floor(value + 0.5)
    else:
        return math.ceil(value - 0.5)

def _integer_to_binary_string(number):
    """
    Converts a non-negative integer to its binary string representation prefixed with '0b'.
    """
    if number == 0:
        return "0b0"
    return bin(number)

def rounded_avg(n, m):
    """
    You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.

    Args:
        n (int): The starting positive integer.
        m (int): The ending positive integer.

    Returns:
        str or int: The binary string representation of the rounded average, 
                    or -1 if n > m.
    """
    # Step 1: Validate inputs and handle the degenerate case where n > m
    # We do not raise an exception for n > m per the problem statement ("return -1"),
    # but we handle it explicitly before any calculation.

    # Explicit check for the condition described in the docstring
    if n > m:
        return -1

    # Step 2: Calculate the count of numbers in the range [n, m]
    count = m - n + 1

    # Step 3: Calculate the sum of the range [n, m]
    total_sum = _compute_sum_range(n, m)

    # Step 4: Calculate the exact average
    exact_average = _compute_average(total_sum, count)

    # Step 5: Round the average to the nearest integer
    rounded_value = _round_to_nearest_integer(exact_average)

    # Step 6: Convert the rounded integer to a binary string
    binary_result = _integer_to_binary_string(rounded_value)

    return binary_result