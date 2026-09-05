def position_min(lst):
    min_val = min(lst)
    return [i for i, val in enumerate(lst) if val == min_val]