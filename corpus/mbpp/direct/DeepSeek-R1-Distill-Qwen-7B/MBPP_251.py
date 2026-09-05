def insert_element(lst, element):
    result = []
    for item in lst:
        result.append(element)
        result.append(item)
    return result