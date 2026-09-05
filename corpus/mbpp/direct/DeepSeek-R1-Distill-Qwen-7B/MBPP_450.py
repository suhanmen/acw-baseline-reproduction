def extract_string(lst, size):
    start_index = (len(lst) - size) if (len(lst) >= size) else 0
    if start_index < 0:
        start_index = 0
    return lst[start_index:]