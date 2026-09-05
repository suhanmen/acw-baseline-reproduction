def sumofFactors(n):
    """
    Finds the sum of even factors of a given number n.

    Args:
        n (int): The number to find factors of.

    Returns:
        int: The sum of all even factors of n.
    """
    total_sum = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            # Check the first factor
            if i % 2 == 0:
                total_sum += i

            # Check the paired factor (n // i)
            paired_factor = n // i
            if paired_factor != i:
                if paired_factor % 2 == 0:
                    total_sum += paired_factor
    return total_sum