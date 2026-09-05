def find_Divisor(a, b):
    """
    Finds the maximum occurring divisor in the interval [a, b].

    Args:
        a (int): The lower bound of the interval.
        b (int): The upper bound of the interval.

    Returns:
        int: The maximum divisor that occurs the most times.

    Raises:
        ValueError: If the input interval is invalid (a > b).
    """
    if a > b:
        raise ValueError("Invalid interval: a must be less than or equal to b.")

    if a == 0:
        raise ValueError("Divisor 0 is not allowed.")

    if a == b:
        return a

    # Generate all possible divisors in the interval [a, b]
    divisors = set()
    for num in range(a, b + 1):
        for divisor in range(1, int(num**0.5) + 1):
            if num % divisor == 0:
                divisors.add(divisor)
                divisors.add(num // divisor)

    # Count the frequency of each divisor
    from collections import defaultdict
    divisor_counts = defaultdict(int)
    for d in divisors:
        divisor_counts[d] += 1

    # Find the divisor with the maximum count
    max_count = -1
    max_divisor = -1
    for divisor, count in divisor_counts.items():
        if count > max_count or (count == max_count and divisor > max_divisor):
            max_count = count
            max_divisor = divisor

    return max_divisor