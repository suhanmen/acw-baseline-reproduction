def harmonic_sum(n):
    if n < 1:
        return 0.0
    total = 0.0
    for i in range(1, n):
        total += 1 / i
    return total

# Explanation:
# The harmonic sum of n-1 is the sum of reciprocals of integers from 1 to n-1.
# For example, harmonic_sum(4) = 1 + 1/2 + 1/3 = 1.8333333333333333