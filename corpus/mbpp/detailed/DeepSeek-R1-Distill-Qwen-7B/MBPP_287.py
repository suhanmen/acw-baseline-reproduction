def square_Sum(n):
    # Input validation
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")

    total = 0
    for i in range(1, n + 1):
        even_number = 2 * i
        total += even_number ** 2

    return total

# Test cases
assert square_Sum(2) == 20, "Test case 1 failed"
assert square_Sum(3) == 56, "Test case 2 failed"
assert square_Sum(4) == 120, "Test case 3 failed"