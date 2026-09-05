def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: The result of 2^n % p.
    """
    result = 1
    base = 2 % p
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        n = n // 2
    return result