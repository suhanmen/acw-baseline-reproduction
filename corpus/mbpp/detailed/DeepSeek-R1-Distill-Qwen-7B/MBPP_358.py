def moddiv_list(a, b):
    if not isinstance(a, list) or not isinstance(b, list):
        return None
    if len(a) == 0 or len(b) == 0:
        return []
    if len(a) != len(b):
        return [a[i] % b[i] for i in range(min(len(a), len(b)))]
    result = list(map(lambda x, y: x % y, a, b))
    return result