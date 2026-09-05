def intersection_nested_lists(list1, list2):
    def flatten(lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result

    flat1 = set(flatten(list1))
    result = []
    for sublist in list2:
        intersection = sorted(set(sublist) & flat1)
        result.append(intersection)
    return result