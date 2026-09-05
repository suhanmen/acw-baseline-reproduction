from math import factorial

def validate_inputs(n, k):
    """
    Validates the inputs for the permutation coefficient calculation.

    Args:
        n (int): The total number of items.
        k (int): The number of items to choose and arrange.

    Returns:
        None

    Raises:
        TypeError: If either n or k is not an integer.
        ValueError: If n or k is negative.
        ValueError: If k is greater than n.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"n must be an integer, got {type(n).__name__}")
    if not isinstance(k, int) or isinstance(k, bool):
        raise TypeError(f"k must be an integer, got {type(k).__name__}")

    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    if k < 0:
        raise ValueError(f"k must be non-negative, got {k}")

    if k > n:
        raise ValueError(f"k cannot be greater than n. Got k={k} and n={n}")

def compute_permutation_coefficient(n, k):
    """
    Calculates the permutation coefficient P(n, k).

    The permutation coefficient P(n, k) represents the number of distinct 
    arrangements of k items chosen from a set of n items where order matters.

    Formula: P(n, k) = n! / (n - k)!

    Args:
        n (int): The total number of items (must be non-negative).
        k (int): The number of items to arrange (must be non-negative and <= n).

    Returns:
        int: The calculated permutation coefficient.

    Note:
        This function does not perform internal input validation to ensure
        the calling function handles exceptions appropriately. The caller
        should validate inputs before invoking this helper or rely on the
        wrapper function that performs validation.
    """
    if n < 0 or k < 0 or k > n:
        raise ValueError("Invalid values for n or k. Ensure 0 <= k <= n.")

    # Base case: P(n, 0) is 1 (there is one way to arrange zero items)
    if k == 0:
        return 1

    # Base case: P(n, 1) is n
    if k == 1:
        return n

    # General case: P(n, k) = n * (n-1) * ... * (n-k+1)
    # This is equivalent to n! / (n-k)!

    numerator_factorial = factorial(n)
    denominator_factorial = factorial(n - k)

    result = numerator_factorial // denominator_factorial

    return result

def permutation_coefficient(n, k):
    """
    Main function to calculate the permutation coefficient of given p(n, k).

    This function serves as the entry point, handling input validation and
    delegating the calculation to a helper function.

    Args:
        n (int): The total number of items.
        k (int): The number of items to choose and arrange.

    Returns:
        int: The permutation coefficient P(n, k).

    Raises:
        TypeError: If n or k are not integers.
        ValueError: If n or k are negative or if k > n.
    """
    # Perform explicit validation of inputs
    validate_inputs(n, k)

    # Compute and return the result
    return compute_permutation_coefficient(n, k)