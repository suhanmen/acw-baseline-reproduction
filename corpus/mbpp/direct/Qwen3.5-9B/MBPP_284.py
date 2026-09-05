def check_element(lst, target):
    return all(isinstance(item, str) and item == target for item in lst)