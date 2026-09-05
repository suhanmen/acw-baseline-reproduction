def max_val(lst):
    if not lst:
        return None
    current_max = lst[0]
    for item in lst[1:]:
        if item > current_max:
            current_max = item
    return current_max