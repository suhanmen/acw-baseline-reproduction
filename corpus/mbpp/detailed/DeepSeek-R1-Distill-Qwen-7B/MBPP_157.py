def encode_list(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    if not lst:
        return []

    current_value = lst[0]
    count = 1
    result = []

    for value in lst[1:]:
        if value == current_value:
            count += 1
        else:
            result.append([count, current_value])
            current_value = value
            count = 1

    result.append([count, current_value])

    return result