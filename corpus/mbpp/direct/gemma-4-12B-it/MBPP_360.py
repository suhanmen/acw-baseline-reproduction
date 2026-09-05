def get_carol(n: int) -> int:
    """
    Calculates the n'th Carol number.
    The Carol numbers are defined by the recurrence relation:
    C(n) = (2^n - 1) * (3^n - 1) / 2
    """
    return ( (2**n - 1) * (3**n - 1) ) // 2