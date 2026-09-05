def Find_Max(lst):
    if not lst:
        return []
    return max(lst, key=len)