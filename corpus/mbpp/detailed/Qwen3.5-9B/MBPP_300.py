from math import comb
from typing import Union

Number = Union[int, float]


def count_binary_sequences(n: Number) -> Number:
    """
    Calculate the count of all binary sequences of length 2n such that
    the sum of the first n bits is the same as the sum of the last n bits.

    A binary sequence consists of only 0s and 1s.
    For a sequence of length 2n, we split it into two halves, each of length n.
    Let k be the number of 1s in the first half.
    The condition requires that the second half also has exactly k 1s.

    For a specific k (where 0 <= k <= n):
    - The number of ways to arrange k 1s in the first half of length n is C(n, k).
    - The number of ways to arrange k 1s in the second half of length n is C(n, k).
    - The total ways for a specific k is C(n, k) * C(n, k).

    The total count is the sum over all possible k from 0 to n:
    Sum_{k=0}^{n} [ C(n, k) * C(n, k) ]

    This formula is also known as the central binomial coefficient squared summed,
    or equivalently the coefficient of x^n in (1+x)^(2n) if considering specific properties,
    but the direct summation of (C(n,k))^2 is the most straightforward combinatorial derivation.
    Specifically, Sum_{k=0}^{n} C(n, k)^2 = C(2n, n).

    However, to adhere strictly to the requirement of spelling out steps and handling logic explicitly
    without relying on the pre-known identity shortcut (to ensure clarity and defensive coding),
    we will iterate and sum the products of combinations.

    Input validation ensures n is a non-negative integer.

    Args:
        n: A non-negative integer representing the half-length of the binary sequence.
           The total sequence length is 2n.

    Returns:
        A float representing the count of valid binary sequences.
        The problem constraints assert float equality, so we cast the result to float.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """

    # Step 1: Validate the input type.
    # n must be an integer according to the problem description (length 2n implies discrete steps).
    # We accept int but reject bool specifically because bool is a subclass of int in Python.
    if isinstance(n, bool):
        raise TypeError("Parameter 'n' must be an integer, not a boolean.")

    if not isinstance(n, int):
        raise TypeError(f"Parameter 'n' must be an integer, got {type(n).__name__}.")

    # Step 2: Validate the input value range.
    # A length cannot be negative, and since the sequence has length 2n, n must be >= 0.
    if n < 0:
        raise ValueError(f"Parameter 'n' must be non-negative, got {n}.")

    # Step 3: Handle the edge case where n is 0.
    # If n is 0, the total length is 0. There is exactly one binary sequence of length 0 (the empty sequence).
    # The sum of the first 0 bits is 0, and the sum of the last 0 bits is 0. They are equal.
    # C(0, 0) * C(0, 0) = 1 * 1 = 1.
    if n == 0:
        return float(1)

    # Step 4: Initialize the accumulator variable.
    # This will hold the running total of valid sequence counts.
    total_valid_sequences = 0

    # Step 5: Iterate through all possible counts of 1s in the first half.
    # Let k be the number of 1s. k can range from 0 to n inclusive.
    # We treat this loop as the primary control flow mechanism.
    for k in range(0, n + 1):

        # Step 6: Calculate the number of ways to choose k positions for 1s in the first half.
        # This is the binomial coefficient "n choose k".
        ways_first_half = comb(n, k)

        # Step 7: Calculate the number of ways to choose k positions for 1s in the second half.
        # Since the condition requires the second half to have the same sum k,
        # the calculation is identical to the first half.
        ways_second_half = comb(n, k)

        # Step 8: Calculate the number of ways for this specific k.
        # Since the choices for the first half and second half are independent,
        # we multiply the counts.
        ways_for_k = ways_first_half * ways_second_half

        # Step 9: Add the current configuration count to the total accumulator.
        total_valid_sequences += ways_for_k

    # Step 10: Convert the final integer result to a float to match the assertion expectations.
    result = float(total_valid_sequences)

    # Step 11: Return the calculated result.
    return result