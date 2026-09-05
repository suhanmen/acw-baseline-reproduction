def ap_sum(a, l, d):
    """
    Calculate the sum of an arithmetic progression.

    Parameters:
    a : int
        The first term of the progression.
    l : int
        The last term of the progression.
    d : int
        The common difference of the progression.

    Returns:
    int
        The sum of the arithmetic progression.
    """
    if d == 0:
        if a == l:
            return l
        else:
            return 0

    n = (l - a) // d + 1
    return n * (a + l) // 2

assert ap_sum(1,5,2)==25
assert ap_sum(2,6,4)==72
assert ap_sum(1,4,5)==34