def sequence(n):
    """
    Finds the n-th number in the Newman-Conway sequence.

    Args:
        n (int): The position in the sequence to find.

    Returns:
        int: The n-th number in the sequence.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")

    memo = {1: 1, 2: 1}

    def helper(k):
        if k in memo:
            return memo[k]
        result = sequence(k - 1) + sequence(k - 2)
        memo[k] = result
        return result

    return helper(n)