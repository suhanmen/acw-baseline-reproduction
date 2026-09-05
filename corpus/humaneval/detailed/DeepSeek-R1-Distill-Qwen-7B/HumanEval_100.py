def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    if n == 1:
        return [1]

    # Determine if n is odd or even
    is_odd = n % 2 != 0

    # Initialize the list with the first level
    stones = [n]

    # Generate each subsequent level
    for i in range(1, n):
        if is_odd:
            # Next odd number after the current level's stones
            next_stones = stones[-1] + 2 if stones[-1] % 2 == 0 else stones[-1] + 2
        else:
            # Next even number after the current level's stones
            next_stones = stones[-1] + 2 if stones[-1] % 2 == 0 else stones[-1] + 2

        stones.append(next_stones)

    return stones