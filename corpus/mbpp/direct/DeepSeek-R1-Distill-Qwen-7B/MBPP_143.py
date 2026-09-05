def find_lists(arr):
    return sum(1 for x in arr if isinstance(x, list))