def common_element(list1, list2):
    for element in list1:
        if element in list2:
            return True
    return False

# The function `common_element` checks for at least one common element between two lists.
# It iterates through each element in `list1` and checks if it exists in `list2`.
# If a common element is found, it returns `True`; otherwise, it returns `False`.