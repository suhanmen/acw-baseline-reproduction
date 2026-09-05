def sum_difference(n):
    # Ensure that n is a non-negative integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    # Calculate the sum of the first n natural numbers
    sum_n = n * (n + 1) // 2

    # Calculate the squared sum
    squared_sum = sum_n ** 2

    # Calculate the sum of squares of the first n natural numbers
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6

    # Calculate and return the difference
    return squared_sum - sum_of_squares

# Test cases
assert sum_difference(12) == 5434
assert sum_difference(20) == 41230
assert sum_difference(54) == 2151270