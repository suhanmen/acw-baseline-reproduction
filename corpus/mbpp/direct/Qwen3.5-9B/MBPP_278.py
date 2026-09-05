def count_first_elements(t):
    count = 0
    for item in t:
        if isinstance(item, tuple):
            break
        count += 1
    return count