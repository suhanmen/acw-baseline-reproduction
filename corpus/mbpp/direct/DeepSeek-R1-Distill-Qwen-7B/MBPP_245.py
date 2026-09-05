def max_sum(arr, n):
    if n == 0:
        return 0
    increasing = [x for x in arr if x >= arr[0]]
    decreasing = [x for x in arr if x <= arr[-1]]
    total = increasing[0]
    for i in range(1, len(increasing)):
        total += increasing[i]
    for i in range(1, len(decreasing)):
        total += decreasing[i]
    return total

assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9], 9) == 194
assert max_sum([80, 60, 30, 40, 20, 10], 6) == 210
assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30], 8) == 138