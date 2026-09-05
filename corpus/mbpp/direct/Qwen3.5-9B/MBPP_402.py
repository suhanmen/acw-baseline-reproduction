def ncr_modp(n, r, p):
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1

    r = min(r, n - r)

    numerator = 1
    for i in range(r):
        numerator = (numerator * (n - i)) % p

    denominator = 1
    for i in range(1, r + 1):
        denominator = (denominator * i) % p

    # Compute modular inverse of denominator mod p using Fermat's little theorem
    # Since p is prime, a^(p-2) ≡ a^-1 (mod p)
    inv_denominator = pow(denominator, p - 2, p)

    return (numerator * inv_denominator) % p