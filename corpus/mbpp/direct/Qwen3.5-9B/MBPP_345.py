def diff_consecutivenums(lst):
    if not lst:
        return []
    return [lst[i + 1] - lst[i] for i in range(len(lst) - 1)]