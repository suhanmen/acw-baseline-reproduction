def average_Odd(n):
    """
    Calculate the average of all odd numbers from 1 up to and including n.
    n must be a positive odd integer.
    """
    count = (n + 1) // 2
    sum_odds = count * count
    return sum_odds // count