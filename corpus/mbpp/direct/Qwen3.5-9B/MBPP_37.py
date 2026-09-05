def sort_mixed_list(lst):
    integers = sorted([x for x in lst if isinstance(x, int)])
    strings = sorted([x for x in lst if isinstance(x, str)])
    return integers + strings