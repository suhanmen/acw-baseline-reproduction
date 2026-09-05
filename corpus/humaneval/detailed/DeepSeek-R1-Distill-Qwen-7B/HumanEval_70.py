def strange_sort_list(lst):
    """
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    """
    if not lst:
        return []

    remaining = lst.copy()
    result = []
    should_min = True

    while remaining:
        if should_min:
            current = min(remaining)
            result.append(current)
            remaining.remove(current)
        else:
            current = max(remaining)
            result.append(current)
            remaining.remove(current)
        should_min = not should_min

    return result