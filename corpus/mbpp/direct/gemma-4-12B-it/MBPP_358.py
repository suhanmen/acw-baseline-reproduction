def moddiv_list(list1, list2):
    """
    Finds the modulo division of two lists using map and lambda.
    """
    return list(map(lambda x, y: x % y, list1, list2))