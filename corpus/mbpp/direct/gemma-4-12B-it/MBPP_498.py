def gcd(a: int, b: int) -> int:
    """
    Find the greatest common divisor of two positive integers using 
    the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    assert gcd(12, 17) == 1
    assert gcd(4, 6) == 2
    assert gcd(2, 9) == 1