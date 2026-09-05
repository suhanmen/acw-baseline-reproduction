def tuple_to_int(tup):
    if not tup:
        return 0
    string_elements = [str(x) for x in tup]
    concatenated = ''.join(string_elements)
    return int(concatenated)