def division_elements(a, b):
    # Input validation
    if not a or not b:
        return ()
    for x, y in zip(a, b):
        if x <= 0 or y <= 0:
            return ()

    # Perform element-wise division
    result = []
    for x, y in zip(a, b):
        result.append(x / y)

    return tuple(result)