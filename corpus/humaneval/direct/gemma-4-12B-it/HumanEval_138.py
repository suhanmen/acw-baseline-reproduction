def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # A positive even number is any number in the set {2, 4, 6, ...}.
    # The smallest positive even number is 2.
    # The sum of 4 smallest positive even numbers is 2 + 2 + 2 + 2 = 8.
    # Any sum of 4 positive even numbers will be:
    # n = 2a + 2b + 2c + 2d, where a, b, c, d are positive integers (>= 1).
    # This simplifies to n = 2(a + b + c + d).
    # Since the minimum value for (a + b + c + d) is 1 + 1 + 1 + 1 = 4,
    # the minimum value for n is 2 * 4 = 8.
    # Additionally, since n is the sum of 4 even numbers, n must be even.
    # Any even number n >= 8 can be represented as 2 + 2 + 2 + (n - 6).
    # Since n is even and >= 8, (n - 6) is an even number >= 2.
    # Therefore, n is representable if and only if n is even and n >= 8.

    return n >= 8 and n % 2 == 0