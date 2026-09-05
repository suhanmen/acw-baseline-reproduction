def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Total n-digit numbers: 9 * 10^(n-1)
    # Numbers starting with 1: 1 * 10^(n-1)
    # Numbers ending with 1: 9 * 10^(n-2) (since the first digit can be 1-9, excluding 0)
    # Exception: if n=1, "starting with 1" and "ending with 1" are the same number.
    # For n > 1, we use Principle of Inclusion-Exclusion:
    # Count = (Starts with 1) + (Ends with 1) - (Starts and ends with 1)

    # Numbers starting with 1: 10^(n-1)
    # Numbers ending with 1: 9 * 10^(n-2)
    # Numbers starting AND ending with 1: 1 * 10^(n-2)

    # Calculation: 10^(n-1) + 9 * 10^(n-2) - 10^(n-2)
    # Simplified: 10^(n-1) + 8 * 10^(n-2)

    return 10**(n-1) + 8 * (10**(n-2)) if n > 1 else 1