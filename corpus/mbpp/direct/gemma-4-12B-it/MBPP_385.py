def get_perrin(n: int) -> int:
    """
    Finds the n'th Perrin number using recursion.
    The Perrin sequence is defined as:
    P(0) = 3
    P(1) = 0
    P(2) = 2
    P(n) = P(n-2) + P(n-3) for n > 2
    """
    if n == 0:
        return 3
    if n == 1:
        return 0
    if n == 2:
        return 2

    # To optimize the recursion and avoid exponential time complexity, 
    # we can use memoization.
    memo = {}

    def recursive_perrin(k):
        if k == 0: return 3
        if k == 1: return 0
        if k == 2: return 2
        if k in memo:
            return memo[k]

        memo[k] = recursive_perrin(k - 2) + recursive_perrin(k - 3)
        return memo[k]

    return recursive_perrin(n)