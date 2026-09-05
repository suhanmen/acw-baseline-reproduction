def get_carol(n: int) -> int:
    """
    Returns the n'th Carol number.
    Carol numbers are defined as C_n = A(n)^2 - 2, where A(n) is the n-th Pell number.
    Pell numbers: P_0 = 0, P_1 = 1, P_n = 2*P_{n-1} + P_{n-2} for n >= 2.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    # Compute n-th Pell number
    if n == 1:
        p = 1
    elif n == 2:
        p = 2
    else:
        p0, p1 = 0, 1
        for _ in range(2, n + 1):
            p0, p1 = p1, 2 * p1 + p0
        p = p1

    # Carol number = Pell(n)^2 - 2
    return p * p - 2