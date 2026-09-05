def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""

    # Handle the case where b is empty
    if not b:
        return True if a else False

    # Handle cases where a is shorter than b or b has only one character
    if len(b) == 1:
        return True if len(a) >= 1 else False
    if len(a) < len(b):
        return False

    # Generate all possible rotations of b
    rotations = set()
    for i in range(len(b)):
        rotation = b[i:] + b[:i]
        rotations.add(rotation)

    # Check if any rotation is a substring of a
    for rot in rotations:
        if rot in a:
            return True

    return False