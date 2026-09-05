def odd_Equivalent(s, n):
    """
    Counts the number of rotations of a binary string that result in an odd number.

    Args:
        s (str): The binary string.
        n (int): The number of rotations to perform.

    Returns:
        int: The count of rotations resulting in an odd number.
    """
    count = 0
    length = len(s)

    # Handle edge case where n is larger than the string length
    if n >= length:
        n = n % length

    # Generate all rotations
    for i in range(n):
        rotated = s[i:] + s[:i]
        if rotated[-1] == '1':
            count += 1

    return count