def larg_nnum(dataset, n):
    if n <= 0:
        return []
    if n > len(dataset):
        return sorted(dataset, reverse=True)
    sorted_dataset = sorted(dataset, reverse=True)
    return sorted_dataset[:n]