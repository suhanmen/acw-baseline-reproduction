import math

def is_coprime(a: int, b: int) -> bool:
    """
    Check whether the given number is co-prime or not.
    Two numbers are co-prime if their greatest common divisor (GCD) is 1.
    """
    return math.gcd(a, b) == 1