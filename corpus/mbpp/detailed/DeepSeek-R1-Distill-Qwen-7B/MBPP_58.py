def opposite_Signs(a, b):
    # Check if either a or b is zero
    if a == 0 or b == 0:
        return False
    # Determine the sign of each number
    sign_a = 1 if a > 0 else -1
    sign_b = 1 if b > 0 else -1
    # Check if signs are different
    return sign_a != sign_b