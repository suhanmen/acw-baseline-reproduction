def remove_empty(lst):
    return [item for item in lst if not isinstance(item, list) or len(item) > 0]