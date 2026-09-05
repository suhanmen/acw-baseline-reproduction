def odd_Equivalent(binary_string: str, n: int) -> int:
    """
    Counts the number of rotations of a binary string that have an odd integer value.

    Args:
        binary_string: A string consisting of '0' and '1'.
        n: The number of rotations to consider (from 0 to n-1).

    Returns:
        The count of rotations that represent an odd number.
    """
    s = binary_string
    length = len(s)
    if n > length:
        n = length % length if length > 0 else 0

    count = 0
    for i in range(n):
        rotated = s[i:] + s[:i]
        # Convert binary string to integer
        value = int(rotated, 2)
        if value % 2 == 1:
            count += 1
    return count