def even_Power_Sum(n):
    """
    Calculate the sum of the fifth powers of the first n even natural numbers.

    Args:
        n (int): The number of even natural numbers to consider.

    Returns:
        int: The sum of the fifth powers of the first n even natural numbers.

    Raises:
        ValueError: If n is not a non-negative integer.
    """
    # Validate input
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    # Generate the first n even natural numbers
    even_numbers = [2 * i for i in range(1, n + 1)]

    # Calculate the fifth power of each and sum them
    total_sum = 0
    for number in even_numbers:
        total_sum += number ** 5

    return total_sum

# Example test cases
assert even_Power_Sum(2) == 1056, "Test case 2 failed"
assert even_Power_Sum(3) == 8832, "Test case 3 failed"
assert even_Power_Sum(1) == 32, "Test case 1 failed"