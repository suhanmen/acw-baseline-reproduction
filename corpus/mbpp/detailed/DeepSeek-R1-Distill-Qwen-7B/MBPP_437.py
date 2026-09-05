def remove_odd(s):
    even_indices = [char for index, char in enumerate(s) if index % 2 == 0]
    return ''.join(even_indices)