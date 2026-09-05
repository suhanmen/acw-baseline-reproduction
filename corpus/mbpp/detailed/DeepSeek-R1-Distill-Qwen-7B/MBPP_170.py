def sum_range_list(lst, start, end):
    if not lst:
        return 0

    try:
        start = int(start)
        end = int(end)
    except ValueError:
        return 0

    if start < 0 or end >= len(lst):
        return 0

    if start > end:
        start, end = end, start

    if start >= len(lst):
        return 0

    total = 0
    for i in range(start, end + 1):
        total += lst[i]

    return total