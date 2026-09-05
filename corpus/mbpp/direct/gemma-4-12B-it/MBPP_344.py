import math

def count_Odd_Squares(start, end):
    """
    Finds the number of elements in the range [start, end] that have 
    an odd number of factors.

    A mathematical property is that a positive integer has an odd number of 
    factors if and only if it is a perfect square.
    """
    count = 0
    # A number n has an odd number of factors if and only if it is a perfect square.
    # We need to count how many perfect squares are in the range [start, end].

    # Find the first integer whose square is >= start
    lower_root = math.ceil(math.sqrt(start))

    # Find the last integer whose square is <= end
    upper_root = math.floor(math.sqrt(end))

    # The number of perfect squares is the count of integers in [lower_root, upper_root]
    if lower_root > upper_root:
        return 0

    return upper_root - lower_root + 1