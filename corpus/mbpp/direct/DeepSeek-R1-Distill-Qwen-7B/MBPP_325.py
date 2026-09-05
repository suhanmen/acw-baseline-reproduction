def get_Min_Squares(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        if n == 2:
            return 2
        # Check for form 4^k*(8m+7)
        while n % 4 == 0:
            n = n // 4
        if n % 8 == 7:
            return 4
        else:
            return 3 if n % 2 == 0 else 2
    # If n is odd
    if n % 8 == 7:
        return 4
    return 3

# Test cases
assert get_Min_Squares(6) == 3, "Test case 6 failed"
assert get_Min_Squares(2) == 2, "Test case 2 failed"
assert get_Min_Squares(4) == 1, "Test case 4 failed"