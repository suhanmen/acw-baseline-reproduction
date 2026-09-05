def min_Ops(lst, k):
    # Input validation
    if not lst or len(lst) < 3:
        return -1
    if k < 2:
        return -1
    if k >= len(lst) or k < len(lst) - 1:
        # Check if all elements are the same
        if all(x == lst[0] for x in lst):
            return 0
        # Otherwise, it's impossible
        return -1

    # Calculate differences from the smallest element
    min_val = min(lst)
    diffs = [x - min_val for x in lst]

    # Check if any difference exceeds k
    for d in diffs:
        if d > k:
            return -1

    # Check if all elements are the same
    if all(d == 0 for d in diffs):
        return 0

    # Sort the differences
    sorted_diffs = sorted(diffs)

    # Calculate the total operations needed
    total_ops = 0
    for i in range(len(sorted_diffs)):
        if sorted_diffs[i] == 0:
            continue
        total_ops += sorted_diffs[i] * (i + 1)

    # Compare total_ops with k
    if total_ops <= k:
        return total_ops
    else:
        return -1