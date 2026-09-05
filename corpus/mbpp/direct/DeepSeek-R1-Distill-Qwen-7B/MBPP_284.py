def check_element(lst, target):
    for item in lst:
        if item != target:
            return False
    return True