def all_unique(lst):
    if len(lst) <= 1:
        return True
    seen = set()
    for element in lst:
        if element in seen:
            return False
        seen.add(element)
    return True