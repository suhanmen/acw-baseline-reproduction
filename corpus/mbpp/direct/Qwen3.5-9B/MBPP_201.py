def chkList(lst):
    if not lst:
        return True
    return all(element == lst[0] for element in lst)