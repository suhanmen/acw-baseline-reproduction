def median(l: list):
    """Return median of elements in the list l."""
    l_sorted = sorted(l)
    n = len(l_sorted)
    if n % 2 == 1:
        return l_sorted[n // 2]
    else:
        return (l_sorted[n // 2 - 1] + l_sorted[n // 2]) / 2