def min_val(lst):
    min_val = None
    for item in lst:
        if isinstance(item, int):
            if min_val is None or item < min_val:
                min_val = item
    return min_val