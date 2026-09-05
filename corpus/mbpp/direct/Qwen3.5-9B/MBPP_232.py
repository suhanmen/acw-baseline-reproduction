def larg_nnum(data, n):
    if n <= 0:
        return []
    if n >= len(data):
        return sorted(data, reverse=True)
    return sorted(data, reverse=True)[:n]