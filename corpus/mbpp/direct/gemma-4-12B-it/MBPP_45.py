import math
from functools import reduce

def get_gcd(arr):
    """
    Finds the greatest common divisor (GCD) of a list of integers.
    """
    if not arr:
        return 0
    return reduce(math.gcd, arr)

if __name__ == "__main__":
    assert get_gcd([2, 4, 6, 8, 16]) == 2
    assert get_gcd([1, 2, 3]) == 1
    assert get_gcd([2, 4, 6, 8]) == 2