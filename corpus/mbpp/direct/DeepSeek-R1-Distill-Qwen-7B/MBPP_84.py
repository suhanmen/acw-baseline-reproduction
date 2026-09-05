def sequence(n, memo={1: 1, 2: 1}):
    if n in memo:
        return memo[n]
    memo[n] = sequence(n - sequence(n - 1), memo) + sequence(sequence(n - 1), memo)
    return memo[n]

assert sequence(10) == 6
assert sequence(2) == 1
assert sequence(3) == 2

sequence(10)