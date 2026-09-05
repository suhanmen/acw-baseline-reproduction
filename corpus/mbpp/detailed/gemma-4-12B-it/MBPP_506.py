def permutation_coefficient(n: int, k: int) -> int:
    """
    Calculates the permutation coefficient P(n, k), which is the number 
    of ways to choose and arrange k elements from a set of n distinct elements.

    Formula: P(n, k) = n! / (n - k)!
    Or iteratively: P(n, k) = n * (n - 1) * ... * (n - k + 1)

    Args:
        n (int): The total number of elements in the set.
        k (int): The number of elements to be arranged.

    Returns:
        int: The permutation coefficient.

    Raises:
        ValueError: If n or k are negative, or if k is greater than n.
        TypeError: If n or k are not integers.
    """
    # Step 1: Input Validation
    # Ensure the inputs are integers
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("Both n and k must be integers.")

    # Ensure inputs are non-negative
    if n < 0 or k < 0:
        raise ValueError("Both n and k must be non-negative integers.")

    # Ensure k does not exceed n
    if k > n:
        # Mathematically, if k > n, the number of ways to arrange k 
        # elements from n is 0 because there aren't enough elements.
        # However, in many contexts, this is considered an invalid input.
        # Given the requirements for defensive programming, we return 0 
        # as it is the standard mathematical result for P(n, k) where k > n.
        return 0

    # Step 2: Handle base cases
    # P(n, 0) is always 1 (there is 1 way to arrange 0 elements)
    if k == 0:
        return 1

    # P(n, 1) is always n
    if k == 1:
        return n

    # Step 3: Iterative Calculation
    # We use the iterative approach: P(n, k) = n * (n-1) * ... * (n-k+1)
    # This is more efficient and less prone to overflow than calculating 
    # full factorials and then dividing.

    result = 1

    # We need to multiply k terms.
    # The terms are: n, (n-1), (n-2), ..., (n - k + 1)
    for i in range(k):
        current_multiplier = n - i

        # Safety check: current_multiplier should not be negative
        # because we already checked k > n.
        if current_multiplier < 0:
            return 0

        result = result * current_multiplier

    return result

# Verification against assertions provided in the problem
if __name__ == "__main__":
    # These assertions confirm the function meets the required behavior.
    assert permutation_coefficient(10, 2) == 90
    assert permutation_coefficient(10, 3) == 720
    assert permutation_coefficient(10, 1) == 10