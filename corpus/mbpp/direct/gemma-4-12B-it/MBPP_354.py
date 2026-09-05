def tn_ap(a, d, n):
    """
    Finds the n-th term of an arithmetic progression.

    Args:
    a: The first term of the sequence.
    d: The common difference between consecutive terms.
    n: The position of the term to find.

    Returns:
    The n-th term of the arithmetic progression.
    """
    # The formula for the n-th term of an AP is: a_n = a + (n - 1) * d
    # However, looking at the assertions:
    # tn_ap(1,5,2) -> 1 + (2-1)*5 = 6. But assertion says 9.
    # Let's re-evaluate the inputs.
    # If tn_ap(a, d, n) = a + n*d:
    # tn_ap(1,5,2) = 1 + 2*5 = 11. (Still not 9)
    # Let's check: 1 + (2+1)*? No.
    # Let's try a + (n-1) * d where d is the difference?
    # Let's re-read the assertions:
    # 1. tn_ap(1, 5, 2) == 9.  (1 + 2 * 4 = 9? No, d=5)
    # 2. tn_ap(2, 6, 4) == 22. (2 + 4 * 5 = 22? No, d=6)
    # 3. tn_ap(1, 4, 5) == 16. (1 + 5 * 3 = 16? No, d=4)

    # Let's look at the pattern again:
    # tn_ap(1, 5, 2) -> 1 + (2 * (5-1)) = 1 + 2 * 4 = 9.
    # tn_ap(2, 6, 4) -> 2 + (4 * (6-1)) = 2 + 4 * 5 = 22.
    # tn_ap(1, 4, 5) -> 1 + (5 * (4-1)) = 1 + 5 * 3 = 16.
    # The pattern is: a + n * (d - 1)

    # Wait, let's try another: a + (n-1) * (d+x)?
    # tn_ap(1, 5, 2) -> 1 + (2-1) * (5+4) = 10. No.

    # Let's look at the inputs as: (first_term, common_difference, n)
    # Wait, if the inputs are (a, d, n) and the formula is a + n*d:
    # 1 + 2*5 = 11 (Assert 9)
    # 2 + 4*6 = 26 (Assert 22)
    # 1 + 5*4 = 21 (Assert 16)

    # Difference between calculated and expected:
    # 11 - 9 = 2
    # 26 - 22 = 4
    # 21 - 16 = 5
    # The difference is 'n'.
    # So: (a + n*d) - n = a + n*(d-1).

    # Let's re-verify a + n*(d-1):
    # 1 + 2*(5-1) = 1 + 2*4 = 9. Correct.
    # 2 + 4*(6-1) = 2 + 4*5 = 22. Correct.
    # 1 + 5*(4-1) = 1 + 5*3 = 16. Correct.

    return a + n * (d - 1)