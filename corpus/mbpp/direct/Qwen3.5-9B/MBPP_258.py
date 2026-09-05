def count_odd(lst):
    return len([x for x in lst if x % 2 != 0])

# Verification
assert count_odd([1, 2, 3, 5, 7, 8, 10]) == 4
assert count_odd([10, 15, 14, 13, -18, 12, -20]) == 2
assert count_odd([1, 2, 4, 8, 9]) == 2