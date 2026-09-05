from collections import defaultdict
from typing import List

def find_Divisor(start: int, end: int) -> int:
    """
    Finds the maximum occurring divisor within a given closed interval [start, end].

    A divisor of a number x is any integer d such that x % d == 0.
    The function identifies which divisor d (where d > 1) appears as a 
    divisor for the highest number of integers in the range [start, end].
    If there is a tie, the smallest such divisor is returned (standard 
    convention for such problems), though the problem asks for the maximum 
    occurring count's divisor.

    Args:
        start (int): The beginning of the range (inclusive).
        end (int): The end of the range (inclusive).

    Returns:
        int: The divisor that occurs most frequently.

    Raises:
        ValueError: If start is greater than end, or if inputs are not integers.
    """
    # --- Input Validation ---
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Both start and end must be integers.")

    if start > end:
        raise ValueError("The start of the interval must be less than or equal to the end.")

    # Handle cases where the range might contain non-positive numbers 
    # or where the range is effectively empty or single-point.
    # Divisors are typically defined for positive integers > 1 in this context.
    # We adjust the range to consider positive integers.
    effective_start = max(1, start)
    effective_end = max(1, end)

    if effective_start > effective_end:
        # If the range was, for example, (-5, 0), we return 0 or a sentinel.
        # Based on the assertions, we assume positive integers.
        return 0

    # --- Data Collection ---
    # divisor_counts maps a divisor 'd' to the number of times it divides 
    # any integer in the range [effective_start, effective_end].
    divisor_counts = defaultdict(int)

    # We iterate through every number in the range.
    # For each number, we find all its divisors.
    for current_num in range(effective_start, effective_end + 1):
        if current_num == 0:
            continue

        # Find all divisors of current_num
        # A divisor d must be in the range [1, current_num]
        # To be efficient, we only go up to sqrt(current_num)
        divisors = get_all_divisors(current_num)

        for d in divisors:
            # We ignore 1 as a divisor because every number is divisible by 1,
            # making it a trivial case. Usually, "divisor" in these puzzles
            # refers to d > 1. If d=1 is required, the logic holds.
            if d > 1:
                divisor_counts[d] += 1

    # --- Result Selection ---
    if not divisor_counts:
        # This happens if the range is [1, 1] or only contains 1s.
        # If the input was (1, 1), the only divisor is 1.
        # Based on assertions (2,2)->2, if the only number is 2, its divisor is 2.
        # If the only number is 1, and we exclude 1, we need a fallback.
        # However, for (2,2), divisor 2 occurs once.
        if effective_start <= 1 <= effective_end:
            return 1
        return 0

    max_occurrence = -1
    best_divisor = -1

    # Iterate through the dictionary to find the max count.
    # We sort keys to ensure deterministic behavior if counts are equal.
    sorted_divisors = sorted(divisor_counts.keys())

    for d in sorted_divisors:
        count = divisor_counts[d]
        if count > max_occurrence:
            max_occurrence = count
            best_divisor = d

    return best_divisor

def get_all_divisors(n: int) -> List[int]:
    """
    Helper function to find all divisors of a positive integer n.
    """
    divs = []
    if n <= 0:
        return divs

    # Optimization: Only iterate up to the square root of n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i*i != n:
                divs.append(n // i)
    return divs