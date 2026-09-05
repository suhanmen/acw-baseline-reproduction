def Find_Min(lst):
    """
    Finds the sublist having the minimum length from a list of lists.
    If multiple sublists have the same minimum length, the first one encountered is returned.
    """
    if not lst:
        return None

    # Use min with a key that looks at the length of the inner lists
    return min(lst, key=len)

if __name__ == "__main__":
    assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
    assert Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
    assert Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']