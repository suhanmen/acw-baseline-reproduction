def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word."""
    len_a, len_b = len(a), len(b)
    if len_b == 0 or len_b > len_a:
        return False
    # Concatenate b with itself to capture all possible rotations
    bb = b + b
    # Check each rotation of length len_b to see if it's a substring of a
    for i in range(len_b):
        current_rotation = bb[i:i+len_b]
        if current_rotation in a:
            return True
    return False