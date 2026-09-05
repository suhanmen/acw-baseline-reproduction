def is_Diff(n: int) -> bool:
    """Return True if the difference between sum of even and odd digits is non-zero, else False."""
    if n < 0:
        n = -n  # Treat negative numbers as positive for digit analysis
    sum_even = 0
    sum_odd = 0
    for digit in str(n):
        d = int(digit)
        if d % 2 == 0:
            sum_even += d
        else:
            sum_odd += d
    return sum_even != sum_odd