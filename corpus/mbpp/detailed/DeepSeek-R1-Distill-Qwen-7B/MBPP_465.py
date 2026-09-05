def drop_empty(dct):
    if not isinstance(dct, dict):
        raise TypeError("Input must be a dictionary")

    result = {}
    for key, value in dct.items():
        # Determine if the value is non-empty
        if (isinstance(value, str) and value.strip()) or \
           (isinstance(value, (list, dict)) and value) or \
           (isinstance(value, (int, float)) and value != 0):
            result[key] = value
    return result