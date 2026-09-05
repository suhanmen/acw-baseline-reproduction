import math

def even_Power_Sum(n: int) -> int:
    """
    Calculates the sum of the fifth powers of the first n even natural numbers.

    The first n even natural numbers are: 2, 4, 6, ..., 2n.
    The formula for the sum is: sum_{i=1}^{n} (2i)^5.

    Args:
        n (int): The number of even natural numbers to sum.

    Returns:
        int: The sum of the fifth powers of the first n even natural numbers.

    Raises:
        ValueError: If n is not a non-negative integer.
        TypeError: If n is not an integer.
    """
    # Input Validation: Check if input is an integer type
    if not isinstance(n, int):
        raise TypeError(f"Input 'n' must be an integer, received {type(n).__name__}.")

    # Input Validation: Check if n is non-negative
    # A count of "first n numbers" implies n >= 0.
    if n < 0:
        raise ValueError(f"Input 'n' must be a non-negative integer, received {n}.")

    # Handle the degenerate case of zero elements
    if n == 0:
        return 0

    total_sum = 0

    # Iterate through the range of numbers to identify the first n even natural numbers.
    # The i-th even natural number is defined by 2 * i.
    # We range from 1 up to n (inclusive).
    for i in range(1, n + 1):
        # Calculate the i-th even natural number
        even_number = 2 * i

        # Calculate the fifth power of that even number
        # Using power operator ** 5 for clarity.
        fifth_power = even_number ** 5

        # Accumulate the result
        total_sum += fifth_power

    return total_sum

# The following assertions are used to verify the correctness of the implementation.
if __name__ == "__main__":
    # Test Case 1: n = 1 (2^5 = 32)
    # Assertion: even_Power_Sum(1) == 32
    assert even_Power_Sum(1) == 32

    # Test Case 2: n = 2 (2^5 + 4^5 = 32 + 1024 = 1056)
    # Assertion: even_Power_Sum(2) == 1056
    assert even_Power_Sum(2) == 1056

    # Test Case 3: n = 3 (2^5 + 4^5 + 6^5 = 32 + 1024 + 7776 = 8832)
    # Assertion: even_Power_Sum(3) == 8832
    assert even_Power_Sum(3) == 8832

    # Edge Case: n = 0 (Sum should be 0)
    assert even_Power_Sum(0) == 0