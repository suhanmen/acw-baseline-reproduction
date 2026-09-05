def average_Odd(n):
    """
    Finds the average of odd numbers from 1 up to and including the given odd number n.

    Args:
        n (int): An odd number.

    Returns:
        float/int: The average of all odd numbers from 1 to n.
    """
    odd_numbers = [i for i in range(1, n + 1) if i % 2 != 0]
    return sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0