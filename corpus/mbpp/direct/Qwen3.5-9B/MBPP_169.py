def get_pell(n: int) -> int:
    """
    Calculate the nth Pell number.
    Pell sequence: P(0)=0, P(1)=1, P(n) = 2*P(n-1) + P(n-2)
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, 2 * curr + prev

    return curr