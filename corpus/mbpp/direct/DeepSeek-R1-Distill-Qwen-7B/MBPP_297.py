def flatten_list(nested_list):
    result = []
    for element in nested_list:
        if isinstance(element, list):
            for item in element:
                result.append(item)
        else:
            result.append(element)
    return result