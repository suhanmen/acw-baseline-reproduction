def get_max_sum(n):
    memo = {}

    def helper(x):
        if x <= 0:
            return 0
        if x in memo:
            return memo[x]
        option1 = x
        option2 = 0
        if x > 2:
            option2 = helper(x // 2) + helper(x // 3) + helper(x // 4) + helper(x // 5)
        result = max(option1, option2)
        memo[x] = result
        return result

    return helper(n)