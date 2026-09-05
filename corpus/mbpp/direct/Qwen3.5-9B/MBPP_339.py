def find_Divisor(start, end):
    """
    Find the maximum occurring divisor in the interval [start, end].
    The function returns the divisor that appears most frequently among all numbers in the interval.
    If there's a tie, return the largest divisor among the most frequent ones.
    """
    if start > end:
        return -1

    divisor_counts = {}

    for num in range(start, end + 1):
        for d in range(1, num + 1):
            if num % d == 0:
                divisor_counts[d] = divisor_counts.get(d, 0) + 1

    if not divisor_counts:
        return -1

    max_occurrence = max(divisor_counts.values())
    candidates = [d for d, count in divisor_counts.items() if count == max_occurrence]

    return max(candidates)