def list_to_float(data):
    def safe_float(x):
        try:
            return float(x)
        except (TypeError, ValueError):
            return x

    result = []
    for item in data:
        converted = tuple(safe_float(x) if isinstance(x, str) else x for x in item)
        result.append(converted)
    return str(result)