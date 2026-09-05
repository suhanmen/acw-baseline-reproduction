def position_max(lst):
    if not lst:
        return []

    max_val = max(lst)
    indices = []

    for index, value in enumerate(lst):
        if value == max_val:
            indices.append(index)

    return indices