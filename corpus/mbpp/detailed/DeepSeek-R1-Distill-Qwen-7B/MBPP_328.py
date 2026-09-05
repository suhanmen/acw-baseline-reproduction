def rotate_left(lst, num, n):
    """
    Rotates a given list `lst` by `num` positions to the left, wrapping around the elements.

    Args:
        lst: The list to be rotated.
        num: The number of positions to rotate the list. If num is larger than the length of lst,
             the effective rotation is num modulo the length of lst.
        n: The number of elements in the list. If not provided, it will be calculated from the length of lst.

    Returns:
        A new list that is the result of rotating `lst` to the left by `num` positions.

    Raises:
        ValueError: If `lst` is empty, `num` is not an integer, or `n` is not an integer.
    """
    if not lst:
        raise ValueError("The list cannot be empty.")

    if not isinstance(num, int) or not isinstance(n, int):
        raise ValueError("Both num and n must be integers.")

    length = len(lst)
    if n is None:
        n = length
    else:
        if n == 0:
            raise ValueError("n cannot be zero.")
        if n < -1 or n >= length:
            raise ValueError("n must be between 1 and the length of the list minus 1.")

    num %= length
    if num == 0:
        return lst.copy()

    return lst[num:] + lst[:num]