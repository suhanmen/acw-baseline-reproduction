def modular_inverse(arr, n, p):
    """
    Counts array elements where the modular inverse of the element
    under a given prime p is equal to itself.

    Note: The problem constraints/examples suggest:
    - The modular inverse 'x' of 'a' satisfies (a * x) % p == 1.
    - We check if (a * a) % p == 1.
    - The parameter 'n' is present in the signature but not 
      explicitly used in the logic of the specific assertions provided.
    """
    count = 0
    for x in arr:
        # An element has a modular inverse equal to itself if
        # (x * x) % p == 1
        if (x * x) % p == 1:
            count += 1
    return count