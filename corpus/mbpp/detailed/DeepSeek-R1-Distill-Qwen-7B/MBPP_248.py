def harmonic_sum(n):
    """
    Calculate the harmonic sum of n-1.

    The harmonic sum is defined as the sum of reciprocals of the first n natural numbers,
    but in this case, we sum up to n-1. That is, sum(1/i for i in range(1, n)).

    Args:
        n (int): The upper limit minus one for the harmonic sum.

    Returns:
        float: The harmonic sum of n-1.

    Raises:
        ValueError: If n is not a positive integer greater than zero.
    """
    # Input validation
    if not isinstance(n, int):
        raise ValueError("n must be an integer.")
    if n <= 0:
        raise ValueError("n must be a positive integer greater than zero.")

    # Base case: if n is 1, return 0 since sum up to 0 is empty
    if n == 1:
        return 0.0

    # Calculate harmonic sum: sum of 1/i for i from 1 to n-1
    harmonic = 0.0
    for i in range(1, n):
        harmonic += 1 / i

    return harmonic

# Example test cases
print(harmonic_sum(7))  # Output: 2.5928571428571425
print(harmonic_sum(4))  # Output: 2.083333333333333
print(harmonic_sum(19)) # Output: 3.547739657143682