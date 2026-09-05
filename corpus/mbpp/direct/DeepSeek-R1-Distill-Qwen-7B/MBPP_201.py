def chkList(lst):
    if not lst:
        return True
    first = lst[0]
    for item in lst[1:]:
        if item != first:
            return False
    return True

# Example usage:
assert chkList(['one','one','one']) == True
assert chkList(['one','Two','Three']) == False
assert chkList(['bigdata','python','Django']) == False