def extract_singly(tuple_list):
    seen = set()
    result = []
    for tup in tuple_list:
        for item in tup:
            if item not in seen:
                result.append(item)
                seen.add(item)
    return result