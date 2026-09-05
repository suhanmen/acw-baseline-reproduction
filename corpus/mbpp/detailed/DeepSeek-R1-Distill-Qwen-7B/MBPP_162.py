def sum_series(n):
    """
    Calculate the sum of the positive integers in the sequence n, n-2, n-4, ..., until the term is <= 0.

    Args:
        n (int): The starting integer.

    Returns:
        int: The sum of the positive integers in the sequence.

    Raises:
        ValueError: If n is not a positive integer.
    """
    # Input Validation
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 1:
        return 0  # Handles zero and negative cases

    # Base Case for n=1
    if n == 1:
        return 1

    # Generate the sequence and calculate the sum
    current = n
    sequence_sum = 0

    while current > 0:
        sequence_sum += current
        current -= 2

    return sequence_sum

# Example usage and assertions
if __name__ == "__main__":
    print(sum_series(6))    # Expected output: 12
    print(sum_series(10))   # Expected output: 30
    print(sum_series(9))    # Expected output: 25
    print(sum_series(1))    # Expected output: 1
    print(sum_series(0))    # Expected output: 0
    print(sum_series(-5))   # Expected output: 0
    # Example with non-integer input
    try:
        print(sum_series("6"))  # Should raise ValueError
    except ValueError as e:
        print(e)