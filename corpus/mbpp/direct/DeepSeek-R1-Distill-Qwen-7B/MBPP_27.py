def remove(strings):
    return [s.replace(r'\d+', '') for s in strings]