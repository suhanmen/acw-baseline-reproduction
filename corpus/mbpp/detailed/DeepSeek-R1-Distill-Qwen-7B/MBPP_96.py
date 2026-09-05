def divisor(n):
    """
    Find the number of divisors of a given integer.
    """
    # Handle empty input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")

    # Handle non-integer inputs
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")

    if n == 0:
        raise ValueError("Input cannot be zero, as zero has infinitely many divisors.")

    # Ensure n is positive for divisor calculation
    n = abs(n)

    # Initialize the divisor count
    divisor_count = 0

    # Iterate through possible divisors up to sqrt(n)
    sqrt_n = int(n ** 0.5)

    # Loop through all possible divisors
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            # Check if i is a perfect square
            if i * i == n:
                divisor_count += 1
            else:
                divisor_count += 2

    return divisor_count

def count_perfect_squares(count, count2):
    """
    Count the number of perfect squares in a given range.
    """
    return count - count2

def find_divisors(n):
    """
    Find the number of divisors of a given integer.
    """
    divisor_count = 0
    sqrt_n = int(n ** 0.5)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            if i * i == n:
                divisor_count += 1
            else:
                divisor_count += 2
    return divisor_count

def divisor(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n == 0:
        raise ValueError("Input cannot be zero, as zero has infinitely many divisors.")
    n = abs(n)
    divisor_count = 0
    sqrt_n = int(n ** 0.5)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            if i * i == n:
                divisor_count += 1
            else:
                divisor_count += 2
    return divisor_count

# Test the function
assert divisor(15) == 4
assert divisor(12) == 6
assert divisor(9) == 3