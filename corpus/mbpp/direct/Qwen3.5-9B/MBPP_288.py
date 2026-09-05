def modular_inverse(arr, e, p):
    """
    Count elements in arr whose modular inverse under prime p equals themselves.
    Condition: (a * a) % p == 1, with a % p != 0.
    """
    def mod_inverse(a, p):
        if p == 1:
            return 0
        a = a % p
        if a == 0:
            return 0
        # Fermat's little theorem: a^(p-2) ≡ a^(-1) (mod p)
        return pow(a, p - 2, p)

    count = 0
    for x in arr:
        reduced = x % p
        if reduced == 0:
            continue
        inv = mod_inverse(reduced, p)
        if inv == reduced:
            count += 1
    return count