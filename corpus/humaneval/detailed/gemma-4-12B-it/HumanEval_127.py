import math

def is_prime(n: int) -> bool:
    """
    Helper function to determine if a given integer is a prime number.
    A prime number is a natural number greater than 1 that has no 
    positive divisors other than 1 and itself.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to the square root of n
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
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
    # --- Input Validation ---
    # Check if inputs are tuples/lists of length 2
    if not (isinstance(interval1, (tuple, list)) and len(interval1) == 2):
        raise ValueError("interval1 must be a pair of integers.")
    if not (isinstance(interval2, (tuple, list)) and len(interval2) == 2):
        raise ValueError("interval2 must be a pair of integers.")

    # Check if elements are integers
    if not all(isinstance(x, int) for x in interval1 + interval2):
        raise ValueError("Interval elements must be integers.")

    # Extract values for clarity
    start1, end1 = interval1
    start2, end2 = interval2

    # Ensure the integrity of the input (start <= end as per problem description)
    if start1 > end1:
        raise ValueError("For interval1, start must be less than or equal to end.")
    if start2 > end2:
        raise ValueError("For interval2, start must be less than or equal to end.")

    # --- Calculate Intersection ---
    # The intersection of [s1, e1] and [s2, e2] is [max(s1, s2), min(e1, e2)]
    intersect_start = max(start1, start2)
    intersect_end = min(end1, end2)

    # Check if an intersection exists
    # If start is greater than end, the intersection is empty
    if intersect_start > intersect_end:
        # No intersection exists
        return "NO"

    # Calculate the length of the intersection
    # For closed intervals [a, b], the length is defined as (b - a)
    # Note: Example (1, 3) and (2, 4) intersection is (2, 3), length = 3 - 2 = 1.
    intersection_length = intersect_end - intersect_start

    # --- Prime Check ---
    # A prime number must be a positive integer.
    # We check if the calculated length is prime.
    result_is_prime = is_prime(intersection_length)

    if result_is_prime:
        return "YES"
    else:
        return "NO"