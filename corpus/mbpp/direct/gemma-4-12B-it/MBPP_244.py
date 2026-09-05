import math

def next_Perfect_Square(n):
    """
    Finds the next perfect square greater than a given number n.
    """
    # If n is negative, the next perfect square is 0 (0^2)
    if n < 0:
        return 0

    # Find the integer square root of n
    root = int(math.isqrt(n))

    # The next perfect square is the square of the next integer
    # However, if n itself is a perfect square, we need the square of root + 1
    # if n is not a perfect square, the square of root + 1 is also the next perfect square.
    # The smallest integer x such that x^2 > n is floor(sqrt(n)) + 1.

    next_root = root + 1
    return next_root * next_root

if __name__ == "__main__":
    assert next_Perfect_Square(35) == 36
    assert next_Perfect_Square(6) == 9
    assert next_Perfect_Square(9) == 16