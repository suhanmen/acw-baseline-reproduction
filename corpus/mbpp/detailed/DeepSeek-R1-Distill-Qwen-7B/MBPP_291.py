def count_no_of_ways(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    if n == 2:
        return k * k

    same_prev = k  # same[2]
    diff_prev = k * (k - 1)  # diff[2]

    for i in range(3, n + 1):
        same_current = diff_prev
        diff_current = (same_prev + diff_prev) * (k - 1)
        same_prev, diff_prev = same_current, diff_current

    total = same_prev + diff_prev
    return total

# Test cases
print(count_no_of_ways(2, 4))  # Output: 16
print(count_no_of_ways(3, 2))  # Output: 6
print(count_no_of_ways(4, 4))  # Output: 228