def tn_gp(a, r, n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n < 1:
        return None
    # Check if a and r are numbers
    if not (isinstance(a, (int, float)) and isinstance(r, (int, float))):
        return None

    # Handle the special case where r is 0
    if r == 0:
        return 0 if n == 1 else None

    # Compute the nth term using the formula
    term = a * (r ** (n - 1))

    # Return the result
    return term

# Test cases
assert tn_gp(1, 5, 2) == 16
assert tn_gp(1, 5, 4) == 256
assert tn_gp(2, 6, 3) == 486

# Edge cases
assert tn_gp(3, 4, 1) == 3
assert tn_gp(0, 5, 3) == 0
assert tn_gp(5, 0, 1) == 5
assert tn_gp(5, 0, 2) == 0
assert tn_gp(2, 0, 0) is None
assert tn_gp("a", 5, 3) is None