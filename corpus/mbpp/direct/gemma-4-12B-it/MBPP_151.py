import math

def is_coprime(a: int, b: int) -> bool:
    """
    Checks whether two numbers are co-prime.
    Two numbers are co-prime if their greatest common divisor (GCD) is 1.
    """
    return math.gcd(a, b) == 1

if __name__ == "__main__":
    assert is_coprime(17, 13) == True
    assert is_coprime(15, 21) == False
    assert is_coprime(25, 45) == False