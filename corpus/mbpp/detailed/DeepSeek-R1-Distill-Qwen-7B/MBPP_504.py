def sum_of_series(n):
    """
    Calculate the cube sum of the first n natural numbers.

    Args:
        n (int): The number of natural numbers to consider.

    Returns:
        int: The sum of cubes of the first n natural numbers.

    Raises:
        ValueError: If n is not a positive integer.
    """
    # Input validation
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")

    # Calculate cube sum
    cube_sum = 0
    for i in range(1, n + 1):
        cube_sum += i ** 3

    return cube_sum

# Test cases
assert sum_of_series(5) == 225, "Test case 1 failed"
assert sum_of_series(2) == 9, "Test case 2 failed"
assert sum_of_series(3) == 36, "Test case 3 failed"

print("All test cases passed")