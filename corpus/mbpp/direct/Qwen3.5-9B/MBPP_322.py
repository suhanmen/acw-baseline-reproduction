def position_min(lst):
    if not lst:
        return []
    min_val = min(lst)
    return [i for i, v in enumerate(lst) if v == min_val]