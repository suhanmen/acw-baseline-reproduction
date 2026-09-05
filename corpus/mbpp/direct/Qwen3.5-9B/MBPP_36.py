def find_Nth_Digit(numerator, denominator, n):
    """
    Find the nth digit in the decimal expansion of the proper fraction numerator/denominator.
    The fraction is assumed to be proper (numerator < denominator).
    """
    if not (0 <= numerator < denominator):
        raise ValueError("numerator must be non-negative and less than denominator")
    if n < 1:
        raise ValueError("n must be a positive integer")

    remainder = numerator
    for _ in range(n):
        remainder *= 10
        digit = remainder // denominator
        remainder = remainder % denominator
        if digit != 0 or _ == n - 1:  # Always return the nth digit
            return digit
    return 0