import math

def count_binary_seq(n):
    total = 0
    for k in range(n + 1):
        total += math.comb(n, k) * math.comb(n, k)
    return total

# Verify the solution with the given assertions
assert count_binary_seq(1) == 2
assert count_binary_seq(2) == 6
assert count_binary_seq(3) == 20