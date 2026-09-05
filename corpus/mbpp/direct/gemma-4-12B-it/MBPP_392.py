def get_max_sum(n):
    """
    Finds the maximum sum possible using the recurrence:
    f(n) = max(f(n/2) + f(n/3) + f(n/4) + f(n/5), n)
    The division is integer division (n // k).
    """
    memo = {}

    def solve(x):
        if x == 0:
            return 0
        if x in memo:
            return memo[x]

        # Recursive step
        res_recursive = (solve(x // 2) + 
                          solve(x // 3) + 
                          solve(x // 4) + 
                          solve(x // 5))

        # Take the maximum of the recursive sum or the value of n itself
        memo[x] = max(res_recursive, x)
        return memo[x]

    return solve(n)