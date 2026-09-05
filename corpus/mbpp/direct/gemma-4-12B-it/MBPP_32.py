def max_Prime_Factors(n):
    """
    Finds the largest prime factor of a given integer n.
    """
    if n <= 1:
        return None

    d = 2
    temp = n
    max_factor = 1

    while d * d <= temp:
        while temp % d == 0:
            max_factor = d
            temp //= d
        d += 1

    if temp > 1:
        max_factor = temp

    return max_factor

if __name__ == "__main__":
    assert max_Prime_Factors(15) == 5
    assert max_Prime_Factors(6) == 3
    assert max_Prime_Factors(2) == 2