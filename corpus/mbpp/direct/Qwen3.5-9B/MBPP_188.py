def prod_Square(n: int) -> bool:
    if n < 1:
        return False

    # A number is a product of two squares if and only if
    # in its prime factorization, every prime has an even exponent.
    # This is equivalent to checking if the square-free part of n is 1.

    import math

    d = n
    f = 2
    while f * f <= d:
        if d % f == 0:
            count = 0
            while d % f == 0:
                count += 1
                d //= f
            if count % 2 == 1:
                return False
        f += 1
    if d > 1:
        # Remaining d is a prime with exponent 1 (odd)
        return False

    return True