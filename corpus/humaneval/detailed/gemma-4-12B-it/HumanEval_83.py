import math

def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.

    Logic:
    - A number has n digits.
    - The first digit cannot be 0.
    - We want to count numbers that:
        A) Start with 1.
        B) End with 1.
    - By the Principle of Inclusion-Exclusion: 
        Total = Count(Starts with 1) + Count(Ends with 1) - Count(Starts AND Ends with 1).
    """

    # Input Validation
    if not isinstance(n, int):
        raise TypeError("Input n must be an integer.")

    if n <= 0:
        # The problem specifies n is a positive integer.
        # If n is not positive, the count of n-digit numbers is 0.
        return 0

    # Edge Case: n = 1
    # The only 1-digit number starting or ending with 1 is '1'.
    if n == 1:
        return 1

    # Calculation for n > 1:

    # 1. Count numbers that start with 1.
    # The first digit is fixed as '1'.
    # The remaining (n-1) digits can be any digit from 0-9.
    # Count = 1 * 10^(n-1)
    count_starts_with_one = 10 ** (n - 1)

    # 2. Count numbers that end with 1.
    # The first digit can be any digit from 1-9 (9 choices).
    # The middle (n-2) digits can be any digit from 0-9 (10 choices each).
    # The last digit is fixed as '1'.
    # Count = 9 * 10^(n-2) * 1
    count_ends_with_one = 9 * (10 ** (n - 2))

    # 3. Count numbers that start with 1 AND end with 1.
    # The first digit is fixed as '1'.
    # The last digit is fixed as '1'.
    # The remaining (n-2) digits can be any digit from 0-9.
    # Count = 1 * 10^(n-2) * 1
    # Note: For n=2, this is 1 * 10^0 * 1 = 1 (The number "11").
    count_starts_and_ends_with_one = 10 ** (n - 2)

    # Apply Principle of Inclusion-Exclusion
    # Total = A + B - (A ∩ B)
    total_count = count_starts_with_one + count_ends_with_one - count_starts_and_ends_with_one

    return int(total_count)