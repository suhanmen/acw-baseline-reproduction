def count_integer(data):
    count = 0
    for item in data:
        if isinstance(item, int) and not isinstance(item, bool):
            count += 1
    return count