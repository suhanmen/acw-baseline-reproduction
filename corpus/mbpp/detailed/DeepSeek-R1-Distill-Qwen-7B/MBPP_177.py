def answer(a, b):
    """
    Find two distinct numbers such that their LCM lies within the given range [a, b].
    Returns None if no such pair exists.
    """
    # Handle edge cases
    if a < 1:
        return None
    if a > b:
        return None

    # Helper function to compute GCD using Euclidean algorithm
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    # Helper function to compute LCM using the formula (x * y) // gcd(x, y)
    def lcm(x, y):
        return (x * y) // gcd(x, y)

    # Iterate through all possible pairs (i, j) where i < j
    for i in range(a, b):
        for j in range(i + 1, b + 1):
            current_lcm = lcm(i, j)
            # Check if the LCM is within the desired range
            if current_lcm >= a and current_lcm <= b:
                return (i, j)

    # If no pair found
    return None

# Test cases
assert answer(3, 8) == (3, 6)
assert answer(2, 6) == (2, 4)
assert answer(1, 3) == (1, 2)