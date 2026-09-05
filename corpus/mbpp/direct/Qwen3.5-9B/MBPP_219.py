def extract_min_max(t, k):
    if k <= 0 or k > len(t):
        return t
    lst = list(t)
    lst.sort()
    min_k = lst[:k]
    max_k = lst[-k:] if k > 1 else [lst[-1]]
    return min_k + max_k if len(max_k) > 1 else min_k + max_k