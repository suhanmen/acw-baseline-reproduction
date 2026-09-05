import math
from typing import Tuple, Union

def _validate_inputs(n: int, k: int) -> None:
    """
    Validates that the inputs n and k are integers and satisfy the constraints:
    n >= 0 and 0 <= k <= n.

    Raises a ValueError if the inputs are invalid.
    """
    # Check if inputs are integers
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("Both n and k must be integers.")

    # Check for negative n
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    # Check for negative k
    if k < 0:
        raise ValueError("k must be a non-negative integer.")

    # Check if k is greater than n
    if k > n:
        raise ValueError("k cannot be greater than n.")

    # Optimization: Use the symmetry property C(n, k) == C(n, n-k)
    # This reduces the number of multiplications/divisions when k > n/2
    effective_k = min(k, n - k)

def _compute_factorial_safe(value: int) -> int:
    """
    Computes the factorial of a non-negative integer value.

    Since n is already validated to be non-negative, we assume value >= 0.
    Returns value! 
    """
    result = 1
    for i in range(2, value + 1):
        result = result * i
    return result

def _compute_binomial_via_factorials(n: int, k: int) -> int:
    """
    Computes the binomial coefficient C(n, k) using the factorial formula:
    C(n, k) = n! / (k! * (n - k)!)

    This is the standard definition and is used here for clarity,
    though a multiplicative approach is often more numerically stable for very large n.
    For typical integer sizes within Python's arbitrary precision limits,
    this direct calculation is safe and clear.
    """
    n_factorial = _compute_factorial_safe(n)
    k_factorial = _compute_factorial_safe(k)
    nk_factorial = _compute_factorial_safe(n - k)

    return n_factorial // (k_factorial * nk_factorial)

def _compute_binomial_multiplicative(n: int, k: int) -> int:
    """
    Computes the binomial coefficient C(n, k) using a multiplicative approach:
    C(n, k) = product(n - i) / product(i + 1) for i in 0..k-1

    This approach avoids calculating huge factorials, although Python handles them fine.
    It is implemented explicitly to show the step-by-step logic.
    """
    # We use the symmetry property to minimize iterations
    # C(n, k) == C(n, n-k), so we compute C(n, min(k, n-k))
    effective_k = min(k, n - k)

    result_numerator = 1
    result_denominator = 1

    # Loop from 1 to effective_k
    # Formula step: multiply numerator by (n - i) and denominator by i
    # We iterate i from 1 to effective_k
    # Corresponding term in numerator is (n - i + 1)
    # Corresponding term in denominator is i

    for i in range(1, effective_k + 1):
        numerator_term = n - i + 1
        denominator_term = i

        result_numerator = result_numerator * numerator_term
        result_denominator = result_denominator * denominator_term

    # Perform integer division at the end
    # Mathematically, the result is guaranteed to be an integer
    final_result = result_numerator // result_denominator

    return final_result

def binomial_Coeff(n: int, k: int) -> int:
    """
    Calculates the binomial coefficient C(n, k), also known as "n choose k".

    This function represents the number of ways to choose k elements from a set 
    of n distinct elements.

    Formula: C(n, k) = n! / (k! * (n-k)!)

    Args:
        n (int): The total number of items (must be non-negative).
        k (int): The number of items to choose (must be between 0 and n inclusive).

    Returns:
        int: The binomial coefficient.

    Raises:
        TypeError: If n or k are not integers.
        ValueError: If n is negative, k is negative, or k > n.
    """
    # Step 1: Validate inputs immediately
    _validate_inputs(n, k)

    # Step 2: Handle the edge case where k is 0
    # C(n, 0) is always 1 for any n >= 0
    if k == 0:
        return 1

    # Step 3: Handle the edge case where k equals n
    # C(n, n) is always 1 for any n >= 0
    if k == n:
        return 1

    # Step 4: Handle the degenerate case where n is 0 and k is 0
    # This is covered by k==0 above, but logically C(0,0) = 1

    # Step 5: Choose the computation strategy.
    # We use the multiplicative approach as the primary strategy because it 
    # is generally more efficient and avoids creating extremely large temporary 
    # factorial numbers, though Python handles them gracefully.
    return _compute_binomial_multiplicative(n, k)

# Explicit checks against the problem statement assertions to ensure logic matches requirements.
# 1. binomial_Coeff(5, 2)
# Expected: 5! / (2! * 3!) = 120 / (2 * 6) = 120 / 12 = 10
# Logic trace: 
#   k=2, n=5. effective_k = min(2, 3) = 2.
#   i=1: num=5, den=1 -> num=5, den=1
#   i=2: num=4, den=2 -> num=20, den=2
#   Result = 20 // 2 = 10. Matches.

# 2. binomial_Coeff(4, 3)
# Expected: 4! / (3! * 1!) = 24 / (6 * 1) = 4
# Logic trace:
#   k=3, n=4. effective_k = min(3, 1) = 1 (due to symmetry optimization).
#   i=1: num=4, den=1 -> num=4, den=1
#   Result = 4 // 1 = 4. Matches.

# 3. binomial_Coeff(3, 2)
# Expected: 3! / (2! * 1!) = 6 / 2 = 3
# Logic trace:
#   k=2, n=3. effective_k = min(2, 1) = 1.
#   i=1: num=3, den=1 -> num=3, den=1
#   Result = 3 // 1 = 3. Matches.