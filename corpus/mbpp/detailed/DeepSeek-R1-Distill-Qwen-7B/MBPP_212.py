def fourth_Power_Sum(n):
    # Input validation: check if n is a non-negative integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    # Calculate the sum of the fourth powers of the first n natural numbers
    total = 0
    for i in range(1, n + 1):
        total += i ** 4

    return total

# Test cases
assert fourth_Power_Sum(2) == 17, "Test case failed for n=2"
assert fourth_Power_Sum(4) == 354, "Test case failed for n=4"
assert fourth_Power_Sum(6) == 2275, "Test case failed for n=6"