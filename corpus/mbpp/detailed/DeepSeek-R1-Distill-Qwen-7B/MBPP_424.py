def extract_rear(s):
    if not isinstance(s, tuple):
        raise ValueError("Input must be a tuple")

    result = []
    for element in s:
        if not isinstance(element, str) or len(element) == 0:
            raise ValueError("All elements must be non-empty strings")

        last_char = element[-1]
        result.append(last_char)

    return result