def count_integer(lst):
    count = 0
    for item in lst:
        if isinstance(item, int):
            count += 1
    return count