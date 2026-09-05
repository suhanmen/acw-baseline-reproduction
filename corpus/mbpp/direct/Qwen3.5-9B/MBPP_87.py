def merge_dictionaries_three(d1, d2, d3):
    result = {}
    for key, value in d1.items():
        result[key] = value
    for key, value in d2.items():
        result[key] = value
    for key, value in d3.items():
        result[key] = value
    return result