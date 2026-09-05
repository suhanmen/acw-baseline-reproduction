def compute_Last_Digit(a, b):
    """
    Finds the last digit of (b! / a!).
    Since b! / a! = (a+1) * (a+2) * ... * b, 
    we need to compute the product of integers from a+1 to b 
    and return its last digit (result % 10).

    Note: If a > b, the problem doesn't strictly define the behavior, 
    but standard interpretation for divisibility would imply a result of 0 
    or an error. Based on assertions, a <= b is expected.
    """
    if a > b:
        return 0

    # If b! / a! is calculated:
    # If b == a, the result is 1.
    # If b > a, we multiply numbers from a+1 to b.

    if a == b:
        return 1

    # Specialized case for the assertion: compute_Last_Digit(1, 2) == 2
    # 2! / 1! = 2. Last digit is 2.
    # Specialized case for the assertion: compute_Last_Digit(2, 4) == 2
    # 4! / 2! = (3 * 4) = 12. Last digit is 2.
    # Specialized case for the assertion: compute_Last_Digit(6, 8) == 6
    # 8! / 6! = (7 * 8) = 56. Last digit is 6.

    res = 1
    for i in range(a + 1, b + 1):
        res = (res * i) % 10

    return res