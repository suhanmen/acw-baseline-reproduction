def list_to_float(data):
    result = []
    for item in data:
        converted_tuple = []
        for element in item:
            try:
                converted_tuple.append(float(element))
            except (ValueError, TypeError):
                converted_tuple.append(element)
        result.append(tuple(converted_tuple))
    return str(result)