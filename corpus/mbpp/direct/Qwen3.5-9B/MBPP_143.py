def find_lists(t):
    return sum(1 for item in t if isinstance(item, list))