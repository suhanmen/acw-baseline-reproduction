def eulerian_num(n, m):
    """
    Calculate the Eulerian number a(n, m), which counts the number of permutations
    of 1 to n with exactly m ascents.

    Args:
        n (int): The number of elements in the permutation.
        m (int): The number of required ascents.

    Returns:
        int: The Eulerian number a(n, m).

    Raises:
        ValueError: If n or m are negative integers, or if m is greater than or equal to n.
    """
    if not (isinstance(n, int) and isinstance(m, int)):
        raise ValueError("Both n and m must be integers.")

    if n < 0 or m < 0 or m >= n:
        raise ValueError("n and m must be non-negative integers, and m must be less than n.")

    # Base cases
    if n == 0:
        return 1 if m == 0 else 0

    # Initialize a 2D array to store Eulerian numbers
    eulerian = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case for n=1
    eulerian[1][0] = 1

    for i in range(2, n + 1):
        for j in range(i - 1):
            eulerian[i][j] = (i - j - 1) * eulerian[i-1][j] + (j + 1) * eulerian[i-1][j + 1]

    return eulerian[n][m]