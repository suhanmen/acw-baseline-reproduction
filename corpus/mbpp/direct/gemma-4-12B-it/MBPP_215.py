def decode_list(data):
    """
    Decodes a run-length encoded list.
    If an element is a list of two elements [count, value], it repeats the value count times.
    Otherwise, it treats the element as a single value.
    """
    decoded = []
    for item in data:
        if isinstance(item, list) and len(item) == 2:
            count, value = item
            decoded.extend([value] * count)
        else:
            decoded.append(item)
    return decoded