def empty_dit(lst):
    """
    Checks whether all dictionaries in a list are empty.
    If the input is not a list but an empty dictionary, it also returns True.
    """
    if isinstance(lst, dict):
        return not lst

    for d in lst:
        if isinstance(d, dict) and d:
            return False
    return True

if __name__ == "__main__":
    assert empty_dit([{},{},{}]) == True
    assert empty_dit([{1,2},{},{}]) == False
    assert empty_dit({}) == True