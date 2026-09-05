def dif_Square(n):
    """
    Checks whether the given number n can be represented as a difference of two squares.
    A number n can be represented as x^2 - y^2 if and only if:
    n is NOT of the form 4k + 2 (i.e., n is not 2, 6, 10, 14, ...).
    This means n must be odd OR n must be a multiple of 4.
    """
    # A number n can be expressed as x^2 - y^2 if:
    # n = (x - y)(x + y)
    # Let a = x - y and b = x + y.
    # Then x = (a + b) / 2 and y = (b - a) / 2.
    # For x and y to be integers, (a + b) and (b - a) must be even.
    # This happens if a and b are both even or both odd.
    # Since a * b = n, if n is odd, we can always find two odd factors (e.g., 1 and n).
    # If n is even, n must be a multiple of 4 so that we can find two even factors (e.g., 2 and n/2).

    if n < 0:
        # While the problem implies non-negative, mathematically,
        # negative numbers can be represented (e.g., -3 = 1^2 - 2^2).
        # However, standard interpretation for these problems usually assumes n >= 0.
        # We apply the same logic: n must not be 2 mod 4.
        n = abs(n)

    return (n % 4 == 1) or (n % 4 == 3) or (n % 4 == 0)

if __name__ == "__main__":
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True