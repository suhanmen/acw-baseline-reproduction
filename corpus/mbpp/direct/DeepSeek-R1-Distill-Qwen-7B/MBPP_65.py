def recursive_list_sum(lst):
    total = 0
    for element in lst:
        if isinstance(element, list):
            total += recursive_list_sum(element)
        else:
            total += element
    return total