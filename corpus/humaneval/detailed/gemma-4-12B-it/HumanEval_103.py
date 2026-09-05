import math

def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    # Validate input types: ensure both n and m are integers
    if not isinstance(n, int) or not isinstance(m, int):
        raise TypeError("Inputs n and m must be integers.")

    # Handle the condition where n is greater than m
    if n > m:
        return -1

    # The problem specifies n and m are positive integers.
    # We check for non-positive inputs to ensure robustness.
    if n <= 0 or m <= 0:
        # Depending on interpretation, we could return -1 or raise an error.
        # Given "positive integers" in the prompt, we treat them as valid inputs.
        pass

    # Calculate the number of terms in the sequence from n to m inclusive.
    # If n=1 and m=5, the terms are {1, 2, 3, 4, 5}, so count is 5.
    count = m - n + 1

    # Calculate the sum of the arithmetic progression from n to m.
    # Formula for sum of an arithmetic series: Sum = (count / 2) * (first_term + last_term)
    # We use integer arithmetic where possible, but the average might be a float.
    first_term = n
    last_term = m
    total_sum = (count * (first_term + last_term)) // 2

    # Calculate the exact average.
    # We use float division here to ensure precision before rounding.
    actual_average = total_sum / count

    # Round the average to the nearest integer.
    # Python's round() function uses "round half to even". 
    # To ensure standard "round half up" behavior (standard in most math contexts),
    # we can use floor(x + 0.5).
    rounded_value = int(math.floor(actual_average + 0.5))

    # Convert the resulting integer to a binary string representation.
    # bin() returns a string prefixed with '0b'.
    binary_representation = bin(rounded_value)

    return binary_representation