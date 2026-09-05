from typing import Tuple, Union

Number = Union[int, float]

def _validate_interval(interval: Tuple[Number, Number]) -> Tuple[bool, str]:
    """
    Validates that the input is a valid interval (tuple of two numbers).
    Returns (is_valid, error_message).
    """
    if not isinstance(interval, tuple) or len(interval) != 2:
        return False, "Interval must be a tuple of exactly two elements."

    start, end = interval

    if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
        return False, "Both elements of the interval must be numeric."

    if start > end:
        return False, "For each interval, start must be less than or equal to end."

    return True, ""

def _calculate_intersection_length(interval1: Tuple[Number, Number], interval2: Tuple[Number, Number]) -> Number:
    """
    Calculates the length of the intersection of two intervals.
    Assumes intervals are already validated.
    Returns the length of the intersection, or -1 if they do not intersect.
    """
    start1, end1 = interval1
    start2, end2 = interval2

    # The start of the intersection is the maximum of the starts
    intersection_start = max(start1, start2)

    # The end of the intersection is the minimum of the ends
    intersection_end = min(end1, end2)

    # If the start of the intersection is greater than the end, there is no intersection
    if intersection_start > intersection_end:
        return -1

    # Length calculation: (end - start + 1) for closed intervals
    # Example: (2, 3) has length 2 (points 2 and 3)
    # However, the problem example says (1, 3) intersect (2, 4) is (2, 3) with length 1.
    # Let's re-read carefully: "intersection ... is (2, 3) which its length is 1".
    # This implies length = end - start.
    # (3) - (2) = 1.
    # So the length is simply intersection_end - intersection_start.

    return intersection_end - intersection_start

def _is_prime(n: Number) -> bool:
    """
    Determines if a number is a prime number.
    Returns True if prime, False otherwise.
    Handles edge cases: n <= 1, n < 0, non-integers.
    """
    # Primes must be positive integers greater than 1
    if not isinstance(n, int):
        return False

    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    # Check odd divisors up to square root of n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True

def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """

    # Step 1: Validate inputs
    valid1, err1 = _validate_interval(interval1)
    if not valid1:
        return "NO"

    valid2, err2 = _validate_interval(interval2)
    if not valid2:
        return "NO"

    # Step 2: Calculate intersection length
    length = _calculate_intersection_length(interval1, interval2)

    # Step 3: Check if intersection exists
    if length < 0:
        return "NO"

    # Step 4: Check if length is a prime number
    # Note: Based on the problem description, length 1 is NOT prime.
    # Our _is_prime function correctly handles 1 (returns False).
    if _is_prime(length):
        return "YES"
    else:
        return "NO"