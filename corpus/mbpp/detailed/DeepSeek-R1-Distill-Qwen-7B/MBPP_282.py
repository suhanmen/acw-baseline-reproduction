def sub_list(a, b):
    # Check if inputs are lists
    if not isinstance(a, list) or not isinstance(b, list):
        return None

    # Check if lists have the same length
    if len(a) != len(b):
        return None

    # Handle empty lists
    if len(a) == 0 or len(b) == 0:
        return None

    # Perform element-wise subtraction
    result = map(lambda x, y: x - y, a, b)

    # Convert result to a list and return
    return list(result)