def decode_list(encoded):
    result = []
    i = 0
    while i < len(encoded):
        current = encoded[i]
        if isinstance(current, list) and len(current) >= 2:
            # It's a run
            count = current[0]
            val = current[1]
            result.extend([val] * count)
            i += 2
        else:
            # It's a single element
            result.append(current)
            i += 1
    return result