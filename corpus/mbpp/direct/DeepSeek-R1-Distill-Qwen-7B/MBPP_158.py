def min_Ops(lst, k, n):
    current_sum = sum(lst)
    target_sum = k * len(lst)

    total_diff = target_sum - current_sum
    operations_needed = 0

    # If the total difference is 0, return 0 operations
    if total_diff == 0:
        return 0

    # Calculate the operations needed
    # Each operation can change one element by at most k - element
    max_total_ops = sum(k - x for x in lst)

    if total_diff > max_total_ops or total_diff % 1 != 0:
        # Not possible within n operations
        return -1

    # Calculate the minimal operations required
    min_ops = sum(abs(x - k) for x in lst) // 2
    if total_diff % 2 != 0:
        min_ops += 1

    return min_ops if min_ops <= n else -1