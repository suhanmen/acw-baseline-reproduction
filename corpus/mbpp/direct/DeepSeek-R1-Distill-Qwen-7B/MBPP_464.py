def check_value(dictionary, value):
    if not dictionary:
        return False  # Assuming empty dict should return False
    first_value = dictionary.values().__next__()
    for v in dictionary.values():
        if v != first_value:
            return False
    return first_value == value