def find_Divisor(a, b):
    """
    Find the maximum occurring divisor in the interval [a, b].
    """
    from collections import defaultdict

    divisors = defaultdict(int)
    for num in range(a, b + 1):
        for d in range(1, num + 1):
            if num % d == 0:
                divisors[d] += 1

    if not divisors:
        return None

    max_count = max(divisors.values())
    for d in sorted(divisors.keys(), reverse=True):
        if divisors[d] == max_count:
            return d

    return None