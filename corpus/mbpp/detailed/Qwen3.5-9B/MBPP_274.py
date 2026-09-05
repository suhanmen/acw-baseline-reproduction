from math import comb
from typing import Union

def _validate_n(n: Union[int, float]) -> int:
    """
    Validates that the input n is a non-negative integer.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    # Check if n is an integer
    if isinstance(n, bool):
        raise TypeError("Input must be an integer, not a boolean.")

    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}.")

    # Check if n is non-negative
    if n < 0:
        raise ValueError(f"Input must be a non-negative integer, got {n}.")

    return n

def _compute_even_index_binomial_sum(n: int) -> int:
    """
    Computes the sum of binomial coefficients at even indices for a given n.

    The sum is defined as: C(n, 0) + C(n, 2) + C(n, 4) + ...
    where C(n, k) is the binomial coefficient "n choose k".
    The summation continues as long as the index k is less than or equal to n.

    Algorithm:
    1. Initialize a running total to zero.
    2. Iterate through even indices starting from 0 up to n (inclusive).
    3. For each even index k, calculate C(n, k) and add it to the total.
    4. Return the final total.

    Note: This function uses an explicit loop and named variables for clarity
    and readability, avoiding mathematical shortcuts like (2**(n-1)) for this specific
    implementation to adhere to the requirement of explicit steps.
    """

    # Initialize the accumulator for the sum
    even_index_sum = 0

    # Start the index k at 0 (the first even index)
    k = 0

    # Loop while the current index k is less than or equal to n
    # We ensure k does not exceed n to avoid calculating out-of-bounds coefficients
    while k <= n:
        # Calculate the binomial coefficient C(n, k)
        # The comb function from math module is used for exact integer arithmetic
        current_coefficient = comb(n, k)

        # Add the current coefficient to the running sum
        even_index_sum = even_index_sum + current_coefficient

        # Increment k by 2 to move to the next even index
        # This ensures we only process indices 0, 2, 4, ...
        k = k + 2

    return even_index_sum

def even_binomial_Coeff_Sum(n: Union[int, float]) -> int:
    """
    Finds the sum of even index binomial coefficients for a given non-negative integer n.

    Parameters:
        n (Union[int, float]): The upper value of the binomial coefficient.
                               Must be a non-negative integer.

    Returns:
        int: The sum of binomial coefficients C(n, k) where k is even.
             Formula: Sum(C(n, k)) for k in {0, 2, 4, ...} such that k <= n.

    Raises:
        TypeError: If n is not an integer (including floats or booleans).
        ValueError: If n is negative.

    Examples:
        For n = 4:
        Indices: 0, 1, 2, 3, 4
        Coeffs:  1, 4, 6, 4, 1
        Even Indices (0, 2, 4): 1 + 6 + 1 = 8

        For n = 6:
        Indices: 0, 1, 2, 3, 4, 5, 6
        Coeffs:  1, 6, 15, 20, 15, 6, 1
        Even Indices (0, 2, 4, 6): 1 + 15 + 15 + 1 = 32
    """

    # Step 1: Validate the input n
    # We explicitly handle the conversion or check to ensure type safety
    validated_n = _validate_n(n)

    # Step 2: Call the computation helper with the validated integer
    result = _compute_even_index_binomial_sum(validated_n)

    # Step 3: Return the computed result
    return result