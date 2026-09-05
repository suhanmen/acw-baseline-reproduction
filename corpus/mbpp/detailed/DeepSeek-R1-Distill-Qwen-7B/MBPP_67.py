def bell_number(n):
    """
    Compute the nth Bell number using an iterative dynamic programming approach.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    # Create a 2D array to store Bell numbers where bell[i][j] = Bell number B(i)
    # Since we're computing B(n), we can optimize space by using a 1D array
    bell = [0] * (n + 1)
    bell[0] = 1  # Base case

    for i in range(1, n + 1):
        # The ith row (i starts from 1) will store Bell numbers B(0), B(1), ..., B(i)
        # For each j from 0 to i, compute bell[j] using the sum of binomial coefficients
        bell[j] = sum(bell[k] * binomial_coefficient(i-1, j-1) for k in range(j))

    return bell[n]

def binomial_coefficient(n, k):
    """
    Compute the binomial coefficient (n choose k).
    """
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    # To compute binomial coefficient efficiently, we'll use the multiplicative formula:
    # C(n, k) = n! / (k! * (n - k)!)
    # This can be optimized by computing it iteratively to avoid large intermediate factorials
    result = 1
    for i in range(1, k+1):
        result = result * (n - i + 1) // i
    return result

# Testing the function with the given examples
def test_bell_number():
    assert bell_number(2) == 2
    assert bell_number(10) == 115975
    assert bell_number(56) == 6775685320645824322581483068371419745979053216268760300
    print("All tests passed!")

test_bell_number()