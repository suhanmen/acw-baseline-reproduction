def insert_element(lst, element):
    if not lst:
        return [element]
    return [element] + lst[0:1] + [element] + lst[1:1] + [element] + lst[2:] if len(lst) >= 2 else [element] + lst[0:1] + [element] + lst[1:]